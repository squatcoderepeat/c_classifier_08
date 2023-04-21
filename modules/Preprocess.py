

def convert_arw_to_png(arw_folder, png_folder):
    arw_files = glob.glob(os.path.join(arw_folder, "*.ARW"))
    os.makedirs(png_folder, exist_ok=True)

    for arw_file in arw_files:
        with rawpy.imread(arw_file) as raw:
            rgb = raw.postprocess()
        png_file = os.path.join(png_folder, os.path.splitext(os.path.basename(arw_file))[0] + '.png')
        Image.fromarray(rgb).save(png_file)


arw_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!'
png_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\png/'

convert_arw_to_png(arw_folder, png_folder)

png_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\png\\'
preprocessed_folder = r'C:\Users\rober\Pictures\mar 21\purple !!!\preprocessed\\'

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

preprocess_images(png_folder, preprocessed_folder)


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
        
    return features_array00





























































.