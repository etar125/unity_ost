#!/bin/sh
files=()
for file in *.assets; do
    files+=("$file")
done
python3 unity_ost.py "${files[@]}"
echo "Done!"
read -n 1
