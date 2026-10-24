# -*- coding: utf-8 -*-
"""
Master Exhaustive Curriculum Generator for INT1204 - Programmation BT.
Generates fully developed, non-abbreviated, complete course content for students
and pedagogical preparation cards for teachers across all 4 Semesters.
"""
import os
import pathlib
import json

ROOT_DIR = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT"
SPEC = "تقني في الإعلام الآلي - خيار برمجة (INT1204 - BT)"

def sanitize(title):
    return "".join(c for c in title if c not in r'\/:*?"<>|')

def save_lesson(sem_folder, mod_folder, num, title, duree_str, lieu, moyens, 
                comp_visee, savoir, savoir_faire, savoir_etre, 
                situation, prerequis, concepts_rich, 
                tp_goal, tp_pratique_rich, validation_rich, conclusion_rich):
    
    lesson_dir = ROOT_DIR / sem_folder / mod_folder / "Lessons"
    lesson_dir.mkdir(parents=True, exist_ok=True)
    
    code_mod = mod_folder.split('_')[0]
    nom_mod = mod_folder.replace(code_mod + '_', '').replace('_', ' ')
    
    md_content = f"""# بطاقة تقنية بيداغوجية (Fiche de Préparation)

## 1. معلومات عامة (Informations Générales)

| العنصر | التفاصيل |
| :--- | :--- |
| **التخصص (Spécialité)** | {SPEC} |
| **المقياس / الوحدة (Module)** | {code_mod} - {nom_mod} |
| **عنوان الدرس (Titre du cours)** | {num} - {title} |
| **الأسبوع والمدة (Semaine & Durée)** | الأسبوع {num} - {duree_str} |
| **المكان (Lieu)** | {lieu} |
| **الوسائل البيداغوجية (Moyens)** | {moyens} |

---

## 2. الكفاءة المستهدفة والأهداف الإجرائية (Compétence & Objectifs)

* **الكفاءة المستهدفة (Compétence visée):**  
  {comp_visee}

* **الأهداف الإجرائية وفق هرم بلوم المعدل (Objectifs Opérationnels):**
  * **معرفية (Savoir / Cognitifs):**  
    {savoir}
  * **مهارية (Savoir-faire / Psychomoteurs - التركيز الأكبر):**  
    {savoir_faire}
  * **سلوكية (Savoir-être / Affectifs):**  
    {savoir_etre}

---

## 3. سيرورة الدرس - المخطط الزمني (Déroulement de la leçon)

| المرحلة (Étape) | النسبة والمدة | نشاط الأستاذ (Rôle du Formateur) | نشاط المتربص (Rôle du Stagiaire) | المحتوى والعملية (Contenu & Démarche) |
| :--- | :---: | :--- | :--- | :--- |
| **1. الانطلاق والتمهيد (Mise en train)** | 10% | يطرح وضعية المشكلة الواقعية، يثير الفضول، وينشط المكتسبات القبلية المتعلقة بالدرس السابق | يستمع باهتمام، يحلل الإشكالية المطروحة، ويقترح فرضيات أولية للحل | إبراز الحاجة التقنية إلى تعلم مهارة درس اليوم في بيئة العمل الحقيقية |
| **2. الاستكشاف (Exploration)** | 15% | يشرح المفاهيم العلمية والقواعد الهندسية أو النحوية للمفهوم الجديد بدقة | يدون القواعد والمصطلحات في دفتره ويشارك في تفكيك عناصر المفهوم | تقديم المادة المعرفية النظرية بأسلوب مباشر ومدعوم بالأمثلة |
| **3. الإنجاز والتطبيق (Réalisation & TP)** | 60% | يوزع بطاقات العمل المخبري، يشرف على التطبيق العملي، ويصحح الأخطاء الميدانية | ينفذ الخطوات العملية بالتفصيل، يكتب الكود أو يفكك العتاد، ويختبر النتائج | الورشة التطبيقية: تدريب عملي شامل خطوة بخطوة |
| **4. الحوصلة (Synthèse)** | 15% | يقود المناقشة الختامية، يلخص النقاط الجوهرية، ويسجل الاستنتاج العام | يساهم في صياغة الخلاصة العامة، يدون الملاحظات، ويحفظ عمله | تثبيت المكتسبات المهنية وتوثيق النتائج والتكليف المنزلي |

---

## 4. التقييم التكويني (Évaluation Formative)

| المؤشرات وشروط النجاح (Indicateurs) | معيار القبول والتحقق (Acquis) |
| :--- | :--- |
| 1. الفهم السليم للمفاهيم النظرية والمصطلحات التقنية. | الإجابة الصحيحة بنسبة 100% عن الأسئلة الشفوية والاختبارات المباشرة. |
| 2. دقة التنفيذ العملي وخلو النتائج من الأخطاء التشغيلية. | مطابقة المخرجات للمواصفات الفنية المحددة في بطاقة الورشة بنجاح. |
| 3. القدرة على استكشاف الأخطاء وتصحيحها ذاتياً (Debugging / Dépannage). | معالجة الحالات الحدية وتجاوز الأعطال الشائعة بنجاح واستقلالية. |

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
{concepts_rich}

---

### 3. التطبيق العملي المخبري (Travail Pratique - TP):
> **الهدف العملي للورشة:** {tp_goal}

{tp_pratique_rich}

---

### 4. التنفيذ، الاختبار والتحقق (Exécution, Test & Validation):
{validation_rich}

---

### خلاصة الدرس (Conclusion):
{conclusion_rich}
"""
    file_name = f"{num} - {sanitize(title)}.md"
    (lesson_dir / file_name).write_text(md_content, encoding="utf-8")

print("Save lesson engine ready.")
