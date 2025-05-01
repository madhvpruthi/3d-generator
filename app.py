import os
from utils import process_image_to_3d, process_text_to_3d

def main():
    print("3D Project")
    choice = input("Enter input type (image/text): ").strip().lower()

    # Ensure output folder exists
    if not os.path.exists("output"):
        os.makedirs("output")

    if choice == "image":
        image_path = input("Enter path to image (JPG/PNG): ").strip()
        if os.path.exists(image_path):
            try:
                output_file = process_image_to_3d(image_path)
                print(f"3D model saved to: {output_file}")
                # The visualization is handled in the process_image_to_3d function (if implemented)
            except Exception as e:
                print(f"Error processing image: {e}")
        else:
            print("Image file not found.")

    elif choice == "text":
        prompt = input("Enter a text prompt: ").strip()
        try:
            output_file = process_text_to_3d(prompt)
            print(f"3D model saved to: {output_file}")
            # The visualization is handled in the process_text_to_3d function
        except Exception as e:
            print(f"Error generating model {e}")
    else:
        print("Invalid choice..")

if __name__ == "__main__":
    main()
