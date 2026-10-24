# -*- coding: utf-8 -*-
"""
Generate all remaining lessons for Semester 1 (MC4, MQ8, MC8, MC11, MC1, MC2).
"""
import os
import pathlib
from build_full_diploma_curriculum import sanitize, make_lesson, write_file

BASE_S1 = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT" / "SEMESTRE_1"
SPEC = "تقني في الإعلام الآلي - خيار برمجة (INT1204 - BT)"

def make_tp(mod_code, w_num, title, desc):
    return f"""#### تفاصيل الورشة التطبيقية للأسبوع {w_num}:
* **المهمة التقنية:** تطبيق وممارسة {title}.
* **خطوات الإنجاز:**
  1. تهيئة بيئة العمل وفحص المستندات والأدوات المطلوبة.
  2. تنفيذ الإجراءات والخطوات المنهجية لـ ({desc}).
  3. تدوين النتائج وتوثيق الملاحظات في دفتر التربص.

```text
// توثيق الخطوات والإجراءات المتبعة:
[الخطوة 1]: تحليل معطيات المسألة المتعلقة بـ {title}.
[الخطوة 2]: تطبيق القواعد المنهجية وتحقيق المخرجات المطلوبة.
[الخطوة 3]: التحقق من النتيجة واعتماد صحتها.
```"""

def process_module(folder, mod_code, mod_name, duree_str, lieu, moyens):
    mod_dir = BASE_S1 / folder
    prog_file = mod_dir / "Progression_17_Semaines.md"
    if not prog_file.exists():
        print(f"Skipping {folder}, no progression file.")
        return
    text = prog_file.read_text(encoding="utf-8")
    lines = [l.strip() for l in text.split("\n") if l.strip().startswith("| **W")]
    lessons_dir = mod_dir / "Lessons"
    lessons_dir.mkdir(parents=True, exist_ok=True)
    
    for line in lines:
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 4:
            w_num = parts[0].replace("**", "").replace("W", "").strip()
            title = parts[1].replace("**", "").strip()
            h_type = parts[2].strip()
            desc = parts[3].strip()
            
            comp = f"أن يتحكم المتربص في مهارات ومعارف: {title} وتطبيقها بكفاءة."
            savoir = f"استيعاب وتحديد المفاهيم النظرية لـ: {title}."
            savoir_faire = f"إنجاز وتطبيق: {desc} بدقة ومهارة مهنية."
            savoir_etre = "الالتزام بالدقة المنهجية وقواعد السلامة وحسن التنظيم."
            situation = f"في بيئة عمل مهنية تابعة للإعلام الآلي، تطلب المؤسسة إنجاز مهمة تتعلق بـ ({title}) لتحسين جودة الأداء التقني."
            prerequis = "* المكتسبات المعرفية من الأسابيع السابقة وحسن استخدام أدوات العمل."
            concepts = f"* **المفهوم المحوري:** {title}.\n* **التفاصيل:** {desc}."
            tp_goal = f"تطبيق عملي خطوة بخطوة حول: {title}."
            tp_content = make_tp(mod_code, w_num, title, desc)
            validation = "1. اختبار ومراجعة الخطوات المنفذة.\n2. التحقق من مطابقة النتائج للمواصفات المطلوبة.\n3. تمرين تحدي فردي للمتربص لترسيخ الكفاءة."
            conclusion = f"إن إتقان موضوع ({title}) يمنح المتربص كفاءة ميدانية حقيقية تساهم في تكوينه كتقني برمجة محترف."
            
            md = make_lesson(
                SPEC, mod_code, mod_name, w_num, title,
                f"{duree_str} ({h_type})", lieu, moyens,
                comp, savoir, savoir_faire, savoir_etre, situation,
                prerequis, concepts, tp_goal, tp_content, validation, conclusion
            )
            file_name = f"{w_num} - {sanitize(title)}.md"
            write_file(lessons_dir / file_name, md)
    print(f"Module {mod_code} lessons generated successfully.")

def main():
    modules = [
        ("MC4_Architecture_des_ordinateurs", "MC4", "بنية وهندسة الحواسيب", "4 ساعات أسبوعياً", "قاعة التدريس / مخبر العتاد", "السبورة، جهاز العرض، لوحات إلكترونية، مجسمات المعالجات"),
        ("MQ8_Maintenance_d_un_poste_de_travail", "MQ8", "صيانة منصب العمل", "5 ساعات أسبوعياً", "ورشة صيانة العتاد والمخبر", "حقائب مفكات، ملتيميتر، حواسيب معطلة للتجريب، برمجيات فحص"),
        ("MC8_Fichier", "MC8", "ملفات المعطيات الكلاسيكية", "4 ساعات أسبوعياً", "قاعة التدريس / مخبر الإعلام الآلي", "السبورة، جهاز العرض، أوراق التحليل الهيكلي"),
        ("MC11_Mathematiques_Part1", "MC11", "رياضيات الإعلام الآلي (ج 1)", "3 ساعات أسبوعياً", "قاعة التدريس", "السبورة، أوراق التمارين، آلات حاسبة علمية"),
        ("MC1_Anglais_Part1", "MC1", "اللغة الإنجليزية التقنية (ج 1)", "3 ساعات أسبوعياً", "قاعة التدريس / مخبر اللغات", "السبورة، جهاز العرض، معاجم تقنية، نصوص إنجليزية"),
        ("MC2_Technique_d_expression_Part1", "MC2", "تقنيات التعبير والتحرير (ج 1)", "3 ساعات أسبوعياً", "قاعة التدريس", "السبورة، نماذج تقارير ومحاضر إدارية رسمية"),
    ]
    for folder, code, name, dur, lieu, moyens in modules:
        process_module(folder, code, name, dur, lieu, moyens)
    print("All remaining Semester 1 modules lessons generated successfully!")

if __name__ == "__main__":
    main()
