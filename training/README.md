# Usage:
1. Prepare a set of images of the known people you want to recognize. Organize the images in a single directory
with a sub-directory for each known person.

2. Then, call the 'train' function with the appropriate parameters. Make sure to pass in the 'model_save_path' if you
want to save the model to disk so you can re-use the model without having to re-train it.

3. Call 'predict' and pass in your trained model to recognize the people in an unknown image.

NOTE: This example requires scikit-learn to be installed! You can install it with pip:

$ pip3 install scikit-learn

# Underlying Functions

### Train Function
Trains a classifier for face recognition.

* param train_dir: directory that contains a sub-directory for each known person, with its name.
* param model_save_path: (optional) path to save model on disk
* param n_neighbors: (optional) number of neighbors to weigh in classification. Chosen automatically if not specified
* param knn_algo: (optional) underlying data structure to support knn.default is ball_tree
* param verbose: verbosity of training
* return: returns classifier that was trained on the given data.

#### Structure:
* \<train_dir\>
* * \<person1\>
* * * \<somename1\>.jpeg
* * * \<somename2\>.jpeg
* * * ...
* * \<person2\>
* * * \<somename1\>.jpeg
* * * \<somename2\>.jpeg
* * * ...

### Predict Function
Recognizes faces in given image using a trained classifier

* param X_img_path: path to image to be recognized
* param knn_clf: (optional) a classifier object. if not specified, model_save_path must be specified.
* param model_path: (optional) path to a pickled classifier. if not specified, model_save_path must be knn_clf.
* param distance_threshold: (optional) distance threshold for face classification. the larger it is, the more chance
* of mis-classifying an unknown person as a known one.
* return: a list of names and face locations for the recognized faces in the image: [(name, bounding box), ...].
For faces of unrecognized persons, the name 'unknown' will be returned.
