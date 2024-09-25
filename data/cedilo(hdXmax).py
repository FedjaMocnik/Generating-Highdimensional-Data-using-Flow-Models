import os
import json
import shutil

# Paths to the source directories and the destination directory
path_to_SD750 = '/home/fedja-mocnik/Documents/IJS/10488964/data/dataSD750'
path_to_SD1500 = '/home/fedja-mocnik/Documents/IJS/10488964/data/dataSD1500'
destination_path = '/home/fedja-mocnik/Documents/IJS/10488964/data/hdXmax'  # Destination directory

# Ensure the destination directory exists
os.makedirs(destination_path, exist_ok=True)

def najdi_and_copy(path, event):
    try:
        with open(os.path.join(path, event), "r") as file:
            jsonData = json.load(file)
        
        flag_data = jsonData.get("flags", {})
        hdXmax = flag_data.get("hdXmax", 0)
        
        if hdXmax != 0:
            print(f"Found hdXmax != 0 in {event}. Copying to {destination_path}.")
            shutil.copy(os.path.join(path, event), os.path.join(destination_path, event))
            return True
    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Error processing file {event}: {e}")
    return False

# obe mapi v en list
events = [(path_to_SD750, pos_json) for pos_json in os.listdir(path_to_SD750) if pos_json.endswith('.json')] + \
         [(path_to_SD1500, pos_json) for pos_json in os.listdir(path_to_SD1500) if pos_json.endswith('.json')]

for path, event in events:
    if najdi_and_copy(path, event):
        print(f"Copied {event} to {destination_path}")
