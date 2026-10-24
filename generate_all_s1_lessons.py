# -*- coding: utf-8 -*-
"""
Generate complete lessons for remaining Semester 1 modules:
MC4 (Architecture - 17 lessons), MQ8 (Maintenance - 17 lessons), MC8 (Fichier - 17 lessons),
MC11 (Maths - 17 lessons), MC1 (Anglais - 17 lessons), MC2 (Expression - 17 lessons).
"""
import os
import pathlib

BASE_S1 = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT" / "SEMESTRE_1"

def sanitize(title):
    return "".join(c for c in title if c not in r'\/:*?"<>|')

def build_lesson(specialite, code_mod, nom_mod, num, title, duree_str, lieu, moyens, comp, savoir, savoir_faire, savoir_etre, situation, prerequis, concepts, tp_goal, tp_content, validation, conclusion):
    md = f"""# بطاقة تقنية بيداغوجية (Fiche de Préparation)

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
    return md

# Let's write generator logic for MC4, MQ8, MC8, MC11, MC1, MC2
print("Helper template configured.")
