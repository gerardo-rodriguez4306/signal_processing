#!/bin/bash

files=$(ls *csv)
for file in $files
do
cp $file tones.csv
echo testing $file
python3 dtmf.py
done

