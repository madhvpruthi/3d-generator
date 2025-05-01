import os
from PIL import Image
from rembg import remove
import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection 
def process_image_to_3d(image_path):
    try: 
        image = Image.open(image_path)
        image_no_bg = remove(image)
        bg_removed_path = os.path.join("output", "no_bg.png")
        image_no_bg.save(bg_removed_path)
        print(f"Background removed image saved to: {bg_removed_path}")
 
        img_data = np.array(image_no_bg.convert("L")) 
 
        heightmap = img_data / 255.0  
 
        x, y = np.meshgrid(np.linspace(0, 1, img_data.shape[1]), np.linspace(0, 1, img_data.shape[0]))
        z = heightmap 
        vertices = np.column_stack((x.flatten(), y.flatten(), z.flatten()))
 
        faces = []
        for i in range(img_data.shape[0] - 1):
            for j in range(img_data.shape[1] - 1):
                p1 = i * img_data.shape[1] + j
                p2 = i * img_data.shape[1] + j + 1
                p3 = (i + 1) * img_data.shape[1] + j
                p4 = (i + 1) * img_data.shape[1] + j + 1
                faces.append([p1, p2, p3])
                faces.append([p3, p2, p4])
        faces = np.array(faces) 
        mesh = trimesh.Trimesh(vertices=vertices, faces=faces) 
        output_path = os.path.join("output", "image_model.obj")
        mesh.export(output_path)
        return output_path
    except Exception as e:
        print(f"Error in process_image_to_3d: {e}")
        raise

def process_text_to_3d(prompt):
    try:
        print(f"Generating 3D model for prompt: {prompt}")
        if "box" in prompt or "cube" in prompt:
            mesh = trimesh.creation.box(extents=(1, 1, 1)) 
        elif "sphere" in prompt:
            mesh = trimesh.creation.icosphere(subdivisions=3, radius=1)
        elif "cylinder" in prompt:
            mesh = trimesh.creation.cylinder(radius=1, height=2)
        elif "cone" in prompt:
            mesh = trimesh.creation.cone(radius=1, height=2)
        elif "tetrahedron" in prompt or "triangle" in prompt:
            mesh = trimesh.creation.icosphere(subdivisions=0, radius=1)
        elif "rectangle" in prompt:
            mesh = trimesh.creation.box(extents=(2, 1, 0.5))
        else:
            print("Shape not recognized. Generating default box.")
            mesh = trimesh.creation.box(extents=(1, 1, 1))
        mesh.apply_translation(-mesh.centroid)
        scale = 1.0 / max(mesh.extents)
        mesh.apply_scale(scale) 
        output_path = f"output/{prompt}_model.obj"
        mesh.export(output_path) 
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(f"3D Model: {prompt.capitalize()}") 
        ax.add_collection3d(Poly3DCollection(mesh.triangles, facecolor='skyblue', edgecolor='k', alpha=0.9))

        # Auto scale axes
        scale = mesh.vertices.flatten()
        ax.auto_scale_xyz(scale, scale, scale)

        plt.tight_layout()
        plt.show()

        return output_path

    except Exception as e:
        print(f"Error in process_text_to_3d: {e}")
        raise

def main():
    print("3D Project ")
    choice = input("Enter input type (image/text): ").strip().lower()
 
    if not os.path.exists("output"):
        os.makedirs("output")

    if choice == "image":
        image_path = input("Enter path to image (JPG/PNG): ").strip()
        if os.path.exists(image_path):
            try:
                output_file = process_image_to_3d(image_path)
                print(f"3D model saved to: {output_file}")
            except Exception as e:
                print(f"Error processing image: {e}")
        else:
            print("Image file not found.")

    elif choice == "text":
        prompt = input("Enter a text prompt: ").strip()
        try:
            output_file = process_text_to_3d(prompt)
            print(f"3D model saved to: {output_file}")
        except Exception as e:
            print(f"Error generating model : {e}")
    else:
        print("Invalid choice..")

if __name__ == "__main__":
    main()
