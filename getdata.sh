#!/usr/bin/env bash

filename=$(echo "/Users/italo/Personal/Dropbox/Aplicaciones/Nudget/$(ls -1t ~/Personal/Dropbox/Aplicaciones/Nudget/ | head -1)")

abspath="$filename"

cat "$abspath" > data.csv
