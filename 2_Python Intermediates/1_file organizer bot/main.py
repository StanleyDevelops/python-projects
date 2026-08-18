from pathlib import Path
import shutil

folder = Path.home() / "Desktop" / "python_test" / "random_files"

# create extension mapped to folders
extension_map = {".jpeg": "Images",
                 ".png": "Images",
                 ".gif": "Images",
                 ".jpg": "Images",
                 ".zip": "Archive",
                 ".mp4": "Movies",
                 ".mp3": "Songs",
                 ".pdf": "PDFs",
                 ".py": "Codes",
                 }


# make folders
for value in extension_map.values():
    directory = folder / Path(value)
    directory.mkdir(exist_ok = True)

moved = 0
skipped = 0
    
# iterate through every files
for item in folder.iterdir():

    if not item.is_file():
        continue

    extension = item.suffix.lower()
    if extension in extension_map:
        destination =  folder / extension_map[extension]

        try: 
            shutil.move(item, destination)
            moved += 1

        except Exception as e:
             print(f"Error moving {item.name}: {e}")
             skipped += 1  
    # Empty extension           
    else:
        skipped += 1       

print(f"Files moved successfully: {moved} 🗹")
print(f"Files Skipped: {skipped}")