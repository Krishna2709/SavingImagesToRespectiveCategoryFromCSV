# 1. Import required libraries
import os
import shutil
import pandas as pd

# 2. Read the csv file
df = pd.read_csv('<path_to_the_csv_file>')

# 3. Extract the different cateogries of images
folders = list(df['<column_containing_categories>'].unique())

# 4. Create empty folders of each caategory to store the images in their respective category
for i in folders:
  os.mkdir('<path_to_the_directory_to_create_empty_folders>'+i)

# 5. Extract the images from the dataframe and copy them to their respective categories.
for i in range(len(df)):
  image = os.path.join('<path_to_images_folder>', str(df.iloc[i]['<column__containing_image_id>']))
  shutil.copy(image, '<path_to_the_directory_to_create_empty_folders>'+df.iloc[i]['<column_containing_categories>'])