from PIL import Image, ImageDraw
import os

# Define the sets of folder paths and destination folders along with their corresponding comments
folder_sets = [
    ([
        r'E:/Qeraat/NewSides/PNG/SideW',  # الأصبهاني
        r'E:/Qeraat/NewSides/PNG/SideA',  # ورش
        r'E:/Qeraat/NewSides/PNG/SideJ',  # أبو جعفر
        r'E:/Qeraat/NewSides/PNG/SideB',  # ابن كثير
        r'E:/Qeraat/NewSides/PNG/SideK',  # قالون
    ], r'E:/Qeraat/NewSides/side', [
        'الأصبهاني', 'ورش', 'أبو جعفر', 'ابن كثير', 'قالون'
    ])
    ,
    ([
        r'E:/Qeraat/NewSides/PNG/SideX',  # الكسائي وخلف
        r'E:/Qeraat/NewSides/PNG/SideL',  # أصحاب التوسط
        r'E:/Qeraat/NewSides/PNG/SideU',  # أصحاب الصلة
        r'E:/Qeraat/NewSides/PNG/SideS',  # شعبة
        r'E:/Qeraat/NewSides/PNG/SideI',   # ابن عامر
    ], r'E:/Qeraat/NewSides/side1', [
        'الكسائي وخلف', 'أصحاب التوسط', 'أصحاب الصلة', 'شعبة', 'ابن عامر'
    ]),
    ([
        r'E:/Qeraat/NewSides/PNG/SideF',  # خلف العاشر
        r'E:/Qeraat/NewSides/PNG/SideY',  # يعقوب
        r'E:/Qeraat/NewSides/PNG/SideE',  # الكسائي
        r'E:/Qeraat/NewSides/PNG/SideM',  # حمزة
        r'E:/Qeraat/NewSides/PNG/SideC',  # أبو عمرو
    ], r'E:/Qeraat/NewSides/side2', [
        'خلف العاشر', 'يعقوب', 'الكسائي', 'حمزة', 'أبو عمرو'
    ]),
]

spacing_between_images = 10  # Adjust as needed

# Iterate through each set of folder paths, destination folders, and comments
# ...
for folder_paths, destination_folder, comments in folder_sets:
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through the range of images (1.png to 522.png)
    for i in range(1, 523):
        image_paths = [os.path.join(folder, f'{i}.png') for folder in folder_paths]

        # Open the images and get the format of the first source image
        images = [Image.open(image_path) for image_path in image_paths]
        first_image_format = images[0].mode

        # Calculate the total width for the concatenated image
        total_width = sum(image.width for image in images) + (len(images) - 1) * spacing_between_images
        # Create a new blank image with the specified mode, width, and height
        concatenated_image = Image.new(first_image_format, (total_width, 2407))

        # Paste each image onto the concatenated image with vertical lines and comments
        x_offset = 0
        draw = ImageDraw.Draw(concatenated_image)

        for image, folder_path, comment in zip(images, folder_paths, comments):
            concatenated_image.paste(image, (x_offset, 0))
            x_offset += image.width + spacing_between_images

            if x_offset < total_width:
                draw.line([(x_offset, 0), (x_offset, 2406)], fill=(0, 0, 0), width=1)
                x_offset += 1  # Space for the line

        # Save the concatenated image
        concatenated_image_path = os.path.join(destination_folder, f'{i}.png')
        concatenated_image.save(concatenated_image_path)

    print(f"Concatenation with vertical lines and comments for {destination_folder} completed.")