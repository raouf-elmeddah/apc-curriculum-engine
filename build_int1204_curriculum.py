# -*- coding: utf-8 -*-
"""
Script to build the full INT1204 curriculum tree according to the APC skill.
"""
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT"

def create_structure():
    # 1. Base folders
    folders = [
        BASE_DIR / "00_PROGRAMME_GLOBAL",
        BASE_DIR / "SEMESTRE_1" / "MQ1_Elaboration_des_algorithmes_simples" / "Lessons",
        BASE_DIR / "SEMESTRE_1" / "MQ3_Programmation_avec_un_langage_procedural_Part1" / "Lessons",
        BASE_DIR / "SEMESTRE_1" / "MC1_Anglais_Part1" / "Lessons",
        BASE_DIR / "SEMESTRE_1" / "MC2_Technique_d_expression_Part1" / "Lessons",
        BASE_DIR / "SEMESTRE_1" / "MC4_Architecture_des_ordinateurs" / "Lessons",
        BASE_DIR / "SEMESTRE_1" / "MQ8_Maintenance_d_un_poste_de_travail" / "Lessons",
        BASE_DIR / "SEMESTRE_1" / "MC8_Fichier" / "Lessons",
        BASE_DIR / "SEMESTRE_1" / "MC11_Mathematiques_Part1" / "Lessons",
        BASE_DIR / "SEMESTRE_2",
        BASE_DIR / "SEMESTRE_3",
        BASE_DIR / "SEMESTRE_4",
        BASE_DIR / "STAGE_PRATIQUE_MI",
    ]
    for f in folders:
        f.mkdir(parents=True, exist_ok=True)
    print("Folder hierarchy created successfully.")

if __name__ == "__main__":
    create_structure()
