#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os
import sys
import importlib

# Add the path to the 'modules' directory to the system path
sys.path.append(r"C:\Users\rober\Downloads\CannabisClassifier\Modules")

# Load the 'modules' package
import modules

for module_file in os.listdir(modules.__path__[0]):
    if module_file.endswith('.py') and module_file != '__init__.py':
        module_name = module_file[:-3]  # Remove the '.py' extension
        module = importlib.import_module(f'modules.{module_name}')
        
        # Import all functions and classes from the module into the global namespace
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr):
                globals()[attr_name] = attr

# Import the necessary functions from their respective modules
from modules.image_conversion import run_image_conversion
from modules.preprocessing import run_preprocessing
from modules.feature_extraction import run_feature_extraction
from modules.show_images import show_unhealthy_images
from modules.canny_test import run_canny_test
from modules.analyze import process_images  # Import the process_images function from analyze module

# Set folder paths
arw_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!'
png_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\png/'

# Run image conversion
run_image_conversion(arw_folder, png_folder)

# Set preprocessed folder paths
preprocessed_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed\\'

# Run preprocessing
run_preprocessing(png_folder, preprocessed_folder)

# Set feature extraction folder paths
save_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\\'

# Run feature extraction
features_array = run_feature_extraction(preprocessed_folder, save_folder)

# Show generated images
folder_path_1 = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\\'
show_generated_images(folder_path_1)

# Run Canny test
preprocessed_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\gray\\'
output_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\canny_output_4\\'

run_canny_test(preprocessed_folder, output_folder)

# Show unhealthy images
folder_path = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\\'
unhealthy_indices = [
    5, 8, 9, 10, 12, 14, 15, 22, 26, 34, 35, 45, 53, 54, 59, 61, 62,
    63, 64, 65, 66, 67, 68, 74, 87, 94, 103, 105, 106, 113, 114, 115,
117, 118, 119
]

show_unhealthy_images(folder_path, unhealthy_indices)
#Run the process_images function from the analyze module

process_images()
