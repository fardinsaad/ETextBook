import os
import shutil

def select_and_save_image():
    try:
        # Step 1: Get the file path from the user
        file_path = input("Enter the full path of the image file you want to upload: ")

        # Step 2: Check if the file exists
        if not os.path.isfile(file_path):
            print("The specified file does not exist.")
            return

        # Step 3: Get the file extension and validate that it is an image
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
        file_extension = file_path.rsplit('.', 1)[-1].lower()

        if file_extension not in allowed_extensions:
            print("Invalid file type. Please provide an image file (png, jpg, jpeg, gif, bmp).")
            return

        # Step 4: Define the directory to save the image
        save_directory = "saved_images"
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Step 5: Create the save path
        file_name = os.path.basename(file_path)
        save_path = os.path.join(save_directory, file_name)

        # Step 6: Copy the image to the save directory
        shutil.copy(file_path, save_path)
        print(f"Image saved successfully to {save_path}")

    except Exception as e:
        print(f"Failed to save image: {e}")

# Example usage
if __name__ == "__main__":
    select_and_save_image()
