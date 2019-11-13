#!/bin/bash

files=$(ls test*)
for file in $files
do
cp $file testSong.wav
echo testing $file
python3 musicID.py
done

