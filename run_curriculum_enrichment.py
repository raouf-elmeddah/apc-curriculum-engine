# -*- coding: utf-8 -*-
"""
Execution script to enrich all modules across Semesters 1, 2, 3, and 4
Ensuring that all lessons have exhaustive, non-abbreviated content for students.
"""
import pathlib
from populate_entire_curriculum_rich import generate_rich_module

ROOT_DIR = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT"

semesters = [
    {
        "folder": "SEMESTRE_1",
        "label": "السداسي الأول",
        "modules": [
            ("MC4_Architecture_des_ordinateurs", "MC4", "بنية وهندسة الحواسيب", "قاعة التدريس / مخبر العتاد", "السبورة، جهاز العرض، لوحات إلكترونية، مجسمات المعالجات"),
            ("MQ8_Maintenance_d_un_poste_de_travail", "MQ8", "صيانة منصب العمل", "ورشة صيانة العتاد والمخبر", "حقائب مفكات، ملتيميتر، حواسيب معطلة للتجريب، برمجيات فحص"),
            ("MC8_Fichier", "MC8", "ملفات المعطيات الكلاسيكية", "قاعة التدريس / مخبر الإعلام الآلي", "السبورة، جهاز العرض، أوراق التحليل الهيكلي"),
            ("MC11_Mathematiques_Part1", "MC11", "رياضيات الإعلام الآلي (ج 1)", "قاعة التدريس", "السبورة، أوراق التمارين، آلات حاسبة علمية"),
            ("MC1_Anglais_Part1", "MC1", "اللغة الإنجليزية التقنية (ج 1)", "قاعة التدريس / مخبر اللغات", "السبورة، جهاز العرض، معاجم تقنية، نصوص إنجليزية"),
            ("MC2_Technique_d_expression_Part1", "MC2", "تقنيات التعبير والتحرير (ج 1)", "قاعة التدريس", "السبورة، نماذج تقارير ومحاضر إدارية رسمية"),
        ]
    },
    {
        "folder": "SEMESTRE_2",
        "label": "السداسي الثاني",
        "modules": [
            ("MQ2_Elaboration_des_algorithmes_complexes", "MQ2", "إعداد الخوارزميات المعقدة", "مخبر الإعلام الآلي", "السبورة، جهاز العرض، حواسيب، بيئة تحرير الخوارزميات"),
            ("MQ3_Programmation_avec_un_langage_procedural_Part2", "MQ3", "البرمجة الإجرائية C++ (ج 2)", "مخبر البرمجة", "حواسيب، بيئة تطوير C++، مترجم GCC"),
            ("MQ4_Programmation_orientee_objet_POO_Part1", "MQ4", "البرمجة كائنية التوجه POO C++ (ج 1)", "مخبر البرمجة", "حواسيب، بيئة تطوير C++"),
            ("MQ7_Installation_et_configuration_d_un_poste_de_travail", "MQ7", "تثبيت وتهيئة منصب العمل", "ورشة العتاد ومخبر الصيانة", "مفكات، حواسيب، فلاشات إقلاعية، أسطوانات أنظمة"),
            ("MC3_Hygiene_securite_et_environnement", "MC3", "النظافة والأمن والبيئة HSE", "قاعة التدريس / ورشة السلامة", "السبورة، مطفآت حريق، أدوات إسعاف، لافتات السلامة"),
            ("MC5_Bureautique_Part1", "MC5", "الإعلام الآلي المكتبي - Word", "مخبر الإعلام الآلي", "حواسيب، برنامج MS Word، طابعات"),
            ("MC1_Anglais_Part2", "MC1", "اللغة الإنجليزية التقنية (ج 2)", "قاعة التدريس", "السبورة، جهاز العرض، معاجم متخصصة"),
            ("MC2_Technique_d_expression_Part2", "MC2", "تقنيات التعبير والتحرير (ج 2)", "قاعة التدريس", "السبورة، نماذج السير الذاتية ومذكرات التخرج"),
            ("MC11_Mathematiques_Part2", "MC11", "رياضيات الإعلام الآلي (ج 2)", "قاعة التدريس", "السبورة، آلات حاسبة، أوراق التمارين"),
        ]
    },
    {
        "folder": "SEMESTRE_3",
        "label": "السداسي الثالث",
        "modules": [
            ("MQ4_Programmation_orientee_objet_POO_Part2", "MQ4", "البرمجة كائنية التوجه POO C++ (ج 2)", "مخبر البرمجة", "حواسيب، بيئة تطوير C++، محرك قواعد بيانات"),
            ("MQ5_Programmation_evenementielle_Part1", "MQ5", "البرمجة بالحدث C++ Builder (ج 1)", "مخبر البرمجة بالحدث", "حواسيب، بيئة C++ Builder متطورة"),
            ("MC7_Access_Part1", "MC7", "قواعد البيانات أكسس Access (ج 1)", "مخبر قواعد البيانات", "حواسيب، برمجيات MS Access"),
            ("MC6_Reseaux_et_Internet", "MC6", "الشبكات والإنترنت", "مخبر الشبكات", "كابلات RJ45، ملاقط، سويتشات، راوترات، Cisco Packet Tracer"),
            ("MQ6_Exploitation_des_BD_en_ligne", "MQ6", "استغلال قواعد البيانات عبر الإنترنت PHP/MySQL", "مخبر تطوير الويب", "حواسيب، سيرفر XAMPP، محرر كود، متصفحات"),
            ("MC9_SGBD", "MC9", "أنظمة تسيير قواعد البيانات SGBD / SQL", "مخبر قواعد البيانات", "حواسيب، محرك قواعد بيانات، أدوات نمذجة"),
            ("MC10_Organisation_d_entreprise", "MC10", "تنظيم المؤسسات والاقتصاد", "قاعة التدريس", "السبورة، جهاز العرض، دراسات حالة لشركات وطنية"),
            ("MC5_Bureautique_Part2", "MC5", "الإعلام الآلي المكتبي - Excel", "مخبر الإعلام الآلي", "حواسيب، برمجيات MS Excel"),
        ]
    },
    {
        "folder": "SEMESTRE_4",
        "label": "السداسي الرابع",
        "modules": [
            ("MQ5_Programmation_evenementielle_Part2", "MQ5", "البرمجة بالحدث C++ Builder (ج 2)", "مخبر البرمجة بالحدث", "حواسيب، بيئة C++ Builder، قواعد بيانات"),
            ("MC7_Access_Part2", "MC7", "قواعد البيانات أكسس Access (ج 2)", "مخبر قواعد البيانات", "حواسيب، برمجيات MS Access"),
            ("MC12_Protection_du_consommateur", "MC12", "حماية المستهلك", "قاعة التدريس", "السبورة، نصوص قانون حماية المستهلك الجزائري"),
            ("MC13_Methodologie", "MC13", "منهجية وإعداد مذكرة التخرج", "قاعة التدريس / مخبر الإعلام الآلي", "السبورة، نماذج مذكرات سابقة، عروض تقديمية"),
        ]
    }
]

def main():
    for sem in semesters:
        s_folder = sem["folder"]
        s_label = sem["label"]
        print(f"Enriching {s_folder}...")
        for mod_folder, mod_code, mod_name, lieu, moyens in sem["modules"]:
            generate_rich_module(s_folder, s_label, mod_folder, mod_code, mod_name, lieu, moyens, {})
    print("ALL modules across ALL semesters enriched with rich, non-abbreviated content successfully!")

if __name__ == "__main__":
    main()
