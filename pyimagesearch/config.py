# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
import os

# Define the base path to the input dataset and then use it to derive the path to the input images and annotation files
path_dir = "/content/multi-class-object-detection-and-bounding-box"
base_path = "dataset"
images_path = os.path.join(path_dir, base_path, "images")
annotations_path = os.path.join(path_dir, base_path, "annotations")

# Define the path to the base output directory
base_output = "output"

# Define the path to the output model, label binarizer, plots output directory and the testing image paths
model_path = os.path.join(path_dir, base_output, "detector.h5")
le_path = os.path.join(path_dir, base_output, "le.pickle")
plots_path = os.path.join(path_dir, base_output, "plots")
test_filenames = os.path.join(path_dir, base_output, "test_paths.txt")

# Initialize the initial learning rate, number of epochs to train for and the batch size
alpha = 1e-4
epochs = 20
batch_size = 32