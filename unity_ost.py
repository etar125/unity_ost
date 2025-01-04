#!/usr/bin/env python3

import os
import sys
try:
    import UnityPy
except ImportError:
    raise ImportError('Please pip install UnityPy')

def unpack(file_name : str):
    # generate file_path
    file_path = file_name
    # load that file via UnityPy.load
    env = UnityPy.load(file_path)

    # iterate over internal objects
    for obj in env.objects:
        # process specific object types
        if obj.type.name in ["AudioClip"]:
            # parse the object data
            clip = obj.read()

            # create destination path
            #dest = os.path.join(destination_folder, data.name)

            # make sure that the extension is correct
            # you probably only want to do so with images/textures
            # dest, ext = os.path.splitext(dest)
            # dest = dest + ".png"

            for name, data in clip.samples.items():
                with open("Out\\" + name, "wb") as f:
                    f.write(data)

os.makedirs("Out", exist_ok=True)
for file in sys.argv[1:]:
    print("Unpacking file \"" + file + "\"...")
    unpack(file)