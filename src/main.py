import os
import shutil
from copy_static import copy_files_recursively
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        print(f"Deleting existing destination directory: '{dir_path_public}'")

    copy_files_recursively(dir_path_static, dir_path_public)
    print(f"Successfully copied all contents to '{dir_path_public}'.")
    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

        

main()