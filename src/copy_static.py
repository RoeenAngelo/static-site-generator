import shutil
import os

def copy_files_recursively(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    
    for filename in os.listdir(src_dir):
        from_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        print(f" * source: {from_path} -> destination: {dest_path}")

        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursively(from_path, dest_path)



