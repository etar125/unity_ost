#!/usr/bin/env python3
import os
import unity_ost

if __name__=="__main__":
    os.makedirs("Out", exist_ok=True)
    for file in os.listdir():
        if file.endswith(".assets"):
            print("Unpacking file \"" + file + "\"...")
            unity_ost.unpack(file)
