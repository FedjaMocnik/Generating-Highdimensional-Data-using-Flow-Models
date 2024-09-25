import os
import json


source_path = '/home/fedja-mocnik/Documents/IJS/10488964/data/hdXmax'

events = [pos_json for pos_json in os.listdir(source_path) if pos_json.endswith('.json')]

# sdrec
energy = []
theta = []
phi = []
n19 = []
n68 = []
l = []
b = []
ra = []
dec = []

#fdrec
totalEnergy = []
calEnergy = []
xmax = []
heightXmax = []
distXmax = []
dEdXmax = []

for event in events:
    try:
        with open(os.path.join(source_path, event), "r") as file:
            jsonData = json.load(file)
        
        # Extract from sdrec, if present
        sdrec_data = jsonData.get("sdrec", {})
        if sdrec_data:
            energy.append(sdrec_data.get("energy", None))
            theta.append(sdrec_data.get("theta", None))
            phi.append(sdrec_data.get("phi", None))
            n19.append(sdrec_data.get("n19", None))
            n68.append(sdrec_data.get("n68", None))
            l.append(sdrec_data.get("l", None))
            b.append(sdrec_data.get("b", None))
            ra.append(sdrec_data.get("ra", None))
            dec.append(sdrec_data.get("dec", None))
        
        # Extract from fdrec, if present
        fdrec_data = jsonData.get("fdrec", [])
        if fdrec_data:
            for fd in fdrec_data:
                totalEnergy.append(fd.get("totalEnergy", None))
                calEnergy.append(fd.get("calEnergy", None))
                xmax.append(fd.get("xmax", None))
                heightXmax.append(fd.get("heightXmax", None))
                distXmax.append(fd.get("distXmax", None))
                dEdXmax.append(fd.get("dEdXmax", None))
    
    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Error processing file {event}: {e}")


data_parsed = {
    "sdrec": {
        "energy": energy,
        "theta": theta,
        "phi": phi,
        #"n19": n19, kva tega ni!
        #"n68": n68,
        "l": l,
        "b": b,
        "ra": ra,
        "dec": dec
    },
    "fdrec": {
        "totalEnergy": totalEnergy,
        "calEnergy": calEnergy,
        "xmax": xmax,
        "heightXmax": heightXmax,
        "distXmax": distXmax,
        "dEdXmax": dEdXmax
    }
}

# Save the extracted data to a new JSON file
with open('data_parsed.json', 'w') as json_file:
    json.dump(data_parsed, json_file, indent=4)

print("Data has been successfully extracted and saved to data_parsed.json")
