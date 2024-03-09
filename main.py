import os
import csv
import shutil
from random import shuffle

def split_data(csv_file, train_folder, test_folder, split_ratio=0.33):
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Read CSV file and shuffle the rows
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        shuffle(data)

    # Calculate the split index
    split_index = int(len(data) * split_ratio)

    # Split the data into train and test sets
    train_data = data[:split_index]
    test_data = data[split_index:]

    # Move images to train folder
    for row in train_data:
        image_id = row['id']
        label = row['label']
        image_path = f"{train_folder_path}/{image_id}.jpg"  # Update this path to the actual image path
        destination = os.path.join(train_folder, label, f"{image_id}.jpg")
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy(image_path, destination)

    # Move images to test folder
    for row in test_data:
        image_id = row['id']
        label = row['label']
        image_path = f"{test_folder_path}/{image_id}.jpg"
        destination = os.path.join(test_folder, label, f"{image_id}.jpg")
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy(image_path, destination)

if __name__ == "__main__":
    csv_file_path = "metadata.csv"
    train_folder_path = "train"
    test_folder_path = "test"

    split_data(csv_file_path, train_folder_path, test_folder_path)
