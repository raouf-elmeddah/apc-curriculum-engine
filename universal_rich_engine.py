# -*- coding: utf-8 -*-
"""
Universal Rich Content Engine for INT1204 - Programmation BT.
Generates comprehensive, in-depth, non-abbreviated content for all modules across Semesters 1 to 4.
"""
import os
import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT"
SPEC = "تقني في الإعلام الآلي - خيار برمجة (INT1204 - BT)"

def sanitize(title):
    return "".join(c for c in title if c not in r'\/:*?"<>|')

def build_rich_lesson_file(file_path, sem_name, mod_code, mod_name, w_num, title, h_type, desc, rich_domain_data):
    """
    Builds an exhaustive, multi-page APC markdown document for a lesson.
    """
    comp_visee = rich_domain_data["comp"]
    savoir = rich_domain_data["savoir"]
    savoir_faire = rich_domain_data["savoir_faire"]
    savoir_etre = rich_domain_data["savoir_etre"]
    situation = rich_domain_data["situation"]
    prerequis = rich_domain_data["prerequis"]
    concepts = rich_domain_data["concepts"]
    tp_title = rich_domain_data["tp_title"]
    tp_steps = rich_domain_data["tp_steps"]
    tp_code = rich_domain_data["tp_code"]
    validation = rich_domain_data["validation"]
    conclusion = rich_domain_data["conclusion"]
    lieu = rich_domain_data.get("lieu", "مخبر الإعلام الآلي والبرمجة")
    moyens = rich_domain_data.get("moyens", "السبورة، جهاز الععرض، حواسيب متصلة بشبكة، بيئة التطوير")

    md = f"""# بطاقة تقنية بيداغوجية (Fiche de Préparation)

## 1. معلومات عامة (Informations Générales)

| العنصر | التفاصيل |
| :--- | :--- |
| **التخصص (Spécialité)** | {SPEC} |
| **المقياس / الوحدة (Module)** | {mod_code} - {mod_name} |
| **عنوان الدرس (Titre du cours)** | {w_num} - {title} |
| **السداسي والمدة (Semestre & Durée)** | {sem_name} - الأسبوع {w_num} ({h_type}) |
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
| **2. الاستكشاف (Exploration)** | 15% | يشرح المفاهيم العلمية والقواعد الهندسية أو النحوية للمفهوم الجديد بدقة وتفصيل | يدون القواعد والمصطلحات في دفتره ويشارك في تفكيك عناصر المفهوم | تقديم المادة المعرفية النظرية بأسلوب مباشر ومدعوم بالأمثلة الشارحة |
| **3. الإنجاز والتطبيق (Réalisation & TP)** | 60% | يوزع بطاقات العمل المخبري، يشرف على التطبيق العملي، ويصحح الأخطاء الميدانية | ينفذ الخطوات العملية بالتفصيل، يكتب الكود أو يفكك العتاد، ويختبر النتائج | الورشة التطبيقية: تدريب عملي شامل خطوة بخطوة حتى التمكين التام |
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
{concepts}

---

### 3. التطبيق العملي المخبري (Travail Pratique - TP):
> **الهدف العملي للورشة:** {tp_title}

{tp_steps}

#### الأكواد البرمجية والخطوات التقنية المنفذة:
{tp_code}

---

### 4. التنفيذ، الاختبار والتحقق (Exécution, Test & Validation):
{validation}

---

### خلاصة الدرس (Conclusion):
{conclusion}
"""
    file_path.write_text(md, encoding="utf-8")

print("Universal Rich Content Engine compiled.")
