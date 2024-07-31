import os
import shutil
import argparse
 
def copy_files(src_folder, dest_folder, include_ext=None, exclude_ext=None):
    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist.")
        return
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
 
    for root, _, files in os.walk(src_folder):
        for file in files:
            file_ext = os.path.splitext(file)[1]
            
            if include_ext and file_ext not in include_ext:
                continue
            if exclude_ext and file_ext in exclude_ext:
                continue
 
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_folder, os.path.relpath(src_file, src_folder))
 
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(src_file, dest_file)
            print(f"Copied '{src_file}' to '{dest_file}'")
 
def parse_arguments():
    parser = argparse.ArgumentParser(description="Copy files from one folder to another with include/exclude options.")
    parser.add_argument('src_folder', type=str, help='Source folder path')
    parser.add_argument('dest_folder', type=str, help='Destination folder path')
    parser.add_argument('--include_ext', type=str, nargs='*', help='Include files with these extensions (e.g., .txt .jpg)')
    parser.add_argument('--exclude_ext', type=str, nargs='*', help='Exclude files with these extensions (e.g., .tmp .log)')
    
    return parser.parse_args()
 
if __name__ == "__main__":
    args = parse_arguments()
    include_ext = args.include_ext if args.include_ext else []
    exclude_ext = args.exclude_ext if args.exclude_ext else []
    copy_files(args.src_folder, args.dest_folder, include_ext, exclude_ext)

    # Nikhil