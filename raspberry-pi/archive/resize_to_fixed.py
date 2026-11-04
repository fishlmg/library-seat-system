from PIL import Image
import os

def resize_images(source_dir, output_dir, target_size=(1024, 1024)):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get the list of all image files in the source directory
    image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    print(f"Source directory: {source_dir}")
    print(f"Output directory: {output_dir}")
    print(f"List of image files: {image_files}")

    for image_file in image_files:
        input_path = os.path.join(source_dir, image_file)
        output_path = os.path.join(output_dir, image_file)

        try:
            # Open the image file
            with Image.open(input_path) as img:
                # Resize the image
                resized_img = img.resize(target_size)

                # Save the resized image
                resized_img.save(output_path)
        except Exception as e:
            print(f"Error resizing image {image_file}: {str(e)}")

    print(f"Resizing completed. Images saved to {output_dir}.")

# Example usage:
source_directory = "D:/Library_seat _query/library/datasets(7)/images"
output_directory = 'D:/Library_seat _query/library/datasets(7)/images'
target_size = (1365,1024)

resize_images(source_directory, output_directory, target_size)
print("success")