#!/usr/bin/python3
import os
import glob
import os
import shutil
import sys
from sys import platform
import tarfile
import subprocess
import glob
import re
import csv
from zipfile import ZipFile 
import shutil




###          FONCTIONNALITES            ###
def msg(pb, sep='', end='\n'):
    print(pb, sep=sep, end=end)


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def isdir(thefile):
    return os.path.isdir(thefile)

def isfile(thefile):
    return os.path.isfile(thefile)



def identification_etudiants(FILENAME, VERBOSE=False):
    ### IDENTIFICATION DES ETUDIANTS ET NOM D'ARCHIVE - PRISE EN COMPTE QUE L'ARCHIVE PEUT PROVENIR DE TOMUSS ###
    if VERBOSE:
        msg("FILENAME = " + FILENAME)
    NUMEROS_ETU = []
    NOM_ARCHIVE_ATTENDU = ""

    replaceP = {"p": "1", "P": "1"}
    FILENAME_P_REPLACED = replace_all(FILENAME, replaceP)
    for mot in FILENAME_P_REPLACED.split(".")[0].split("_"):
        if mot.isdigit() and len(mot) == 8:
            NUMEROS_ETU.append(mot)
            if len(NUMEROS_ETU) > 1:
                NOM_ARCHIVE_ATTENDU += "_"
            NOM_ARCHIVE_ATTENDU += mot

    if len(NUMEROS_ETU) == 0:
        msg("ERREUR : aucun numero d'etudiant detecte dans: " + FILENAME)
        return ""
    if not FILENAME_P_REPLACED.split(".")[0].endswith(NOM_ARCHIVE_ATTENDU):
        msg("L'archive  " + FILENAME + "  ne suit pas le format NUM_ETU1_NUM_ETU2_NUM_ETU3.tgz")
    f = FILENAME
    if "#" in f:
        f = f.split("#")[1]
    NOM_ARCHIVE = f[f.find(NUMEROS_ETU[0][1:]) - 1] + NUMEROS_ETU[0][1:] + f.split(".")[0].split(NUMEROS_ETU[0][1:])[1]
    txtNUM_ETU = "_".join(NUMEROS_ETU)
    if VERBOSE:
        msg("NOM_ARCHIVE = " + NOM_ARCHIVE)
        msg("Numeros des etudiants =", end=' ')
        msg(txtNUM_ETU, end='\n')
    return txtNUM_ETU


def extraction_archive(FILENAME, VERBOSE=False):
    ###  EXTRACTION DE L'ARCHIVE  ###
    if VERBOSE:
        msg("===> decompression de l'archive ...")
    try:
        tar = tarfile.open(FILENAME)
    except:
        print("File {} is corrupt".format(FILENAME))
        return ""
    # DIR = tar.members[0].name.split("/")[0]
    DIR = "aucun_dossier"
    try:
        for tarmember in tar:
            if tarmember.isdir() and '/' not in tarmember.name:
                DIR = tarmember.name
    except:
        print("File {} is corrupt".format(FILENAME))
        return ""
    
    if DIR == "aucun_dossier":
        msg("Aucun dossier a la racine de l'archive")
        if isdir(DIR):
            shutil.rmtree(DIR, ignore_errors=True)
        os.mkdir(DIR)
    if VERBOSE:
        msg("Repertoire principal = " + DIR)
    try:
        tar.extractall()
    except:
        print("File {} is corrupt".format(FILENAME))
        return ""
    tar.close()
    if VERBOSE:
        msg("===> decompression de l'archive ... done")
    return DIR



def verif_arborescence(DIR):
    ###  VERIFICATION DE L'ARBORESCENCE  ###
    msg("===> verification de l'arborescence ...")
    if not isdir(DIR) or DIR == ".":
        msg("ERREUR : Repertoire principal inexistant")
        sys.exit(0)
    os.chdir(os.getcwd() + "/" + DIR)
    if not isdir("bin"):
        msg("Dossier bin inexistant", 0.5)
    if not isdir("src"):
        msg("Dossier src inexistant", 0.5)
    if not isdir("doc"):
        msg("Dossier doc inexistant", 0.5)
    if not isdir("data"):
        msg("Dossier data inexistant", 0.5)
    msg("===> verification de l'arborescence ... done")
    if VERBOSE:
        msg("==> note = " + str(NOTE))



def students_list(dir):
    l = []
    files = glob.glob(dir+"/*.*")
    for f in files:
        if f.find(".tar.gz") != -1 or f.find(".tgz") != -1 or f.find(".tar") != -1 or f.find(".zip") != -1:
            l.append(f)
    return l



def extract_all_students(dir, plagiat_dir, year):
    pwd = os.getcwd()
    os.chdir(dir)
    archives = students_list(".")
    print("Execution du script pour "+str(len(archives))+" archives.\n")
    for file in archives:
        msg("____________________")
        msg("*** file: "+file)
        file_short = file.split("/")[-1]
        students = identification_etudiants(file_short)
        if students != "":
            filename_out = plagiat_dir + "/" + year + "__" + students + ".txt"
            dir_student = extraction_archive(file)
            if dir_student=="":
                continue
            print("extract data: "+dir_student + " ==> "+ filename_out)

            data_files =    [ 
                                ["src/pixel.h", "src/Pixel.h"],
                                ["src/pixel.cpp", "src/Pixel.cpp"],
                                ["src/image.h", "src/Image.h"],
                                ["src/image.cpp", "src/Image.cpp"],
                                ["readme.txt", "Readme.txt", "README.txt", "readme.md", "Readme.md", "README.md"],
                                ["Makefile", "makefile"],
                            ]
            data = ""
            for fs in data_files:
                for f in fs: 
                    f = dir_student + "/" + f
                    #msg("test file: "+f)
                    if isfile(f):
                        with open(f, 'r', encoding="latin-1") as fp: 
                            dataf = fp.read()
                            data += dataf
                            msg("add: "+f)
                        break
                    #data += "\n=======================================================================================================\n"
            
            with open (filename_out, encoding='latin-1', mode='w', newline='\n') as fp: 
                fp.write(data)
            msg("save: "+filename_out + "     length="+str(len(data)))

            print("rm -rf "+dir_student)
            if dir_student != ".":
                shutil.rmtree( dir_student )
    os.chdir(pwd)



if __name__ == '__main__' and sys.flags.interactive == 0:
    if len(sys.argv) != 2:
        msg("ERREUR : lancez le script avec l'archive des archives en parametre: " + sys.argv[0] + " TOUTES_LES_ARCHIVES.zip")
        sys.exit(0)
    
    file = sys.argv[1]
    with ZipFile(file, 'r') as zip: 
        dir_all = zip.namelist()[0].split('/')[0]
        year = dir_all.split('_')[0]
        msg("*** année="+year)
        msg("*** dir all="+dir_all)
        msg("rm -rf "+dir_all )
        if isdir( dir_all):
            shutil.rmtree( dir_all )
        msg("extract all zip")
        zip.extractall() 


    plagiat = "plagiat"
    if not isdir(plagiat):
        os.mkdir(plagiat)
    os.chdir(plagiat)
    plagiat_dir = os.getcwd()
    os.chdir("..")
    msg("*** plagiat dir (output): "+ plagiat_dir)

    extract_all_students(dir_all, plagiat_dir, year)

    msg("pwd: "+os.getcwd())
    msg("rm -rf "+dir_all )
    shutil.rmtree( dir_all )

    # diff -y --suppress-common-lines 2020__11716941_11704898_11603981_11714862.txt 2020__11803116_11806115_11807885.txt