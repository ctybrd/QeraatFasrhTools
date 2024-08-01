from PIL import Image, ImageDraw
import os
import shutil

# Define the base directory (relative to where the script is run or a defined base)
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive +'/'

# Define the sets of folder paths and destination folders along with their corresponding comments
folder_sets = [
    ([
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideW'),  # الأصبهاني
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideA'),  # ورش
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideJ'),  # أبو جعفر
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideB'),  # ابن كثير
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideK'),  # قالون
    ], os.path.join(drive, 'Qeraat/NewSides/side'), [
        'الأصبهاني', 'ورش', 'أبو جعفر', 'ابن كثير', 'قالون'
    ])
    ,
    ([
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideX'),  # الكسائي وخلف
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideL'),  # أصحاب التوسط
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideU'),  # أصحاب الصلة
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideS'),  # شعبة
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideI'),   # ابن عامر
    ], os.path.join(drive, 'Qeraat/NewSides/side1'), [
        'الكسائي وخلف', 'أصحاب التوسط', 'أصحاب الصلة', 'شعبة', 'ابن عامر'
    ]),
    ([
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideF'),  # خلف العاشر
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideY'),  # يعقوب
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideE'),  # الكسائي
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideM'),  # حمزة
        os.path.join(drive, 'Qeraat/NewSides/PNG/SideC'),  # أبو عمرو
    ], os.path.join(drive, 'Qeraat/NewSides/side2'), [
        'خلف العاشر', 'يعقوب', 'الكسائي', 'حمزة', 'أبو عمرو'
    ]),
]

# Function to empty folder
spacing_between_images = 10  # Adjust as needed
def empty_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

# Iterate through each set of folder paths, destination folders, and comments
for folder_paths, destination_folder, comments in folder_sets:
    try:
        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        empty_folder(destination_folder)
        # Iterate through the range of images (1.png to 522.png)
        for i in range(1, 523):
            try:
                image_paths = [os.path.join(folder, f'{i}.png') for folder in folder_paths]

                # Open the images and get the format of the first source image
                images = [Image.open(image_path) for image_path in image_paths]
                first_image_format = images[0].mode

                # Calculate the total width for the concatenated image
                total_width = sum(image.width for image in images) + (len(images) - 1) * spacing_between_images
                # Create a new blank image with the specified mode, width, and height
                concatenated_image = Image.new(first_image_format, (total_width, 1684))

                # Paste each image onto the concatenated image with vertical lines and comments
                x_offset = 0
                draw = ImageDraw.Draw(concatenated_image)

                for image, folder_path, comment in zip(images, folder_paths, comments):
                    concatenated_image.paste(image, (x_offset, 0))
                    x_offset += image.width + spacing_between_images

                    if x_offset < total_width:
                        draw.line([(x_offset, 0), (x_offset, 1684)], fill=(0, 0, 0), width=1)
                        x_offset += 1  # Space for the line

                # Save the concatenated image
                concatenated_image_path = os.path.join(destination_folder, f'{i}.png')
                concatenated_image.save(concatenated_image_path)

            except Exception as e:
                print(f"Error processing image {i}: {e}")

        print(f"Concatenation with vertical lines and comments for {destination_folder} completed.")

    except Exception as e:
        print(f"Error processing folder set: {e}")
