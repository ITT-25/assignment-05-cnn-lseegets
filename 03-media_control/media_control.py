import cv2
import time
import numpy as np
from keras.models import load_model
from pynput.keyboard import Controller, Key

keyboard = Controller()

PREDICTION_COOLDOWN = 1
IMG_SIZE = 64
CONDITIONS = ['like', 'no_gesture', 'dislike', 'stop' ]
COLOR_CHANNELS = 3
SKIN_LOWER = np.array([0, 48, 80])
SKIN_UPPER = np.array([20, 255, 255])

last_prediction_time = 0
model = load_model("gesture_recognition.keras")

cap = cv2.VideoCapture(0)

def gesture_to_key(gesture):
    if gesture == "like":
        keyboard.press(Key.media_volume_up)
    elif gesture == "dislike":
        keyboard.press(Key.media_volume_down)
    elif gesture == "stop":
        keyboard.press(Key.media_play_pause)

while True:
    _, frame = cap.read()

    # Detect skin tone
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, SKIN_LOWER, SKIN_UPPER)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # If there are contours, get the bounding box of the largest one (assuming the largest
        # one will be a hand)
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        hand_bbox = frame[y:y+h, x:x+w]

        # Resize that bounding box to match the training images
        img = cv2.resize(hand_bbox, (IMG_SIZE, IMG_SIZE))
        img = img.astype('float32') / 255.
        img = img.reshape(1, IMG_SIZE, IMG_SIZE, COLOR_CHANNELS)

        current_time = time.time()
        # If the program isn't currently in cooldown, make a prediction using the contour
        if current_time - last_prediction_time >= PREDICTION_COOLDOWN:
            preds = model.predict(img)
            # Get the gesture with the highest probability
            index = np.argmax(preds, axis=1)[0]
            gesture = CONDITIONS[index]
            print("Predicted gesture: ", gesture)
            gesture_to_key(gesture)
            last_prediction_time = current_time

    cv2.imshow('Media Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
