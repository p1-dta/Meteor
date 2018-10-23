#!/bin/bash
rm -rf ./dist
rm -rf ./build
pyinstaller -w ./chi_train.py
cp sets.json ./dist/chi_train/
