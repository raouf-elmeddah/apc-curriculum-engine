# -*- coding: utf-8 -*-
"""
Exhaustive lesson content generator for Semester 1: MC4, MQ8, MC8, MC11, MC1, MC2.
Each lesson contains comprehensive technical theory, detailed practical procedures,
diagrams/tables, complete code or step-by-step lab tasks, validation exercises, and summaries.
"""
import os
import pathlib
from generate_s1_full_curriculum import write_lesson, sanitize

BASE_S1 = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT" / "SEMESTRE_1"

# We will write specialized generators for each module.
print("Module generator template ready.")
