import os
import glob
import rawpy
import cv2
import numpy as np
import shutil
from skimage import feature
from skimage import color
from PIL import Image

def convert_arw_to_png(arw_folder, png_folder):
    arw_files = glob.glob(os.path.join(arw_folder, "*.ARW"))
    os.makedirs(png_folder, exist_ok=True)

    for arw_file in arw_files:
        with rawpy.imread(arw_file) as raw:
            rgb = raw.postprocess()
        png_file = os.path.join(png_folder, os.path.splitext(os.path.basename(arw_file))[0] + '.png')
        Image.fromarray(rgb).save(png_file)

def preprocess_images(png_folder, preprocessed_folder):
    png_files = glob.glob(os.path.join(png_folder, "*.png"))
    os.makedirs(preprocessed_folder, exist_ok=True)

    for png_file in png_files:
        img = cv2.imread(png_file)

        # Resize the image
        img_resized = cv2.resize(img, (500, 500))

        # Apply Gaussian blur
        img_blurred = cv2.GaussianBlur(img_resized, (5, 5), 0)

        # Save the preprocessed images
        preprocessed_file = os.path.join(preprocessed_folder, os.path.basename(png_file))
        cv2.imwrite(preprocessed_file, img_blurred)

def extract_features(preprocessed_folder, save_folder):
    preprocessed_files = glob.glob(os.path.join(preprocessed_folder, "*.png"))

    for i, preprocessed_file in enumerate(preprocessed_files):
        img = cv2.imread(preprocessed_file)

        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Save the grayscale image
        gray_file = os.path.join(save_folder, os.path.basename(preprocessed_file))
        cv2.imwrite(gray_file, gray_img)

        # Extract the histogram of oriented gradients (HOG) feature
        hog_feature = feature.hog(gray_img)

        # Gaussian blur
        blur = cv2.GaussianBlur(gray_img, (5, 5), 0)
        # Save the blurred image
        blur_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_blur.png')
        cv2.imwrite(blur_file, blur)

        edges = cv2.Canny(gray_img, 100, 200)

        # Save the edges image
        edges_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_edges.png')
        cv2.imwrite(edges_file, edges)

        # Compute the color histogram
        color_hist = color.rgb2gray(img).flatten()

        # Convert the image to HSV color space to identify the location of different colors
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Save the HSV image
        hsv_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_hsv.png')
        cv2.imwrite(hsv_file, hsv)

        # Combine the features
        combined_features = np.concatenate((hog_feature, color_hist))
        num_features = len(hog_feature) + len(color_hist)
        
        if i == 0:
            global features_array
            features_array = np.empty((len(preprocessed_files), num_features))
                
        features_array[i] = combined_features
            
        return features_array


def main():
    arw_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!'
    png_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/png/'

    convert_arw_to_png(arw_folder, png_folder)

    preprocessed_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed/'

    preprocess_images(png_folder, preprocessed_folder)

    save_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed_step2/'

    features_array = extract_features(preprocessed_folder, save_folder)

    # Save the features array to an .npy file
    np.save('array_preprocess.npy', features_array)

    # Load the array from the .npy file
    array = np.load('array_preprocess.npy')
    print(f"Features array saved to: {os.path.abspath('array_preprocess.npy')}")

    # Move the features array .npy file to the save_folder
    src_path = 'array_preprocess.npy'
    dst_path = os.path.join(save_folder, 'array_preprocess.npy')
    os.replace(src_path, dst_path)

    # Move the grayscale blurred images to a separate folder
    source_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed_step2/'
    destination_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed_step2/gray/'

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all the files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file ends with "_blur.png"
        if filename.endswith("_blur.png"):
            # Construct the file paths for the source and destination
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Move the file from the source folder to the destination folder
            shutil.move(source_path, destination_path)

if __name__ == "__main__":
    main()




####################################################


# import os
# import glob
# import rawpy
# import cv2
# import numpy as np
# from skimage import feature
# from skimage import color
# from PIL import Image

# def convert_arw_to_png(arw_folder, png_folder):
#     arw_files = glob.glob(os.path.join(arw_folder, "*.ARW"))
#     os.makedirs(png_folder, exist_ok=True)

#     for arw_file in arw_files:
#         with rawpy.imread(arw_file) as raw:
#             rgb = raw.postprocess()
#         png_file = os.path.join(png_folder, os.path.splitext(os.path.basename(arw_file))[0] + '.png')
#         Image.fromarray(rgb).save(png_file)

# def preprocess_images(png_folder, preprocessed_folder):
#     png_files = glob.glob(os.path.join(png_folder, "*.png"))
#     os.makedirs(preprocessed_folder, exist_ok=True)

#     for png_file in png_files:
#         img = cv2.imread(png_file)

#                 # Resize the image
#         img_resized = cv2.resize(img, (500, 500))

#                 # Apply Gaussian blur
#         img_blurred = cv2.GaussianBlur(img_resized, (5, 5), 0)

#                 # Save the preprocessed images
#         preprocessed_file = os.path.join(preprocessed_folder, os.path.basename(png_file))
#         cv2.imwrite(preprocessed_file, img_blurred)

# def extract_features(preprocessed_folder, save_folder):
#     preprocessed_files = glob.glob(os.path.join(preprocessed_folder, "*.png"))

#     for i, preprocessed_file in enumerate(preprocessed_files):
#         img = cv2.imread(preprocessed_file)

#             # Convert the image to grayscale
#         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#             # Save the grayscale image
#         gray_file = os.path.join(save_folder, os.path.basename(preprocessed_file))
#         cv2.imwrite(gray_file, gray_img)

#             # Extract the histogram of oriented gradients (HOG) feature
#         hog_feature = feature.hog(gray_img)

#             # Gaussian blur
#         blur = cv2.GaussianBlur(gray_img, (5, 5), 0)
#             # Save the blurred image
#         blur_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_blur.png')
#         cv2.imwrite(blur_file, blur)

#         edges = cv2.Canny(gray_img, 100, 200)

#             # Save the edges image
#         edges_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_edges.png')
#         cv2.imwrite(edges_file, edges)

#             # Compute the color histogram
#         color_hist = color.rgb2gray(img).flatten()

#             # Convert the image to HSV color space to identify the location of different colors
#         hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#             # Save the HSV image
#         hsv_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_hsv.png')
#         cv2.imwrite(hsv_file, hsv)

#             # Combine the features
#         combined_features = np.concatenate((hog_feature, color_hist))
#         num_features = len(hog_feature) + len(color_hist)
            
#         if i == 0:
#             global features_array
#             features_array = np.empty((len(preprocessed_files), num_features))
                
#         features_array[i] = combined_features
            
#         return features_array



# def main():
#     arw_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!'
#     png_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/png/'

#     convert_arw_to_png(arw_folder, png_folder)

#     preprocessed_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed/'

#     preprocess_images(png_folder, preprocessed_folder)

#     save_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed_step2/'

#     features_array = extract_features(preprocessed_folder, save_folder)

#     # Get the current working directory
#     current_dir = os.getcwd()

#     # Construct the full file path
#     file_path = os.path.join(current_dir, "array_preprocess.npy")

#     # Load the array from the .npy file
#     array = np.load(file_path)
#     print(f"Features array saved to: {os.path.abspath('array_preprocess.npy')}")

#     # Define the source and destination paths
#     dst_path = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed_step2/array_preprocess.npy'

#     # Copy the file
#     os.makedirs(os.path.dirname(dst_path), exist_ok=True)  # create the destination folder if it does not exist
#     os.replace(file_path, dst_path)  # replace the file in the destination folder with the new file

#     source_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed_step2/'
#     destination_folder = r'C:/Users/rober/Pictures/mar 21/purple !!!/preprocessed_step2/gray/'

#     # Create the destination folder if it doesn't exist
#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)

#     # Loop through all the files in the source folder
#     for filename in os.listdir(source_folder):
#         # Check if the file ends with "_blur.png"
#         if filename.endswith("_blur.png"):
#             # Construct the file paths for the source and destination
#             source_path = os.path.join(source_folder, filename)
#             destination_path = os.path.join(destination_folder, filename)

#             # Move the file from the source folder to the destination folder
#             shutil.move(source_path, destination_path)

# if __name__ == "__main__":
#     main()

# ##################
# ###
# ###  iteration 2
# ####################
# # import os
# # import glob
# # import rawpy
# # import cv2
# # import numpy as np
# # from skimage import feature
# # from skimage import color
# # from PIL import Image
# # import shutil

# # def convert_arw_to_png(arw_folder, png_folder):
# #     arw_files = glob.glob(os.path.join(arw_folder, "*.ARW"))
# #     os.makedirs(png_folder, exist_ok=True)

# #     for arw_file in arw_files:
# #         with rawpy.imread(arw_file) as raw:
# #             rgb = raw.postprocess()
# #         png_file = os.path.join(png_folder, os.path.splitext(os.path.basename(arw_file))[0] + '.png')
# #         Image.fromarray(rgb).save(png_file)

# # def main():
        
# #     arw_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!'
# #     png_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\png/'

# #     convert_arw_to_png(arw_folder, png_folder)

# #     png_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\png\\'
# #     preprocessed_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed\\'

# #     def preprocess_images(png_folder, preprocessed_folder):
# #         png_files = glob.glob(os.path.join(png_folder, "*.png"))
# #         os.makedirs(preprocessed_folder, exist_ok=True)

# #         for png_file in png_files:
# #             img = cv2.imread(png_file)

# #             # Resize the image
# #             img_resized = cv2.resize(img, (500, 500))

# #             # Apply Gaussian blur
# #             img_blurred = cv2.GaussianBlur(img_resized, (5, 5), 0)

# #             # Save the preprocessed images
# #             preprocessed_file = os.path.join(preprocessed_folder, os.path.basename(png_file))
# #             cv2.imwrite(preprocessed_file, img_blurred)

# #     preprocess_images(png_folder, preprocessed_folder)


# #     def extract_features(preprocessed_folder, save_folder):
# #         preprocessed_files = glob.glob(os.path.join(preprocessed_folder, "*.png"))

# #         for i, preprocessed_file in enumerate(preprocessed_files):
# #             img = cv2.imread(preprocessed_file)

# #             # Convert the image to grayscale
# #             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #             # Save the grayscale image
# #             gray_file = os.path.join(save_folder, os.path.basename(preprocessed_file))
# #             cv2.imwrite(gray_file, gray_img)

# #             # Extract the histogram of oriented gradients (HOG) feature
# #             hog_feature = feature.hog(gray_img)

# #             # Gaussian blur
# #             blur = cv2.GaussianBlur(gray_img, (5, 5), 0)
# #             # Save the blurred image
# #             blur_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_blur.png')
# #             cv2.imwrite(blur_file, blur)

# #             edges = cv2.Canny(gray_img, 100, 200)

# #             # Save the edges image
# #             edges_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_edges.png')
# #             cv2.imwrite(edges_file, edges)

# #             # Compute the color histogram
# #             color_hist = color.rgb2gray(img).flatten()

# #             # Convert the image to HSV color space to identify the location of different colors
# #             hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# #             # Save the HSV image
# #             hsv_file = os.path.join(save_folder, os.path.splitext(os.path.basename(preprocessed_file))[0] + '_hsv.png')
# #             cv2.imwrite(hsv_file, hsv)

# #             # Combine the features
# #             combined_features = np.concatenate((hog_feature, color_hist))
# #             num_features = len(hog_feature) + len(color_hist)
            
# #             if i == 0:
# #                 global features_array
# #                 features_array = np.empty((len(preprocessed_files), num_features))
                
# #             features_array[i] = combined_features
            
# #         return features_array




# #     # Get the current working directory
# #     current_dir = os.getcwd()

# #     # Construct the full file path
# #     file_path = os.path.join(current_dir, "array_preprocess.npy")

# #     # Load the array from the .npy file
# #     array = np.load(file_path)
# #     print(f"Features array saved to: {os.path.abspath('array_preprocess.npy')}")


# #     # Define the source and destination paths
# #     dst_path = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\array_preprocess.npy'

# #     # Copy the file
# #     os.makedirs(os.path.dirname(dst_path), exist_ok=True) # create the destination folder if it does not exist
# #     os.replace(file_path, dst_path) # replace the file in the destination folder with the new file


# #     # Array looks beautiful doesnt it? Remember, CANNY is up here, which means we can always tweak our canny settings, as well as everything else, this is like the fine tuning engine right here. 



# #     # this makes the gray folder, and moves all the gray images into it

# #     import shutil

# #     source_folder = 'C:\\Users\\rober\\Pictures\\mar 21\\purple !!!\\preprocessed_step2\\'
# #     destination_folder = 'C:\\Users\\rober\\Pictures\\mar 21\\purple !!!\\preprocessed_step2\\gray\\'

# #     # Create the destination folder if it doesn't exist
# #     if not os.path.exists(destination_folder):
# #         os.makedirs(destination_folder)

# #     # Loop through all the files in the source folder
# #     for filename in os.listdir(source_folder):
# #         # Check if the file ends with "_blur.png"
# #         if filename.endswith("_blur.png"):
# #             # Construct the file paths for the source and destination
# #             source_path = os.path.join(source_folder, filename)
# #             destination_path = os.path.join(destination_folder, filename)

# #             # Move the file from the source folder to the destination folder
# #             shutil.move(source_path, destination_path)


# #     if __name__ == "__main__":
# #         main()