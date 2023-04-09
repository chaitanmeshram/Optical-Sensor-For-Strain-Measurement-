import os
import matplotlib.pyplot as plt
import pandas as pd

'''
taking initial image input of folder containing initiL image to measure
initial length of rod in terms of pixels
'''

initial_image_path = "Initial folder"

# Get a list of all the image filenames in the folder

ini_im = os.listdir(initial_image_path)

#initializing initial length of rod as 0

d = 0

# Load the image using matplotlib

ini_path = os.path.join(initial_image_path, ini_im)

im = plt.imread(ini_path)

# Display the image and ask the user to select two points

fig, ax = plt.subplot()
ax.imshow(im)


poi1 = plt.ginput(1)[0]
poi2 = plt.ginput(1)[0]
plt.close()

#measuring rod length using distance formula
d = ((poi2[0]-poi1[0])**2 +(poi2[1] - poi1[1]**2))**0.5

#measuring strains by looping through images

# Define the folder path where the images are stored
folder_path = "folder path"

# Get a list of all the image filenames in the folder
image_files = os.listdir(folder_path)

# Create an empty list to store the data
data = []

# Loop through each image in the folder
for image_file in image_files:
    # Load the image using matplotlib
    image_path = os.path.join(folder_path, image_file)
    image = plt.imread(image_path)

    # Display the image and ask the user to select two points
    fig, ax = plt.subplots()
    ax.imshow(image)
    point1 = plt.ginput(1)[0]
    point2 = plt.ginput(1)[0]
    plt.close()

    # Calculate the distance between the points
    distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
    strain = distance*d
    # Append the filename and distance to the data list
    data.append([image_file, strain])

# Create a Pandas DataFrame from the data list
df = pd.DataFrame(data, columns=["Filename", "Strain"])

# Export the DataFrame to an Excel file
output_path = os.path.join(folder_path, "strains.xlsx")
df.to_excel(output_path, index=False)

# Open the Excel file
os.startfile(output_path)