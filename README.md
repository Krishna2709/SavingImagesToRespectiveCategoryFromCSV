# SavingImagesToRespectiveCategoryFromCSV
Saving the images from train directory to respective categories from a CSV file! <br>

If you have a dataset containing images and a csv file which label those images to their respective labels,
<br>
train_images.csv contain two labels/categories

> dataset:
  - train_images
  - train_images.csv <br>
  
you can store them to their respective folders as follows

> dataset:
  - train_images
    - category_1
    - category_2
    
## Required Libraries
1. Pandas - to read the csv file 
2. os - to load the directory path 
3. shutil - to copy the images from train_images to their respective folders.
