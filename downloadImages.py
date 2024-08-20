import os
import requests

# Define the directory where you want to save the images
save_directory = "D:/Sahab10"  # Change this to your desired directory

# Ensure the directory exists
os.makedirs(save_directory, exist_ok=True)

# Loop through the range of page numbers and download each image
for i in range(1, 604):  # 1 to 603 inclusive
    url = f"https://tafsir.app/scans/m-sahabah/{i}.jpg"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Save the image
        with open(os.path.join(save_directory, f"{i}.jpg"), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded page {i}.jpg")
    else:
        print(f"Failed to download page {i}.jpg, status code: {response.status_code}")
