import os
import shutil

# Display folders, subfolders and filenames
for folderName, subfolders, filenames in os.walk("/home/rohith"):
    print("The folder is " + folderName)
    print("The subfolders in " + folderName + " are: " + str(subfolders))
    print("The filenames in " + folderName + " are: " + str(filenames))
    print()

    # Remove folders with the name fish
    for subfolder in subfolders:
        print("Actually in subfolder: " + subfolder)
        if "fish" in subfolder:
            # os.rmdir(os.path.join(folderName, subfolder))
            print("Folder: " + folderName)
            print(subfolder + " removed!")

    # Copy all *.rxt files in recursive mode
    for file in filenames:
        if file.endswith(".rxt"):
            shutil.copy(
                os.path.join(folderName, file),
                os.path.join(folderName, file + ".backup"),
            )
