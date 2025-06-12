## Lee-Ann Seegets (11/15P)

### 1. Exploring Parameters (2.5/5)
* selected hyperparameter values make sense
    * only change the number of training images not the overall number of images in the dataset (-1P)
    * from the 250 images per condition you additionally append the no_gestures, that results in irregular training- & testsets
* networks were trained correctly
    * yep (1P)
* there are results
    * yep (1P)
* results are reported and visualized appropriately
    * Plot for inference time is a bit confusing (title for x-axes makes no sense for average inference time) (-0.5P)
    * report could be a bit more structured (-0.5P)
    * report is also minimalistic, no overall recommendation (-0.5P)


### 2. Gathering a Dataset (4.5/5)
* sufficient images captured
    * all images at the same place (-0.5P)
* sufficient images annotated
    * yep (2P)
* annotations are compatible to the HaGRID dataset
    * yep (1P)
* confusion matrix
    * yep (1P)


### 3. Gesture-based Media Controls (4/5)
* three hand poses are tracked and distinguished reliably 
    * a cool down for start/stop would be nice (-0.5P)
    * like/dislike is predicted semi good (-0.5P)
* three media control features are implemented
    * yep (1P)
* mapping of gestures to media controls works and makes sense
    * yep (1P)
* low latency between gesture and the system’s reaction
    * yep (1P)