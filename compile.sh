#!/bin/bash
pyinstaller -w --add-data "settings/settings.json;settings" --add-data "sets/sets.json;sets" --noconfirm ./meteor.py
