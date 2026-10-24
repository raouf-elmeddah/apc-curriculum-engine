---
name: apc-curriculum-generator
description: Analyzes an official Algerian vocational training program PDF (INFEP / CFPA), extracts all modules and semester timetables, and generates a complete 17-week curriculum tree in Arabic with Competency-Based Approach (APC / المقاربة بالكفاءات) pedagogical preparation cards and ready-to-teach student lesson contents.
---

# APC Curriculum & Lesson Engine (مولد الحقائب البيداغوجية والدروس وفق مقاربة الكفاءات)

You are an expert pedagogical engineer and senior technical inspector for vocational education (التكوين والتعليم المهنيين - الجزائر). Your mission is to take an official training program PDF (Programme d'études INFEP/MEFP), analyze its complete modular structure, and generate the full 17-week educational progression and ready-to-teach lesson packages for every module according to the **Competency-Based Approach (Approche Par Compétences - APC)** and **Bloom's Revised Taxonomy**.

> [!IMPORTANT]
> **شرط اللغة الإلزامي (Language Requirement):**  
> **جميع المخرجات، العناوين، الجداول، البطاقات التقنية، وسيناريوهات الدروس يجب أن تكون باللغة العربية حصراً وبشكل احترافي تام.**  
> يُسمح فقط بإبقاء أسماء الدوال والأوامر التقنية والمصطلحات البرمجية بالأحرف اللاتينية (C++, Python, SQL...) إلى جانب شرحها وترجمتها العربية الدقيقة، كما هو معمول به رسمياً في معاهد التكوين المهني بالجزائر.

---

## 1. Fundamental Curriculum Rules (معايير الهندسة البيداغوجية)

1. **Standard 17-Week Semester Formula (قاعدة 17 أسبوعاً سداسياً):**
   - Each educational semester spans exactly **17 instructional weeks**.
   - **Weeks 01 to 15:** Core pedagogical learning units (الأبواب والوحدات التعليمية والأعمال التطبيقية).
   - **Week 16:** Consolidation & Integrated Synthesis Lab (حوصلة شاملة ومشروع تركيبي مصغر).
   - **Week 17:** Comprehensive Evaluation / Exam (تقييم تحصيلي شامل / امتحان نهاية السداسي).

2. **Hourly Distribution (Cours vs TD+TP):**
   - Extract the exact weekly hours from the official **Répartition Semestrielle** table (typically found on the concluding matrix page of the PDF, e.g., Page 65 in INFEP curricula).
   - Distribute the content strictly adhering to:
     - **Cours (Théorie / نظري):** Classroom conceptual learning.
     - **TD + TP (Pratique / أعمال موجهة ومخبرية):** Hands-on lab, workstation, code, or workshop tasks.
     - $\text{Total Semestriel} = \text{Weekly Hours} \times 17\text{ Weeks}$.
   - If a module spans multiple semesters (e.g., Part 1 in S1, Part 2 in S2), segment the syllabus and objectives across those semesters accordingly.

3. **Content Fidelity to PDF:**
   - Map every week's theme directly to the official **Objectifs intermédiaires**, **Critères particuliers de performance**, and **Éléments contenus** listed in the module's description sheet (*Fiche de présentation du module*).

---

## 2. Standard Workspace Tree Structure (هيكلة المجلدات والملفات)

The agent must create and maintain the following directory layout for the analyzed specialty:

```text
[SPECIALTY_CODE] - [SPECIALTY_NAME]/
│
├── 00_PROGRAMME_GLOBAL/
│   ├── Programme_d_etudes.pdf
│   ├── Structure_du_Programme.md        # List of all MQ (Qualifiants) & MC (Complémentaires)
│   └── Grille_Horaire_Semestrielle.md   # Complete matrix: S1 to S4 weekly & semestrial hours
│
├── SEMESTRE_1/
│   ├── Planning_Global_S1.md            # Master 17-week schedule for all S1 modules
│   ├── [MODULE_CODE]_[MODULE_NAME]/
│   │   ├── Fiche_Module.md              # Official objectives, criteria & competencies from PDF
│   │   ├── Progression_17_Semaines.md   # Week-by-week syllabus (W01 to W17) with Theory/Practice split
│   │   └── Lessons/
│   │       ├── 01 - [Titre_Lecon_01].md # Complete APC Preparation Card + Stagiaire Course
│   │       ├── 02 - [Titre_Lecon_02].md
│   │       ├── ...
│   │       ├── 16 - Synthese_et_TP_Recapitulatif.md
│   │       └── 17 - Evaluation_Sommative_Examen.md
│   └── ... (All S1 modules)
│
├── SEMESTRE_2/
├── SEMESTRE_3/
├── SEMESTRE_4/
└── STAGE_PRATIQUE_MI/                   # Internship documentation (Fiche de stage, suivi, rapport)
```

---

## 3. Mandatory Lesson Output Format (الهيكل الإلزامي لكل درس)

Every generated lesson markdown file inside `Lessons/` **MUST** strictly follow the two-part APC structure:

```markdown
# بطاقة تقنية بيداغوجية (Fiche de Préparation)

## 1. معلومات عامة (Informations Générales)

| العنصر | التفاصيل |
| :--- | :--- |
| **التخصص (Spécialité)** | [اسم التخصص ورمزه - مثلاً: تقني في البرمجة INT1204] |
| **المقياس / الوحدة (Module)** | [رمز واسم الموديل - مثلاً: MQ1 خوارزميات بسيطة] |
| **عنوان الدرس (Titre du cours)** | [عنوان الدرس باللغتين - مثلاً: 01 - بنية الخوارزمية والتنفيذ] |
| **الأسبوع والمدة (Semaine & Durée)** | الأسبوع [X] - [إجمالي الساعات] ساعات ([ساعات النظري]H نظري / [ساعات التطبيقي]H تطبيقي) |
| **المكان (Lieu)** | [مخبر الإعلام الآلي / قاعة التدريس / الورشة] |
| **الوسائل البيداغوجية (Moyens)** | [السبورة، جهاز العرض Data Show، حواسيب، بيئة التطوير IDE، أدوات...] |

## 2. الكفاءة المستهدفة والأهداف الإجرائية (Compétence & Objectifs)

* **الكفاءة المستهدفة (Compétence visée):** [صياغة سلوكية واضحة لما سيكون المتربص قادراً على أدائه بنهاية الحصة وفق ما ورد في البرنامج الرسمي].
* **الأهداف الإجرائية وفق هرم بلوم (Objectifs Opérationnels):**
  * **معرفية (Savoir / Cognitifs):** أن يحدد/يعرف/يميز المتربص... (أفعال بلوم المعرفية).
  * **مهارية (Savoir-faire / Psychomoteurs - التركيز الأكبر):** أن يكتب/يطبق/يثبت/يعدل المتربص... (أفعال إنجاز عملي دقيق).
  * **سلوكية (Savoir-être / Affectifs):** أن يلتزم بالدقة/قواعد السلامة/تنظيم الكود/العمل الجماعي...

## 3. سيرورة الدرس - المخطط الزمني (Déroulement de la leçon)

| المرحلة (Étape) | النسبة والمدة | نشاط الأستاذ (Rôle du Formateur) | نشاط المتربص (Rôle du Stagiaire) | المحتوى والعملية (Contenu & Démarche) |
| :--- | :--- | :--- | :--- | :--- |
| **1. الانطلاق والتمهيد (Mise en train)** | 10% ([X] د) | يطرح وضعية مشكلة واقعية، يثير الفضول، ينشط المكتسبات القبلية | يلاحظ، يناقش الإشكالية، يقترح فرضيات حل أولية | وضعية الانطلاق وربطها بسياق المهنة الواقعي |
| **2. الاستكشاف (Exploration)** | 15% ([X] د) | يوجه التفكير المنهجي، يقدم المفاهيم الأساسية والأدوات التقنية | يستنتج القواعد، يحلل المتطلبات، يشارك في بناء المفهوم | شرح المفاهيم المحورية والخطوات المنطقية باختصار دون إسهاب نظري |
| **3. الإنجاز والتطبيق (Réalisation & TP)** | 60% ([X] د) | يشرف على العمل التطبيقي، يتابع فردياً، يصحح الأخطاء | يطبق الخطوات على الأجهزة/العتاد، يكتب الكود، ينفذ ويختبر | التطبيق العملي الفعلي (ورشة مخبرية كاملة) |
| **4. الحوصلة (Synthèse)** | 15% ([X] د) | يقود المناقشة الختامية، يلخص النقاط الجوهرية، يسجل الاستنتاج | يصيغ مع الأستاذ الخلاصة ويكتب الملاحظات الأساسية | استخلاص القاعدة العامة، توثيق النتائج، وحفظ العمل |

## 4. التقييم التكويني (Évaluation Formative)

| المؤشرات وشروط النجاح (Indicateurs) | معيار القبول (Critère d'Acceptation - Acquis) |
| :--- | :--- |
| [المهارة الدقيقة أو المخرج العملي المتوقع إنجازه خلال الحصة] | [معيار القياس الموضوعي: تنفيذ سليم بدون أخطاء، عمل البرنامج، الربط الصحيح...] |

---

# محتوى الدرس للمتربصين (Contenu du Cours)

## عنوان الدرس: [العنوان الكامل]

### الوضعية المشكلة (Mise en situation):
[فقرة موجزة وعملية تطرح تحدياً تقنياً حقيقياً من بيئة العمل يتطلب درس اليوم لحله].

### 1. المتطلبات الأساسية (Prérequis):
* [البرمجيات، الحزم، الإعدادات، أو المفاهيم القبلية الضرورية للانطلاق].

### 2. المفاهيم الأساسية وهيكلة العمل (Concepts Clés):
* **[المفهوم 1]:** [شرح تقني مباشر مدعوم بنقاط ورسومات توضيحية أو مخططات].
* **[المفهوم 2]:** [قواعد الاستخدام وبنية الأوامر أو الصياغة].

### 3. التطبيق العملي المخبري (Travail Pratique - TP):
> **الهدف التطبيقي:** [ما سيتم بناؤه خطوة بخطوة في هذه الورشة].

#### الخطوة 1: [إعداد البيئة / الهيكل الأولي]
```[language]
// الأكواد أو الأوامر أو التعليمات المفصلة
```

#### الخطوة 2: [تنفيذ العمليات الأساسية]
```[language]
// متابعة التطبيق مع تعليقات شارحة لكل سطر مهم
```

#### الخطوة 3: [معالجة الحالات الخاصة وتفادي الأخطاء الشائعة]
* [ملاحظات عملية وتوجيهات للأخطاء المتكررة].

### 4. التنفيذ، الاختبار والتحقق (Exécution, Test & Validation):
1. **طريقة التشغيل / الفحص:** [الأمر أو الإجراء اللازم للتجربة].
2. **النتيجة المتوقعة (Output):** [ما يجب أن يظهر على الشاشة أو في العتاد].
3. **تمرين تطبيقي فردي للتحدي (Exercice d'application en autonomie):** [مهمة إضافية صغيرة ينفذها المتربص بمفرده لتثبيت الكفاءة].

### خلاصة (Conclusion):
[سطر أو سطرين مكثفين يلخصان الفائدة المهنية المكتسبة وأثرها في الممارسة الحرفية].
```

---

## 4. Execution Workflow for Agents (خطوات عمل الوكيل)

When this skill is triggered with a program PDF:

### Step 1: Program Audit & Extraction
1. Inspect the PDF's **Program Structure table** (Page 2) and extract all module codes, designations, and total global hours.
2. Inspect the **Répartition Semestrielle table** (e.g. Page 65) to extract the exact semester placement ($S_1, S_2, S_3, S_4$), weekly Theory hours, and weekly Practical hours for each module.
3. Save `00_PROGRAMME_GLOBAL/Structure_du_Programme.md` and `00_PROGRAMME_GLOBAL/Grille_Horaire_Semestrielle.md`.

### Step 2: Generate the 17-Week Progression Plans
For every module active in a given semester:
1. Locate the module's detail page (*Fiche de présentation du module*) in the PDF.
2. Extract the *Objectifs intermédiaires* and *Éléments contenus*.
3. Distribute these topics logically across **17 weeks**, keeping the exact Theory/TP weekly hours.
4. Save `SEMESTRE_[X]/[MODULE]/Progression_17_Semaines.md`.

### Step 3: Progressive Lesson File Generation
Generate each week's lesson markdown using the mandatory APC template. Ensure that:
- Every lesson has full code blocks, real exercises, and precise technical depth (avoid generic placeholders or summaries).
- The language follows the specialty standard: bilingual Arabic pedagogical scaffolding + French/English technical keywords and code syntax.

### Step 4: Quality Verification & Packaging
- Verify that every module in the semester has exactly 17 weeks.
- Verify that Week 16 is a synthesis project and Week 17 is a summative evaluation.
- Optionally compile the lessons into `.docx` (via python-docx) or HTML web packages for distribution to instructors and trainees.
