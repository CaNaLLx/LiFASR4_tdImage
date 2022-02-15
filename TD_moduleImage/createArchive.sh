#!/bin/bash
#
# Ce script crée automatiquement votre archive prête à être rendue et/ou à être testé par le script de correction# 
# Vous devez avoir les deux répertoires cote à cote comme ceci
#   ~/lifap4/P1234567_P1234567_P1234567
#   ~/lifap4/TD_moduleImage
#
# Ce script se lance comme ceci
#  $ cd ~/lifpa4/TD_moduleImage
#  $ ./createArchive.sh ../P1234567_P1234567_P1234567
# 
# Vous pouvez ensuite lancer le script de correction sans risquer d'écraser le répertoire de travail se trouvant à l'étage d'en dessous.
# $  ./evalModuleImage.py P1234567_P1234567_P1234567.tgz


if [ $# -ne 1 ]; then 
        echo "Nombre d'arguments non valide (ouvrez le script et regarder la doc). Usage:"
        echo "$0 chemin_vers_le_repertoire_de_travail"
        exit 0
fi

CURDIR=`pwd`
echo "current dir: ${CURDIR}"
echo "module image dir: $1"
cd $1
echo "==> run make clean in `pwd`"
make clean
/bin/rm -rf doc/html
cd ..

DIR="$(basename -- $1)"
echo "basename: ===${DIR}==="


echo "==> run tar in `pwd`"
echo "tar cfz ${DIR}.tgz --exclude=.git --exclude=.vscode ${DIR}"
tar cfz ${DIR}.tgz --exclude=.git --exclude=.vscode --exclude=.gitignore --exclude=lib ${DIR}
mv ${DIR}.tgz $CURDIR
cd $CURDIR
