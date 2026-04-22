import zipfile
import os

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zpfile:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root,file)
                rel_path = os.path.relpath(full_path, os.path.dirname(folder_path))
                zpfile.write(full_path, rel_path)

if __name__ == '__main__':
    folder_path = input("Enter file path: ")
    output_fname = input("Enter the output file path: ")

    zip_folder(folder_path, output_fname)
    

    print(f"Successfully Created {output_fname}")