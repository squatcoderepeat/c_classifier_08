def analyze_plant_health(image_path, num_clusters=8):
    segmented_img = cv2.imread(image_path)
    color_percentages = {}

    if segmented_img is not None:
        unique_colors, percentages = get_color_percentages(segmented_img, num_clusters)  # Change function name

        for color, percentage in zip(unique_colors, percentages):
            for lower_range, upper_range, color_name in color_ranges:
                if (color >= lower_range).all() and (color <= upper_range).all():
                    color_category = color_name
                    break
            else:
                color_category = 'Other'

            color_percentages[color_category] = percentage

    else:
        print(f"Image could not be read for file '{image_path}'")

    return color_percentages

# Example usage
folder_path =  #'/content/drive/MyDrive/cannabis_kmeans_1/output_images/'
image_color_percentages = process_all_images(folder_path, num_clusters=4)

# Convert the list of dictionaries to a NumPy array
color_names = [color_info[2] for color_info in color_ranges]
color_names.append('Other')

array_data = np.zeros((len(image_color_percentages), len(color_names)))

for i, color_percentages in enumerate(image_color_percentages):
    for j, color_name in enumerate(color_names):
        array_data[i, j] = color_percentages.get(color_name, 0)

print("Color percentages array:")
print(array_data)


# More of the above, here we are setting thresholds for the specific colors and giving the user a response in case we think there is actually an issue. 

# Color percentages array:
# <pre>[[16.0990991   0.          0.          0.         23.47567568]
#  [ 5.91111111  0.          0.          0.         34.35915916]
#  [19.67507508  0.          0.          0.         43.13873874]
#  [ 0.94774775  0.          0.          0.         27.18978979]
#  [29.81981982  0.          0.          0.         18.38258258]
#  [34.12192192  0.         20.53453453  0.          9.57237237]
#  [10.53633634  0.          0.          0.         29.86666667]
#  [33.03843844  0.          0.          0.         11.92372372]
#  [25.22462462  0.         24.49009009  0.         10.14234234]
#  [24.46486486  0.         35.45345345  0.         14.42282282]
#  [21.77177177  0.         23.9957958   0.         40.46306306]
#  [35.25465465  0.          0.          0.          7.98498498]
#  [25.34114114  0.         34.15255255  0.         20.16576577]
#  [16.65405405  0.          0.          0.         19.3975976 ]
#  [36.68408408  0.          0.         21.26426426 10.3981982 ]
#  [29.95675676  0.          0.         20.91351351 25.53513514]
#  [42.37057057  0.          0.          0.         18.71711712]
#  [16.85165165  0.          0.          0.         43.42882883]
#  [28.84564565  0.          0.          0.         11.18018018]
#  [ 0.          0.          0.          0.         30.10690691]
#  [18.14594595  0.          0.          0.         12.83963964]
#  [ 8.87747748  0.          0.          0.         16.33813814]
#  [ 8.66786787  0.         12.12552553  0.         46.37777778]
#  [10.95375375  0.          0.          0.          3.66846847]
#  [11.74714715  0.          0.          0.         38.93993994]
#  [ 6.53873874  0.          0.          0.          8.57717718]
#  [12.53333333  0.         13.72312312  0.          5.92012012]
#  [36.92912913  0.          0.          0.         17.32552553]
#  [19.79099099  0.          0.          0.         23.98258258]
#  [39.64864865  0.          0.          0.         11.5015015 ]
#  [ 4.25105105  0.          0.          0.         23.95015015]
#  [10.04144144  0.          0.          0.          4.93813814]
#  [33.16996997  0.          0.          0.         12.27687688]
#  [27.45885886  0.          0.          0.         50.72852853]
#  [ 9.98558559  0.         14.11351351  0.          9.91711712]
#  [10.56876877  0.         12.82162162  0.          2.81741742]
#  [23.60660661  0.          0.          0.          8.27567568]
#  [23.7975976   0.          0.          0.          6.02942943]
#  [ 8.22342342  0.          0.          0.          7.67867868]
#  [12.30870871  0.          0.          0.         12.61201201]
#  [13.17117117  0.          0.          0.         27.4972973 ]
#  [33.21861862  0.          0.          0.         19.32192192]
#  [21.92252252  0.          0.          0.          0.60840841]
#  [19.16216216  0.          0.          0.          0.56396396]
#  [10.65105105  0.          0.          0.         12.8012012 ]
#  [ 3.72372372  0.         16.94354354  0.         22.35135135]
#  [ 9.53753754  0.          0.          0.         58.26006006]
#  [ 0.          0.          0.          0.         13.66786787]
#  [ 0.          0.          0.          0.          5.38198198]
#  [25.5957958   0.          0.          0.          6.07687688]
#  [41.64564565  0.          0.          0.         10.25345345]
#  [23.5027027   0.          0.          0.         14.75195195]
#  [30.34114114  0.          0.          0.          9.52312312]
#  [29.77657658  0.         27.6996997   0.         13.41921922]
#  [19.91951952  0.         26.47747748  0.         36.44744745]
#  [28.16036036  0.          0.          0.          5.16816817]
#  [36.50690691  0.          0.          0.          2.71171171]
#  [24.78798799  0.          0.          0.         29.38498498]
#  [32.67207207  0.          0.          0.         21.16216216]
#  [26.34894895  0.         37.90750751  0.         14.81741742]
#  [24.43183183  0.          0.          0.          6.41501502]
#  [18.37357357  0.         10.15135135  0.         22.3039039 ]
#  [17.41381381  0.         10.003003    0.         50.90810811]
#  [ 0.          0.          5.42522523  0.         31.6978979 ]
#  [ 0.         28.66126126  4.81501502  0.         33.38318318]
#  [ 0.         22.15915916  0.          0.         38.72552553]
#  [ 0.          0.          8.06906907  0.         18.21981982]
#  [ 0.          0.         11.72072072  0.         13.95615616]
#  [ 0.         11.35855856  0.          0.          6.03723724]
#  [ 0.          0.          0.          0.          9.95495495]
#  [ 0.          8.93333333  0.          0.         10.50930931]
#  [ 0.          0.          0.          0.         42.71291291]
#  [ 0.          0.          0.          0.         42.43423423]
#  [ 0.          0.          0.          0.         24.3957958 ]
#  [ 0.          0.         12.36276276  0.         29.57057057]
#  [ 0.          0.          0.          0.         22.19039039]
#  [ 0.          0.          0.          0.         52.76276276]
#  [ 0.          0.          0.          0.         13.0966967 ]
#  [24.48468468  0.          0.          0.         13.81381381]
#  [21.9963964   0.          0.          0.         22.95255255]
#  [25.91891892  0.          0.          0.         11.13393393]
#  [31.1987988   0.          0.          0.         18.88108108]
#  [30.03723724  0.          0.          0.          6.69069069]
#  [27.66666667  0.          0.          0.         11.51651652]
#  [ 0.          0.          0.          0.          7.63123123]
#  [ 0.          0.          0.          0.         18.72492492]
#  [21.28048048  0.          0.          0.          4.31891892]
#  [18.72192192  0.         27.46426426  0.         28.56396396]
#  [ 0.          0.          0.          0.          6.95015015]
#  [13.83963964  0.          0.          0.          9.90990991]
#  [ 0.          0.          0.          0.         29.14114114]
#  [52.78647687  0.          0.          0.          3.47900356]
#  [11.30533808  0.          0.          0.         14.5202847 ]
#  [11.21209964  0.          0.          0.         10.77935943]
#  [16.17651246  0.          6.17010676  0.         55.63914591]
#  [10.7088968   0.          0.          0.         15.37793594]
#  [ 8.8975089   0.          0.          0.         14.72170819]
#  [ 9.16939502  0.          0.          0.         25.14163701]
#  [11.83914591  0.          0.          0.         12.70462633]
#  [11.9886121   0.          0.          0.         16.95587189]
#  [12.81921708  0.          0.          0.          5.49537367]
#  [59.59857651  0.          0.          0.         14.83487544]
#  [21.45124555  0.          0.          0.          3.6341637 ]
#  [22.96298932  0.         38.97864769  0.         21.89395018]
#  [11.98007117  0.          0.          0.         18.19715302]
#  [11.95160142  0.          7.27615658  0.         54.54092527]
#  [ 7.70676157  0.          8.97580071  0.         47.13736655]
#  [15.35231317  0.          0.          0.         28.28896797]
#  [ 7.62562278  0.          0.          0.         27.12740214]
#  [ 2.82135231  0.          0.          0.         19.60782918]
#  [ 3.87829181  0.          0.          0.         61.45338078]
#  [ 9.53309609  0.          0.          0.         15.99857651]
#  [11.22633452  0.          0.          0.         20.39928826]
#  [ 0.          0.         18.08042705  0.         34.20213523]
#  [ 9.06263345  0.          0.          8.78007117  3.30604982]
#  [ 0.          0.          9.20569395  0.          2.60925267]
#  [ 9.7024911   0.          0.          0.         61.0341637 ]
#  [ 0.          0.         10.88683274  0.         10.95017794]
#  [ 6.35587189  0.         10.90533808  0.          2.89466192]
#  [ 6.82348754  0.          6.67544484  0.          2.27188612]
#  [ 9.6341637   0.          0.          0.         13.38434164]
#  [ 3.49252669  0.          1.47330961  0.         53.78932384]
#  [ 3.60498221  0.          1.67117438  0.         57.7772242 ]
#  [ 2.78362989  0.          0.          0.         25.99786477]
#  [ 6.64982206  0.          0.          0.          0.62562278]
#  [ 7.57508897  0.          0.          0.          0.5202847 ]
#  [21.52811388  0.          0.          0.          2.85124555]
#  [21.58647687  0.          0.          0.         27.94021352]
#  [ 0.          0.          0.          0.          3.08398577]
#  [ 0.          0.          0.          0.          3.16085409]
#  [16.713879    0.          0.          0.          0.58362989]
#  [16.99786477  0.          0.          0.          8.81850534]
#  [17.03843416  0.          0.          0.         10.89323843]
#  [16.80071174  0.          0.          0.          9.25053381]
#  [13.28540925  0.          0.          0.         25.97153025]
#  [ 5.31174377  0.          0.          0.         16.02775801]
#  [ 8.06548043  0.          0.          0.          9.23772242]
#  [ 7.32384342  0.          0.          0.          7.50320285]]</pre>




# Define threshold values for color ranges (in percentages)
thresholds = {
    'yellow': 10,
    'brown': 5,
    'purple': 5
}

# Define a function to check the health of the plant
def is_plant_healthy(color_percentages, thresholds):
    problems = []

    if color_percentages[1] > thresholds['yellow']:
        problems.append('Yellowing leaves (possible nutrient deficiency)')

    if color_percentages[2] > thresholds['brown']:
        problems.append('Browning leaves (possible nutrient burn or over-watering)')

    if color_percentages[3] > thresholds['purple']:
        problems.append('Purpling leaves (possible phosphorus deficiency or cold stress)')

    return problems

# Iterate through the images and check if the plant is healthy or not
for idx, color_percentages in enumerate(array_data):
    problems = is_plant_healthy(color_percentages, thresholds)
    if problems:
        print(f"Image index {idx} has the following problems:")
        for problem in problems:
            print(f"  - {problem}")
    else:
        print(f"Image index {idx} appears to be healthy.")



# ideally i need to add the unhealthy ones in here automaticall
unhealthy_indices = [
    5, 8, 9, 10, 12, 14, 15, 22, 26, 34, 35, 45, 53, 54, 59, 61, 62,
    63, 64, 65, 66, 67, 68, 74, 87, 94, 103, 105, 106, 113, 114, 115,
    117, 118, 119
]

def show_unhealthy_images(folder_path, unhealthy_indices):
    plt.figure(figsize=(20, 20))
    for i, index in enumerate(unhealthy_indices, start=1):
        img_path = os.path.join(folder_path, f'cannabis-{index + 10}.png')
        img = Image.open(img_path)
        plt.subplot(6, 6, i)
        plt.imshow(img)
        plt.axis('off')
        plt.title(f'Image index {index}')

    plt.tight_layout()
    plt.show()

show_unhealthy_images(folder_path, unhealthy_indices)