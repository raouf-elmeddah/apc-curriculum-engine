# -*- coding: utf-8 -*-
"""
Generate an index file for Semester 1 to make browsing all modules and lessons effortless.
"""
import pathlib

BASE_S1 = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT" / "SEMESTRE_1"
index_path = BASE_S1 / "دليل_السداسي_الأول_الفهرس.md"

index_content = """# الدليل البيداغوجي الشامل للسداسي الأول (Index Semestre 1)
**تخصص: تقني في الإعلام الآلي - خيار برمجة (INT1204 - BT)**  
*الحجم الساعي الإجمالي للسداسي الأول: 493 ساعة (29 ساعة أسبوعياً على مدار 17 أسبوعاً تدريسياً).*

---

## 📚 فهرس المقاييس والوثائق المنجزة للسداسي الأول

### 1. المقاييس التأهيلية الأساسية (Modules Qualifiants)

#### أ. مقياس MQ1: إعداد الخوارزميات البسيطة (Élaboration des algorithmes simples)
* **الحجم الساعي:** 68 ساعة (4 ساعات أسبوعياً: 2H نظري + 2H مخبر).
* **وثائق المقياس:**
  * [بطاقة تقديم المقياس الرسمية (Fiche Module)](./MQ1_Elaboration_des_algorithmes_simples/Fiche_Module.md)
  * [التدرج البيداغوجي لـ 17 أسبوعاً (Progression)](./MQ1_Elaboration_des_algorithmes_simples/Progression_17_Semaines.md)
* **المذكرات البيداغوجية والدروس (17 درساً مكتملاً وفق APC):**
  1. [الأسبوع 01: مفهوم الخوارزمية ومنهجية حل المشكلات البرمجية](./MQ1_Elaboration_des_algorithmes_simples/Lessons/01%20-%20مفهوم%20الخوارزمية%20ومنهجية%20حل%20المشكلات%20البرمجية.md)
  2. [الأسبوع 02: الشكل العام للخوارزمية والمخططات الانسيابية](./MQ1_Elaboration_des_algorithmes_simples/Lessons/02%20-%20الشكل%20العام%20للخوارزمية%20والمخططات%20الانسيابية%20(Organigrammes).md)
  3. [الأسبوع 03: المتغيرات، الثوابت، والأنواع البيانية الأساسية](./MQ1_Elaboration_des_algorithmes_simples/Lessons/03%20-%20المتغيرات،%20الثوابت،%20والأنواع%20البيانية%20الأساسية.md)
  4. [الأسبوع 04: العمليات الأساسية القراءة، الكتابة، والإسناد](./MQ1_Elaboration_des_algorithmes_simples/Lessons/04%20-%20العمليات%20الأساسية%20القراءة%20(Lire)،%20الكتابة%20(Écrire)،%20والإسناد%20(←).md)
  5. [الأسبوع 05: البنية الشرطية البسيطة والبديلة](./MQ1_Elaboration_des_algorithmes_simples/Lessons/05%20-%20البنية%20الشرطية%20البسيطة%20والبديلة%20(Si%20...%20Alors%20...%20Sinon).md)
  6. [الأسبوع 06: البنية الشرطية المتعددة والشروط المركبة](./MQ1_Elaboration_des_algorithmes_simples/Lessons/06%20-%20البنية%20الشرطية%20المتعددة%20والشروط%20المركبة%20(Selon%20%20Cas%20où).md)
  7. [الأسبوع 07: البنية التكرارية بعداد محدد حلقة Pour](./MQ1_Elaboration_des_algorithmes_simples/Lessons/07%20-%20البنية%20التكرارية%20بعداد%20محدد%20حلقة%20(Pour%20...%20Faire).md)
  8. [الأسبوع 08: البنية التكرارية بالشرط القبلي حلقة Tant Que](./MQ1_Elaboration_des_algorithmes_simples/Lessons/08%20-%20البنية%20التكرارية%20بالشرط%20القبلي%20حلقة%20(Tant%20Que%20...%20Faire).md)
  9. [الأسبوع 09: البنية التكرارية بالشرط البعدي حلقة Répéter](./MQ1_Elaboration_des_algorithmes_simples/Lessons/09%20-%20البنية%20التكرارية%20بالشرط%20البعدي%20حلقة%20(Répéter%20...%20Jusqu'à).md)
  10. [الأسبوع 10: السلاسل النصية الحرفية والعمليات عليها](./MQ1_Elaboration_des_algorithmes_simples/Lessons/10%20-%20السلاسل%20النصية%20الحرفية%20(Chaînes%20de%20caractères)%20والعمليات%20عليها.md)
  11. [الأسبوع 11: الجداول أحادية البعد (Vecteurs) المفهوم والتصريح](./MQ1_Elaboration_des_algorithmes_simples/Lessons/11%20-%20الجداول%20أحادية%20البعد%20(Vecteurs)%20المفهوم%20والتصريح%20والقراءة.md)
  12. [الأسبوع 12: الخوارزميات الحسابية والبحثية في الجداول الأحادية](./MQ1_Elaboration_des_algorithmes_simples/Lessons/12%20-%20الخوارزميات%20الحسابية%20والبحثية%20في%20الجداول%20الأحادية%20(Min,%20Max,%20Somme).md)
  13. [الأسبوع 13: خوارزميات الترتيب والفرز في الجداول](./MQ1_Elaboration_des_algorithmes_simples/Lessons/13%20-%20خوارزميات%20الترتيب%20والفرز%20في%20الجداول%20(Tri%20par%20sélection%20&%20Tri%20à%20bulles).md)
  14. [الأسبوع 14: الجداول ثنائية الأبعاد (Matrices) المفهوم والمعالجة](./MQ1_Elaboration_des_algorithmes_simples/Lessons/14%20-%20الجداول%20ثنائية%20الأبعاد%20(Matrices)%20المفهوم%20والتصريح%20والمعالجة.md)
  15. [الأسبوع 15: العمليات المتقدمة على المصفوفات والقطر الرئيسي](./MQ1_Elaboration_des_algorithmes_simples/Lessons/15%20-%20العمليات%20المتقدمة%20على%20المصفوفات%20(مجموع%20الأسطر،%20القطر%20الرئيسي).md)
  16. [الأسبوع 16: حوصلة عامة ومشروع تطبيقي تركيبي شامل](./MQ1_Elaboration_des_algorithmes_simples/Lessons/16%20-%20حوصلة%20عامة%20 ومشروع%20تطبيقي%20تركيبي%20(Mini-Projet%20de%20Synthèse).md)
  17. [الأسبوع 17: التقييم التحصيلي والامتحان النهائي للمقياس](./MQ1_Elaboration_des_algorithmes_simples/Lessons/17%20-%20التقييم%20التحصيلي%20والامتحان%20النهائي%20للمقياس%20(Évaluation%20Sommative).md)

---

#### ب. مقياس MQ3: البرمجة بلغة إجرائية C++ (Partie 1)
* **الحجم الساعي:** 51 ساعة (3 ساعات أسبوعياً ورشات مخبرية 100% TP).
* **وثائق المقياس:**
  * [بطاقة تقديم المقياس الرسمية (Fiche Module)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Fiche_Module.md)
  * [التدرج البيداغوجي لـ 17 أسبوعاً (Progression)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Progression_17_Semaines.md)
* **المذكرات البيداغوجية والدروس (17 درساً مكتملاً مع الأكواد التنفيذية):**
  1. [الأسبوع 01: تثبيت بيئة التطوير C++ وإعداد المشروع الأول](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/01%20-%20تثبيت%20بيئة%20التطوير%20C++%20وإعداد%20المشروع%20الأول.md)
  2. [الأسبوع 02: البنية العامة لبرنامج C++ ومكتبات الإدخال والإخراج](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/02%20-%20البنية%20العامة%20لبرنامج%20C++%20ومكتبات%20الإدخال%20والإخراج.md)
  3. [الأسبوع 03: أنواع المعطيات الأساسية، المتغيرات، والثوابت](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/03%20-%20أنواع%20المعطيات%20الأساسية،%20المتغيرات،%20والثوابت.md)
  4. [الأسبوع 04: المعاملات الحسابية، المنطقية، وأولويات العمليات](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/04%20-%20المعاملات%20الحسابية،%20المنطقية،%20وأولويات%20العمليات.md)
  5. [الأسبوع 05: تنسيق المخرجات باستخدام مكتبة iomanip](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/05%20-%20تنسيق%20المخرجات%20باستخدام%20مكتبة%20iomanip.md)
  6. [الأسبوع 06: البنية الشرطية البسيطة والبديلة (if / else)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/06%20-%20البنية%20الشرطية%20البسيطة%20والبديلة%20(if%20%20else).md)
  7. [الأسبوع 07: الشروط المركبة والتفرع المتعدد (if ... else if)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/07%20-%20الشروط%20المركبة%20والتفرع%20المتعدد%20(if%20...%20else%20if).md)
  8. [الأسبوع 08: بنية الاختيار المتعدد (switch ... case)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/08%20-%20بنية%20الاختيار%20المتعدد%20(switch%20...%20case).md)
  9. [الأسبوع 09: التكرار بعداد محدد: حلقة (for)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/09%20-%20التكرار%20بعداد%20محدد%20حلقة%20(for).md)
  10. [الأسبوع 10: التكرار بالشرط القبلي: حلقة (while)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/10%20-%20التكرار%20بالشرط%20القبلي%20حلقة%20(while).md)
  11. [الأسبوع 11: التكرار بالشرط البعدي: حلقة (do ... while)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/11%20-%20التكرار%20بالشرط%20البعدي%20حلقة%20(do%20...%20while).md)
  12. [الأسبوع 12: تعليمات التحكم في الحلقات (break و continue)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/12%20-%20تعليمات%20التحكم%20في%20الحلقات%20(break%20و%20continue).md)
  13. [الأسبوع 13: مقدمة إلى الدوال: التصريح والتعريف والإجراءات](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/13%20-%20مقدمة%20إلى%20الدوال%20(Fonctions)%20التصريح%20والتعريف.md)
  14. [الأسبوع 14: الدوال ذات القيمة المرجعة وتمرير الوسائط](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/14%20-%20الدوال%20ذات%20القيمة%20المرجعة%20(return)%20والوسائط.md)
  15. [الأسبوع 15: نطاق المتغيرات والتحميل الزائد للدوال (Surcharge)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/15%20-%20نطاق%20المتغيرات%20والتحميل%20الزائد%20للدوال%20(Surcharge).md)
  16. [الأسبوع 16: مشروع تطبيقي تركيبي مخبري (نظام إدارة مداولات)](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/16%20-%20مشروع%20تطبيقي%20تركيبي%20مخبري%20(Mini-Projet%20C++).md)
  17. [الأسبوع 17: التقييم التحصيلي والامتحان المخبري النهائي](./MQ3_Programmation_avec_un_langage_procedural_Part1/Lessons/17%20-%20التقييم%20التحصيلي%20والامتحان%20المخبري%20النهائي.md)

---

#### ج. مقياس MQ8: صيانة منصب العمل (Maintenance d'un poste de travail)
* **الحجم الساعي:** 85 ساعة (5 ساعات أسبوعياً ورشات عملية 100% TP).
* [بطاقة المقياس الرسمية](./MQ8_Maintenance_d_un_poste_de_travail/Fiche_Module.md) | [التدرج البيداغوجي لـ 17 أسبوعاً](./MQ8_Maintenance_d_un_poste_de_travail/Progression_17_Semaines.md)

---

### 2. المقاييس المكملة (Modules Complémentaires)
* **MC4: بنية وهندسة الحواسيب (68H):**  
  [بطاقة المقياس](./MC4_Architecture_des_ordinateurs/Fiche_Module.md) | [التدرج لـ 17 أسبوعاً](./MC4_Architecture_des_ordinateurs/Progression_17_Semaines.md)
* **MC8: ملفات المعطيات الكلاسيكية (68H):**  
  [بطاقة المقياس](./MC8_Fichier/Fiche_Module.md) | [التدرج لـ 17 أسبوعاً](./MC8_Fichier/Progression_17_Semaines.md)
* **MC1: اللغة الإنجليزية التقنية - الجزء 1 (51H):**  
  [بطاقة المقياس](./MC1_Anglais_Part1/Fiche_Module.md) | [التدرج لـ 17 أسبوعاً](./MC1_Anglais_Part1/Progression_17_Semaines.md)
* **MC2: تقنيات التعبير والتحرير المهني - الجزء 1 (51H):**  
  [بطاقة المقياس](./MC2_Technique_d_expression_Part1/Fiche_Module.md) | [التدرج لـ 17 أسبوعاً](./MC2_Technique_d_expression_Part1/Progression_17_Semaines.md)
* **MC11: رياضيات الإعلام الآلي - الجزء 1 (51H):**  
  [بطاقة المقياس](./MC11_Mathematiques_Part1/Fiche_Module.md) | [التدرج لـ 17 أسبوعاً](./MC11_Mathematiques_Part1/Progression_17_Semaines.md)
"""

index_path.write_text(index_content, encoding="utf-8")
print("Semester 1 Master Index generated successfully.")
