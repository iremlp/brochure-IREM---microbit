#!/bin/sh
# changement : utiliser le script directement dans le dossier source
# j'y ai mis un lien symbolique. Commande à exécuter :
#
#  ~/github/brochure-IREM---microbit/source$ ./compile_toutes_les_fiches.sh
#
find -maxdepth 1  -name "fiche_*.tex"|while read file; do
    pdflatex --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -recorder -jobname="$file" mainShort_script.tex
    mv "$file".pdf ./../fiches/
    rm -rf ./_minted-.
    rm "$file".*
done