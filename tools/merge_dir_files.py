import sys
import os
import shutil

def main():
    if not len(sys.argv) == 4:
        exit(1)

    for dir_path in sys.argv[1:3]:
        if not os.path.isdir(dir_path):
            exit(1)

    if os.path.exists(sys.argv[3]):
        if os.path.isfile(sys.argv[3]):
            exit(1)

        shutil.rmtree(sys.argv[3])

    os.mkdir(sys.argv[3])
    merged_files = []

    # scan modified folder, append contents to vanilla file
    print("merging files")

    for file_name in os.listdir(sys.argv[2]):
        # build paths
        vanilla_path = os.path.join(sys.argv[1], file_name)
        modified_path = os.path.join(sys.argv[2], file_name)
        merged_path = os.path.join(sys.argv[3], file_name)
        
        # open files
        modified_src = open(modified_path, "r")
        try:
            vanilla_src = open(vanilla_path, "r")
        except IOError:
            vanilla_src = None
        dst = open(merged_path, "w")
        
        # copy data
        if vanilla_src:
            dst.writelines(vanilla_src.readlines())
            dst.write("\n")
            dst.write("\n")
        dst.writelines(modified_src.readlines())
        dst.close()
        
        merged_files.append(file_name.lower())

    # copy nonmerged files
    print("copying vanilla files")

    for file_name in os.listdir(sys.argv[1]):
        if file_name.lower() in merged_files:
            continue
        
        vanilla_path = os.path.join(sys.argv[1], file_name)
        merged_path = os.path.join(sys.argv[3], file_name)
        
        src = open(vanilla_path, "r")
        dst = open(merged_path, "w")
        
        dst.writelines(src.readlines())
        dst.close()
        src.close()

if __name__ == "__main__":
    """
        Usage: merge_dir_files.py dirpath_vanilla dirpath_modified dirpath_merged
        dirpath_vanilla must exist
        dirpath_modified must exist
        dirpath_merged can exist, but does not have to
    """
    main()