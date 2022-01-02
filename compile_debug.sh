#!/bin/bash
pyinstaller --add-data settings/settings.json;settings --add-data sets/sets.json;sets --noconfirm ./meteor.py
