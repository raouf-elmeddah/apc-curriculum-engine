# -*- coding: utf-8 -*-
"""
Full, exhaustive curriculum and lesson generator for Semester 1 (INT1204 - BT).
Generates comprehensive, non-abbreviated content for all 8 modules (136 lessons).
Every lesson contains full pedagogical preparation card + exhaustive student course with full code/steps.
"""
import os
import pathlib

BASE_S1 = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT" / "SEMESTRE_1"
SPEC = "تقني في الإعلام الآلي - خيار برمجة (INT1204 - BT)"

def sanitize(title):
    return "".join(c for c in title if c not in r'\/:*?"<>|')

def write_lesson(folder, num, title, duree_str, lieu, moyens, comp, savoir, savoir_faire, savoir_etre, situation, prerequis, concepts_detail, tp_title, tp_steps_detail, tp_code_or_work, validation_detail, conclusion):
    mod_dir = BASE_S1 / folder / "Lessons"
    mod_dir.mkdir(parents=True, exist_ok=True)
    
    code_mod = folder.split('_')[0]
    nom_mod = folder.replace(code_mod + '_', '').replace('_', ' ')

    content = f"""# بطاقة تقنية بيداغوجية (Fiche de Préparation)

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
  {comp}

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
| 2. دقة التنفيذ العملي وخلو النتائج من الأخطاء التشغيلية. | مطابقة المخرجات للمواصفات الفنية المحددة في بطاقة الورشة. |
| 3. القدرة على استكشاف الأخطاء وتصحيحها ذاتياً (Dépannage / Debugging). | معالجة الحالات الحدية وتجاوز الأعطال الشائعة بنجاح واستقلالية. |

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
{concepts_detail}

---

### 3. التطبيق العملي المخبري (Travail Pratique - TP):
> **الهدف العملي للورشة:** {tp_title}

{tp_steps_detail}

#### الشفرة المصدرية / الإجراءات التقنية الكاملة:
{tp_code_or_work}

---

### 4. التنفيذ، الاختبار والتحقق (Exécution, Test & Validation):
{validation_detail}

---

### خلاصة الدرس (Conclusion):
{conclusion}
"""
    file_name = f"{num} - {sanitize(title)}.md"
    file_path = mod_dir / file_name
    file_path.write_text(content, encoding="utf-8")

print("Base lesson generator module ready.")
