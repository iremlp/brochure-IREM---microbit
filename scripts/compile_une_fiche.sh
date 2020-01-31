#!/bin/sh
# commande à exécuter directement dans le dossier ./../source
# il y a un lien symbolique vers ce fichier
# 
# ~/github/brochure-IREM---microbit/source$ ./compile_une_fiche.sh ./fiche_mb-classroom.te
#
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -recorder -jobname="$1" mainShort.tex
mv "$1".pdf ./../fiches/
rm -rf ./_minted-.
rm "$1".*