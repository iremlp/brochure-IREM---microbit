#!/bin/sh
cd ./../source/
find -maxdepth 1  -name "fiche_*.tex"|while read file; do
    pdflatex --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -recorder -jobname="$file" mainShort.tex
    mv "$file".pdf ./../fiches/
    rm -rf ./_minted-.
    rm "$file".*
done
