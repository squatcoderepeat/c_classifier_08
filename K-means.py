import os
import cv2
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans


def main():
    # Define the source and destination paths
    folder_path_1 = Path(r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2')
    output_folder = folder_path_1 / "kmeans_output"

    # Create the output folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    # Define the number of clusters
    num_clusters = 8

    # Loop over each file in the source folder
    for filename in folder_path_1.iterdir():
        if filename.name.endswith('hsv.png'):
            # Load the preprocessed image
            image = cv2.imread(str(filename))

            # Flatten the image into a 2D array of pixels
            pixels = np.reshape(image, (-1, 3))

            # Run KMeans clustering on the flattened image
            kmeans = KMeans(n_clusters=num_clusters)
            kmeans.fit(pixels)

            # Reshape the cluster centers back into the original image shape
            cluster_centers = kmeans.cluster_centers_.astype('uint8')
            segmented_image = cluster_centers[kmeans.labels_]
            segmented_image = np.reshape(segmented_image, image.shape)

            # Save the segmented image to the output folder
            output_path = output_folder / f"{filename.stem}-KMeans-Segmented.png"
            cv2.imwrite(str(output_path), segmented_image)

            edges = cv2.Canny(segmented_image, 100, 200)
            output_path = output_folder / f"{filename.stem}-KMeans-Segmented-edges.png"
            cv2.imwrite(str(output_path), edges)


if __name__ == "__main__":
    main()


# # Define the source and destination paths
# folder_path_1 = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\\'
# output_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\kmeans_output\\'

# # Create the output folder if it doesn't exist
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # Define the number of clusters
# num_clusters = 8

# # Loop over each file in the source folder
# for filename in os.listdir(folder_path_1):
#     if filename.endswith('hsv.png'):
#         # Load the preprocessed image
#         image_path = os.path.join(folder_path_1, filename)
#         image = cv2.imread(image_path)

#         # Flatten the image into a 2D array of pixels
#         pixels = np.reshape(image, (-1, 3))

#         # Run KMeans clustering on the flattened image
#         kmeans = KMeans(n_clusters=num_clusters)
#         kmeans.fit(pixels)

#         # Reshape the cluster centers back into the original image shape
#         cluster_centers = kmeans.cluster_centers_.astype('uint8')
#         segmented_image = cluster_centers[kmeans.labels_]
#         segmented_image = np.reshape(segmented_image, image.shape)

#         # Save the segmented image to the output folder
#         output_path = os.path.join(output_folder, f'{filename}-KMeans-Segmented.png')
#         cv2.imwrite(output_path, segmented_image)
        
#         edges = cv2.Canny(segmented_image, 100, 200)
#         output_path = os.path.join(output_folder, f'{filename}-KMeans-Segmented-edges.png')
#         cv2.imwrite(output_path, edges)

########## older code to save 


######### This is superflous code for a kmeans clustering.

# # Define the source and destination paths
# # folder_path_1 = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\\'

# def process_images_kmeans():
#     input_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2\\'
#     output_folder = '/content/drive/MyDrive/cannabis_kmeans_1/output_images/'
#     os.makedirs(output_folder, exist_ok=True)

#     # Get a list of all the files in the input folder
#     file_list = os.listdir(input_folder)

#     for file_name in file_list:
#         # Check if the file is a PNG image
#         if file_name.endswith('.png'):
#             print(f"Processing image {file_name}")
#             file_path = os.path.join(input_folder, file_name)
#             print(f"File path: {file_path}")
#             img = io.imread(file_path)

#             if img is not None:
#                 img_flat = img.reshape(-1, 3)
#                 kmeans = KMeans(n_clusters=8)
#                 kmeans.fit(img_flat)
#                 segmented_img_flat = kmeans.cluster_centers_[kmeans.labels_].astype("uint8")
#                 segmented_img = segmented_img_flat.reshape(img.shape)
                
#                 output_path = os.path.join(output_folder, f'{file_name}-KMeans-Segmented.png')
#                 cv2.imwrite(output_path, segmented_img)
#                 print(f"Image saved at: {output_path}")
#                 print("Image processing complete")
#             else:
#                 print(f"Image could not be read for file '{file_path}'")
#         else:
#             print(f"Skipping non-PNG file '{file_name}'")

# # Call the function to process the images
# process_images_kmeans()



######### This is more superflous code for a kmeans clustering


# import os
# import cv2
# import numpy as np
# from skimage import io
# from sklearn.cluster import KMeans

# preprocessed_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2'
# save_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed_step2'


# def process_images_kmeans(recursive=False, regex_str=None):
#     os.makedirs(save_folder, exist_ok=True)
    
#     if recursive:
#         file_list = []
#         for root, dirs, files in os.walk(preprocessed_folder):
#             for file in files:
#                 if file.endswith('.jpg') or file.endswith('.png'):
#                     file_list.append(os.path.join(root, file))
#     else:
#         file_list = [os.path.join(preprocessed_folder, file) for file in os.listdir(preprocessed_folder) 
#                      if file.endswith('.jpg') or file.endswith('.png')]
    
#     for file_path in file_list:
#         if regex_str and regex_str not in file_path:
#             continue  # skip files not matching the regex string
        
#         print(f"Processing image {file_path}")
#         img = io.imread(file_path)

#         if img is not None:
#             img_flat = img.reshape(-1, 3)
#             kmeans = KMeans(n_clusters=4)
#             kmeans.fit(img_flat)
#             segmented_img_flat = kmeans.cluster_centers_[kmeans.labels_].astype("uint8")
#             segmented_img = segmented_img_flat.reshape(img.shape)
            
#             output_path = os.path.join(save_folder, f'cannabis-{os.path.basename(file_path)[:-4]}-KMeans-Segmented.png')
#             cv2.imwrite(output_path, segmented_img)
#             print(f"Image saved at: {output_path}")
#             print("Image processing complete")
#         else:
#             print(f"Image could not be read for file '{file_path}'")

#     return save_folder

# kmean_pics = process_images_kmeans(preprocessed_folder)
# show_generated_images(kmean_pics)

