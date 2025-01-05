#!/usr/bin/env python3

import os
import sys
try:
    import UnityPy
except ImportError:
    raise ImportError('Please pip install UnityPy')

def unpack(file_name : str):
    file_path = file_name
    env = UnityPy.load(file_path)
    for obj in env.objects:
        if obj.type.name in ["AudioClip"]:
            clip = obj.read()
            for name, data in clip.samples.items():
                with open(os.path.join("Out", name), "wb") as f:
                    f.write(data)

if __name__=="__main__":
    os.makedirs("Out", exist_ok=True)
    for file in sys.argv[1:]:
        print("Unpacking file \"" + file + "\"...")
        unpack(file)
