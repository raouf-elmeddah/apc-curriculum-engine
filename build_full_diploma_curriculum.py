# -*- coding: utf-8 -*-
"""
Full Diploma Curriculum Builder for INT1204 - Programmation BT
Generates S1 remaining lessons, S2, S3, S4 modules and lessons, and MI Internship docs.
"""
import os
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT"

def sanitize(title):
    return "".join(c for c in title if c not in r'\/:*?"<>|')

def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def make_lesson(specialite, code_mod, nom_mod, num, title, duree_str, lieu, moyens, comp, savoir, savoir_faire, savoir_etre, situation, prerequis, concepts, tp_goal, tp_content, validation, conclusion):
    return f"""# بطاقة تقنية بيداغوجية (Fiche de Préparation)

## 1. معلومات عامة (Informations Générales)

| العنصر | التفاصيل |
| :--- | :--- |
| **التخصص (Spécialité)** | {specialite} |
| **المقياس / الوحدة (Module)** | {code_mod} - {nom_mod} |
| **عنوان الدرس (Titre du cours)** | {num} - {title} |
| **الأسبوع والمدة (Semaine & Durée)** | الأسبوع {num} - {duree_str} |
| **المكان (Lieu)** | {lieu} |
| **الوسائل البيداغوجية (Moyens)** | {moyens} |

---

## 2. الكفاءة المستهدفة والأهداف الإجرائية (Compétence & Objectifs)

* **الكفاءة المستهدفة (Compétence visée):**  
  {comp}

* **الأهداف الإجرائية وفق هرم بلوم المعدل (Objectifs Opérationnels):**
  * **معرفية (Savoir / Cognitifs):** {savoir}
  * **مهارية (Savoir-faire / Psychomoteurs):** {savoir_faire}
  * **سلوكية (Savoir-être / Affectifs):** {savoir_etre}

---

## 3. سيرورة الدرس - المخطط الزمني (Déroulement de la leçon)

| المرحلة (Étape) | النسبة والمدة | نشاط الأستاذ (Rôle du Formateur) | نشاط المتربص (Rôle du Stagiaire) | المحتوى والعملية (Contenu & Démarche) |
| :--- | :---: | :--- | :--- | :--- |
| **1. الانطلاق والتمهيد (Mise en train)** | 10% | يطرح وضعية المشكلة الواقعية، يثير الفضول، وينشط المكتسبات القبلية | يحلل الإشكالية المطروحة ويقترح فرضيات أولية للحل | ربط المفهوم النظري بالتحديات المهنية الواقعية |
| **2. الاستكشاف (Exploration)** | 15% | يقدم المفاهيم الأساسية، القواعد العلمية، والخرائط الذهنية أو المخططات | يدون القواعد والملاحظات في دفتره ويشارك في تفكيك المفهوم | شرح مركز ومباشر للمفاهيم الأساسية دون حشو |
| **3. الإنجاز والتطبيق (Réalisation & TP)** | 60% | يوزع بطاقات التمارين أو العمل المخبري، يوجه المتربصين، ويصحح الأخطاء | ينجز التطبيق العملي، يحل التمارين، يختبر العتاد أو البرمجيات | الورشة التطبيقية: تدريب عملي خطوة بخطوة |
| **4. الحوصلة (Synthèse)** | 15% | يقود المناقشة الختامية، يلخص النقاط الجوهرية، ويسجل الاستنتاج العام | يشارك في صياغة الخلاصة ويدونها في دفتره | تثبيت المكتسبات المهنية والتحضير للحصة القادمة |

---

## 4. التقييم التكويني (Évaluation Formative)

| المؤشرات وشروط النجاح (Indicateurs) | معيار القبول والتحقق (Acquis) |
| :--- | :--- |
| 1. استيعاب المفاهيم النظرية وتطبيق القواعد العلمية السليمة. | الإجابة الصحيحة بنسبة لا تقل عن 80% عن الأسئلة الشفوية والتقنية. |
| 2. إنجاز المهام التطبيقية وحل المسائل في الوقت المحدد. | تنفيذ الخطوات بنجاح وتحقيق النتيجة المطلوبة بدون أخطاء. |

---

# محتوى الدرس للمتربصين (Contenu du Cours)

## عنوان الدرس: {title}

---

### الوضعية المشكلة (Mise en situation):
{situation}

---

### 1. المتطلبات الأساسية (Prérequis):
{prerequis}

---

### 2. المفاهيم الأساسية وهيكلة العمل (Concepts Clés):
{concepts}

---

### 3. التطبيق العملي المخبري (Travail Pratique - TP):
> **الهدف العملي للورشة:** {tp_goal}

{tp_content}

---

### 4. التنفيذ، الاختبار والتحقق (Exécution, Test & Validation):
{validation}

---

### خلاصة الدرس (Conclusion):
{conclusion}
"""

def generate_module_lessons(base_mod_dir, spec_name, mod_code, mod_name, duree_str, lieu, moyens, progression_text, tp_template_func):
    lessons_dir = base_mod_dir / "Lessons"
    lessons_dir.mkdir(parents=True, exist_ok=True)
    
    # parse lines from progression_text
    lines = [l.strip() for l in progression_text.strip().split("\n") if l.strip().startswith("| **W")]
    for line in lines:
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 4:
            w_num = parts[0].replace("**", "").replace("W", "").strip()
            title = parts[1].replace("**", "").strip()
            h_type = parts[2].strip()
            content_desc = parts[3].strip()
            
            comp = f"أن يتحكم المتربص في مهارات ومعارف: {title} وتطبيقها عملياً."
            savoir = f"استيعاب وتحديد المفاهيم النظرية لـ: {title}."
            savoir_faire = f"إنجاز وتطبيق: {content_desc} بدقة ومهارة مهنية."
            savoir_etre = "الالتزام بالدقة المنهجية وقواعد السلامة وحسن التنظيم."
            situation = f"في بيئة عمل مهنية تابعة للإعلام الآلي، تطلب المؤسسة إنجاز مهمة تتعلق بـ ({title}) لتحسين جودة الأداء التقني."
            prerequis = "* المكتسبات المعرفية من الأسابيع السابقة وحسن استخدام أدوات العمل."
            concepts = f"* **المفهوم المحوري:** {title}.\n* **التفاصيل:** {content_desc}."
            tp_goal = f"تطبيق عملي خطوة بخطوة حول: {title}."
            tp_content = tp_template_func(mod_code, w_num, title, content_desc)
            validation = "1. اختبار ومراجعة الخطوات المنفذة.\n2. التحقق من مطابقة النتائج للمواصفات المطلوبة.\n3. تمرين تحدي فردي للمتربص لترسيخ الكفاءة."
            conclusion = f"إن إتقان موضوع ({title}) يمنح المتربص كفاءة ميدانية حقيقية تساهم في تكوينه كتقني برمجة محترف."
            
            lesson_md = make_lesson(
                spec_name, mod_code, mod_name, w_num, title,
                f"{duree_str} ({h_type})", lieu, moyens,
                comp, savoir, savoir_faire, savoir_etre, situation,
                prerequis, concepts, tp_goal, tp_content, validation, conclusion
            )
            file_name = f"{w_num} - {sanitize(title)}.md"
            write_file(lessons_dir / file_name, lesson_md)

print("Framework ready for full execution.")
