# -*- coding: utf-8 -*-
"""
Generate complete lessons 01 to 17 for MQ3 (Programmation procédurale C++ - Part 1)
Strictly following the APC model in Arabic with complete runnable C++ code.
"""
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent / "INT1204 - Programmation BT"
LESSONS_DIR = BASE_DIR / "SEMESTRE_1" / "MQ3_Programmation_avec_un_langage_procedural_Part1" / "Lessons"
LESSONS_DIR.mkdir(parents=True, exist_ok=True)

lessons_data = [
    {
        "num": "01",
        "title": "تثبيت بيئة التطوير C++ وإعداد المشروع الأول",
        "competence": "أن يكون المتربص قادراً على تثبيت بيئة التطوير المتكاملة (IDE) وإعداد مشروع برمجي جديد وكتابة وترجمة وتنفيذ أول برنامج بلغة C++ بنجاح.",
        "savoir": "أن يحدد دور المحرر، المترجم (Compiler)، الرابط (Linker)، والمنفذ في دورة حياة البرنامج.",
        "savoir_faire": "تثبيت البرنامج، إنشاء ملف مصدر .cpp، ترجمته وتنفيذه وفحص مخرجات شاشة الكونسول.",
        "savoir_etre": "احترام خطوات العمل المنهجية وتفادي تسمية الملفات والمجلدات بالحروف الخاصة أو المسافات.",
        "situation": "بصفتك مبرمجاً جديداً في مؤسسة، يطلب منك إعداد بيئة العمل على حاسوبك وبناء أول برنامج ترحيبي بالشركة لاختبار جاهزية المترجم.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    // طباعة رسالة ترحيبية
    cout << "مرحبا بكم في عالم البرمجة بلغة C++!" << endl;
    cout << "Bienvenue dans le monde du C++ !" << endl;
    cout << "Specialite : INT1204 - Programmation BT" << endl;
    
    return 0;
}"""
    },
    {
        "num": "02",
        "title": "البنية العامة لبرنامج C++ ومكتبات الإدخال والإخراج",
        "competence": "أن يتقن المتربص البنية النمطية لبرنامج C++، وفهم دور الدالة الرئيسية main وتوظيف كائنات الإدخال والإخراج القياسية (cin و cout).",
        "savoir": "أن يشرح التوجيهات للمترجم (#include)، وفضاء الأسماء (namespace std)، وعلامة نهاية التعليمة (;).",
        "savoir_faire": "كتابة برنامج تفاعلي يطبع رسائل واضحة ويستقبل مدخلات المستخدم من لوحة المفاتيح عبر cin.",
        "savoir_etre": "تنظيم أسطر الكود واستخدام الإزاحة المعيارية (Indentation) للوضوح البصري.",
        "situation": "تصميم شاشة ترحيبية بنظام تسجيل تطلب من المستخدم إدخال اسمه وعمره، ثم ترحب به رسمياً.",
        "tp_code": """#include <iostream>
#include <string>

using namespace std;

int main() {
    string nom;
    int age;

    cout << "=== استمارة التسجيل الأولية ===" << endl;
    cout << "الرجاء إدخال اسمك الكامل: ";
    cin >> nom;

    cout << "الرجاء إدخال عمرك: ";
    cin >> age;

    cout << "\nأهلاً وسهلاً بك يا " << nom << "!" << endl;
    cout << "عمرك المسجل هو: " << age << " سنة." << endl;

    return 0;
}"""
    },
    {
        "num": "03",
        "title": "أنواع المعطيات الأساسية، المتغيرات، والثوابت",
        "competence": "أن يكون المتربص قادراً على التصريح بالمتغيرات واستخدام الأنواع القياسية (int, float, double, char, bool) والكلمة المفتاحية const لتفادي الهدر التخزيني.",
        "savoir": "تحديد الحجم التخزيني في الذاكرة لكل نوع ومجال القيم المسموح بها ومفهوم الثابت const.",
        "savoir_faire": "التصريح بالمتغيرات مع الإسناد الابتدائي وتجنب أخطاء تداخل الأنواع.",
        "savoir_etre": "اختيار أسماء متغيرات ذات دلالة واضحة (Noms significatifs) باللغة الإنجليزية أو الفرنسية.",
        "situation": "في متجر إلكتروني، نريد تخزين: معرّف السلعة، سعرها، نسبة التخفيض الثابتة 15%، الحرف الدال على المقاس، وهل المنتج متوفر في المخزن.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    // تعريف الثوابت
    const float TAUX_REDUCTION = 0.15f;

    // التصريح بالمتغيرات
    int idProduit = 1054;
    double prixInitial = 4500.50;
    char taille = 'L';
    bool enStock = true;

    // حساب السعر النهائي بعد التخفيض
    double prixFinal = prixInitial * (1.0 - TAUX_REDUCTION);

    cout << "معرف السلعة: " << idProduit << endl;
    cout << "السعر الأولي: " << prixInitial << " DA" << endl;
    cout << "المقاس: " << taille << endl;
    cout << "السعر بعد تخفيض 15%: " << prixFinal << " DA" << endl;
    cout << "حالة التوفر: " << (enStock ? "متوفر" : "غير متوفر") << endl;

    return 0;
}"""
    },
    {
        "num": "04",
        "title": "المعاملات الحسابية، المنطقية، وأولويات العمليات",
        "competence": "أن يتحكم المتربص في تطبيق العمليات الحسابية (+, -, *, /, %) وعمليات الزيادة والنقصان (++ و --) والمعاملات المنطقية وأولويات الحساب في تعبير معقد.",
        "savoir": "التمييز بين القسمة الصحيحة للعدد الصحيح والقسمة العشرية، ومفهوم باقي القسمة (Modulo %).",
        "savoir_faire": "كتابة معادلات رياضية معقدة بالصيغة البرمجية الصحيحة وضبط الأقواس لحماية الأولويات.",
        "savoir_etre": "الحرص على تفادي القسمة على الصفر التي تؤدي لانهيار البرنامج (Crash).",
        "situation": "تطوير برنامج لتحويل مدة زمنية معطاة بالثواني إلى صيغة (ساعات، دقائق، ثواني) باستعمال المعاملين / و %.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    int totalSecondes, heures, minutes, secondes;

    cout << "أدخل المدة الإجمالية بالثواني: ";
    cin >> totalSecondes;

    heures = totalSecondes / 3600;
    int reste = totalSecondes % 3600;
    minutes = reste / 60;
    secondes = reste % 60;

    cout << "الوقت المكافئ هو: " 
         << heures << " ساعة و " 
         << minutes << " دقيقة و " 
         << secondes << " ثانية." << endl;

    return 0;
}"""
    },
    {
        "num": "05",
        "title": "تنسيق المخرجات باستخدام مكتبة iomanip",
        "competence": "أن يكون المتربص قادراً على تنسيق مخرجات الأرقام والجداول على الشاشة باستخدام دوال مكتبة <iomanip> (setprecision, fixed, setw, setfill).",
        "savoir": "أن يوضح وظيفة المنسقات المنهجية للتدفق (Manipulateurs de flux) في ضبط عرض الأعمدة ودقة الفواصل العشرية.",
        "savoir_faire": "تصميم جدول فاتورة أنيق ومتناسق الأعمدة كأنه مطبوع في برنامج محاسبي رسمي.",
        "savoir_etre": "العناية بالمظهر الجمالي والاحترافي للواجهة النصية وراحة المستخدم.",
        "situation": "طباعة كشف نقاط تلميذ أو فاتورة مبيعات حيث يجب أن تظهر الأسعار برقمين دقيقين بعد الفاصلة ومحاذاة الأعمدة بشكل متناسق.",
        "tp_code": """#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    cout << "=== فاتورة مبيعات منسقة ===" << endl;
    cout << left << setw(15) << "Désignation" 
         << right << setw(10) << "Quantité" 
         << setw(15) << "Prix Unitaire" 
         << setw(15) << "Total HT" << endl;
    cout << string(55, '-') << endl;

    cout << fixed << setprecision(2);

    cout << left << setw(15) << "Clavier USB" 
         << right << setw(10) << 3 
         << setw(15) << 1200.50 
         << setw(15) << (3 * 1200.50) << endl;

    cout << left << setw(15) << "Souris Optique" 
         << right << setw(10) << 5 
         << setw(15) << 650.00 
         << setw(15) << (5 * 650.00) << endl;

    return 0;
}"""
    },
    {
        "num": "06",
        "title": "البنية الشرطية البسيطة والبديلة (if / else)",
        "competence": "أن يكون المتربص قادراً على برمجة اتخاذ القرار في C++ باستخدام تعليمة if البسيطة وتعليمة if ... else البديلة مع شروط المقارنة.",
        "savoir": "أن يشرح بنية جملة if، وتقييم الشرط المنطقي كقيمة حقيقية (True / 1) أو خاطئة (False / 0).",
        "savoir_faire": "كتابة برنامج يفحص قابلية قسمة عددين، أو التحقق من كلمة مرور رقمية.",
        "savoir_etre": "وضع الأقواس المعقوفة {} دائماً لحصر كتل التعليمات التابعة للشروط حتى لو كانت تعليمة واحدة.",
        "situation": "فحص رصيد بنكي قبل إتمام عملية السحب: إذا كان الرصيد كافياً يتم الخصم، وإلا يطبع البرنامج رسالة 'رصيدك غير كافٍ'.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    double solde = 25000.0;
    double montantRetrait;

    cout << "رصيدك الحالي هو: " << solde << " DA" << endl;
    cout << "أدخل المبلغ المراد سحبه: ";
    cin >> montantRetrait;

    if (montantRetrait > 0 && montantRetrait <= solde) {
        solde -= montantRetrait;
        cout << "تمت العملية بنجاح! تفضل استلم نقودك." << endl;
        cout << "الرصيد المتبقي: " << solde << " DA" << endl;
    } else {
        cout << "خطأ: المبلغ المطلوب غير صالح أو يتجاوز رصيدك الحالي!" << endl;
    }

    return 0;
}"""
    },
    {
        "num": "07",
        "title": "الشروط المركبة والتفرع المتعدد (if ... else if)",
        "competence": "أن يتقن المتربص هيكلة القرارات ذات الحالات المتعددة باستخدام if ... else if والشروط المنطقية المركبة بواسطة (&&, ||, !).",
        "savoir": "تحديد جدول الحقيقة لروابط المعاملات المنطقية وقواعد تقييم المسار القصير (Short-circuit evaluation).",
        "savoir_faire": "برمجة تصنيف المتربصين وتحديد الملاحظات التقديرية بدقة بناءً على العلامة.",
        "savoir_etre": "ترتيب الشروط منطقياً من الأكثر تحديداً إلى الأعم لتفادي تجاهل الحالات الخاصة.",
        "situation": "نظام جامعي لتحديد التقدير الرسمي: ممتاز (>= 16)، جيد جداً (>= 14)، جيد (>= 12)، مقبول (>= 10)، وراسب (< 10).",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    float note;
    cout << "أدخل معدل المتربص (من 0 إلى 20): ";
    cin >> note;

    if (note < 0 || note > 20) {
        cout << "خطأ: المعدل يجب أن يكون بين 0 و 20!" << endl;
    } else if (note >= 16) {
        cout << "التقدير: ممتاز (Mention Très Bien)" << endl;
    } else if (note >= 14) {
        cout << "التقدير: جيد (Mention Bien)" << endl;
    } else if (note >= 12) {
        cout << "التقدير: قريب من الجيد (Mention Assez Bien)" << endl;
    } else if (note >= 10) {
        cout << "التقدير: مقبول (Mention Passable)" << endl;
    } else {
        cout << "النتيجة: مؤجل / راسب (Ajourné)" << endl;
    }

    return 0;
}"""
    },
    {
        "num": "08",
        "title": "بنية الاختيار المتعدد (switch ... case)",
        "competence": "أن يكون المتربص قادراً على برمجة قوائم الخيارات التفاعلية باستخدام بنية switch ... case والتحكم بتعليمة break والقسم الافتراضي default.",
        "savoir": "شروط استخدام switch (أن يكون المتغير من نوع صحيح int أو حرفي char حصراً) ودور تعليمة break الإلزامية.",
        "savoir_faire": "بناء آلة حاسبة إلكترونية متكاملة تقوم بالعمليات الحسابية الأساسية بناءً على رمز العملية المدخل.",
        "savoir_etre": "عدم نسيان حالة default لمعالجة الخيارات الخاطئة بلباقة واحترافية.",
        "situation": "تصميم آلة حاسبة بسيطة تطلب من المستخدم إدخال عددين ورمز العملية الحسابية (+, -, *, /) ثم تطبع النتيجة الدقيقة.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    double a, b;
    char operation;

    cout << "أدخل العدد الأول: ";
    cin >> a;
    cout << "أدخل رمز العملية (+, -, *, /): ";
    cin >> operation;
    cout << "أدخل العدد الثاني: ";
    cin >> b;

    switch (operation) {
        case '+':
            cout << "النتيجة: " << a << " + " << b << " = " << (a + b) << endl;
            break;
        case '-':
            cout << "النتيجة: " << a << " - " << b << " = " << (a - b) << endl;
            break;
        case '*':
            cout << "النتيجة: " << a << " * " << b << " = " << (a * b) << endl;
            break;
        case '/':
            if (b != 0)
                cout << "النتيجة: " << a << " / " << b << " = " << (a / b) << endl;
            else
                cout << "خطأ رياضي: لا يمكن القسمة على الصفر!" << endl;
            break;
        default:
            cout << "خطأ: رمز العملية غير معروف!" << endl;
            break;
    }

    return 0;
}"""
    },
    {
        "num": "09",
        "title": "التكرار بعداد محدد: حلقة (for)",
        "competence": "أن يتقن المتربص برمجة الحلقات المحددة التكرار لعدد معلوم من المرات باستخدام حلقة for وعداد الحلقة، وتوظيفها في العمليات التراكمية.",
        "savoir": "فهم الأقسام الثلاثة لتعليمة for: (التهيئة؛ الشرط؛ خطوة التحديث).",
        "savoir_faire": "كتابة برامج لحساب مجموع المتتاليات، جداول الضرب، وحساب القوى ومضروب الأعداد.",
        "savoir_etre": "تفادي الحلقات المفرغة أو كتابة شروط توقف مستحيلة التحقق.",
        "situation": "حساب مضروب عدد طبيعي N (Factorielle : N!) المدخل من المستخدم وطباعة خطوات الضرب خطوة بخطوة.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    int n;
    long long factorielle = 1;

    cout << "أدخل عدداً صحيحاً موجباً لحساب مضروبه: ";
    cin >> n;

    if (n < 0) {
        cout << "خطأ: المضروب غير معرف للأعداد السالبة!" << endl;
    } else {
        for (int i = 1; i <= n; i++) {
            factorielle *= i;
        }
        cout << n << "! = " << factorielle << endl;
    }

    return 0;
}"""
    },
    {
        "num": "10",
        "title": "التكرار بالشرط القبلي: حلقة (while)",
        "competence": "أن يكون المتربص قادراً على كتابة حلقات التكرار المشروط مسبقاً (while) لفحص صحة مدخلات المستخدم وتنفيذ خوارزميات التقارب التكراري.",
        "savoir": "أن يشرح آلية التحقق من الشرط قبل دخول الحلقة وإمكانية عدم تنفيذها مطلقاً إذا كان الشرط غير محقق من البداية.",
        "savoir_faire": "برمجة قفل أمني يطلب كلمة مرور صحيحة ويسمح بـ 3 محاولات فقط قبل غلق النظام.",
        "savoir_etre": "الحذر التام من الحلقات اللانهائية وتحديث متغير التحكم داخل جسم الحلقة.",
        "situation": "نظام تسجيل يرفض قبول أي علامة سالبة أو تفوق 20 ويظل يطلب إدخال علامة صحيحة، مع إمكانية إدخال 999 للخروج.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    float note;

    cout << "أدخل علامة صحيحة محصورة بين 0 و 20: ";
    cin >> note;

    while (note < 0 || note > 20) {
        cout << "قيمة غير مقبولة! أعد الإدخال (0 إلى 20): ";
        cin >> note;
    }

    cout << "تم قبول العلامة بنجاح: " << note << " / 20" << endl;

    return 0;
}"""
    },
    {
        "num": "11",
        "title": "التكرار بالشرط البعدي: حلقة (do ... while)",
        "competence": "أن يتقن المتربص استخدام حلقة do ... while التي تضمن تنفيذ جسم التكرار لمرة واحدة على الأقل قبل فحص شرط الاستمرار، وبرمجة القوائم التكرارية.",
        "savoir": "التمييز بين while و do ... while من حيث لحظة فحص الشرط وضرورة وضع الفاصلة المنقوطة في نهاية do ... while;",
        "savoir_faire": "بناء برنامج تفاعلي يعرض قائمة خدمات ويعيد تكرارها حتى يختار المستخدم صراحة خيار الخروج (Exit).",
        "savoir_etre": "تقديم تجربة استخدام مرنة تسمح للمستخدم بإجراء عدة عمليات متتالية دون إعادة فتح البرنامج.",
        "situation": "بناء نظام صراف تفاعلي يسمح للمستخدم بإجراء عدة عمليات إيداع وسحب متتالية، ولا يتوقف إلا إذا اختار خيار الخروج.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    int choix;
    double solde = 50000.0;

    do {
        cout << "\n=== قائمة الخدمات المصرفية ===" << endl;
        cout << "1. الاطلاع على الرصيد" << endl;
        cout << "2. إيداع أموال" << endl;
        cout << "3. سحب أموال" << endl;
        cout << "4. إنهاء العملية والخروج" << endl;
        cout << "أدخل اختيارك (1-4): ";
        cin >> choix;

        switch (choix) {
            case 1:
                cout << "رصيدك الحالي هو: " << solde << " DA" << endl;
                break;
            case 2: {
                double depot;
                cout << "المبلغ المراد إيداعه: ";
                cin >> depot;
                if (depot > 0) {
                    solde += depot;
                    cout << "تم الإيداع بنجاح! الرصيد الجديد: " << solde << " DA" << endl;
                }
                break;
            }
            case 3: {
                double retrait;
                cout << "المبلغ المراد سحبه: ";
                cin >> retrait;
                if (retrait > 0 && retrait <= solde) {
                    solde -= retrait;
                    cout << "تم السحب بنجاح! الرصيد الجديد: " << solde << " DA" << endl;
                } else {
                    cout << "خطأ: الرصيد غير كافٍ!" << endl;
                }
                break;
            }
            case 4:
                cout << "شكراً لتعاملكم معنا. إلى اللقاء!" << endl;
                break;
            default:
                cout << "خيار غير صالح! الرجاء الاختيار من 1 إلى 4." << endl;
        }
    } while (choix != 4);

    return 0;
}"""
    },
    {
        "num": "12",
        "title": "تعليمات التحكم في الحلقات (break و continue)",
        "competence": "أن يكون المتربص قادراً على التحكم في انسياب الحلقات بالخروج الفوري (break) أو تخطي الدورة الحالية (continue) لرفع كفاءة المعالجة.",
        "savoir": "شرح الفرق بين إنهاء الحلقة تماماً بـ break وتجاوز التعليمات المتبقية في الدورة الحالية بـ continue.",
        "savoir_faire": "تطبيق تعليمات التحكم في البحث عن رقم، وتخطي الأعداد السالبة عند جمع مجموعة قيم.",
        "savoir_etre": "عدم الإفراط في استخدام break لضمان بقاء منطق الكود مقروءاً ومحكماً.",
        "situation": "جمع 5 أعداد موجبة يدخلها المستخدم: إذا أدخل المستخدم رقماً سالباً يتم تجاهله وتخطيه، وإذا أدخل 0 يتوقف البرنامج فوراً.",
        "tp_code": """#include <iostream>

using namespace std;

int main() {
    int somme = 0;
    int nombre;

    cout << "أدخل أعداداً موجبة لجمعها (أدخل 0 للتوقف الفوري):" << endl;

    for (int i = 1; i <= 10; i++) {
        cout << "العدد رقم " << i << ": ";
        cin >> nombre;

        if (nombre == 0) {
            cout << "تم إدخال 0: إيقاف الحلقة فوراً عبر break." << endl;
            break;
        }

        if (nombre < 0) {
            cout << "عدد سالب! سيتم تجاهله عبر continue ولن يضاف للمجموع." << endl;
            continue;
        }

        somme += nombre;
    }

    cout << "المجموع النهائي للأعداد الموجبة المقبولة: " << somme << endl;

    return 0;
}"""
    },
    {
        "num": "13",
        "title": "مقدمة إلى الدوال (Fonctions): التصريح والتعريف",
        "competence": "أن يكون المتربص قادراً على تقسيم البرنامج الضخم إلى وحدات برمجية مستقلة عبر التصريح بالدوال الإجرائية (void) واستدعائها.",
        "savoir": "مفهوم البرمجة المعيارية (Modular programming)، نموذج الدالة (Prototype)، وجسم التعريف (Corps).",
        "savoir_faire": "كتابة واستدعاء دوال تقوم بطباعة خطوط الزخرفة، شاشات الترحيب، وقوائم الخيارات.",
        "savoir_etre": "إعادة استخدام الأكواد (Code reuse) وتفادي تكرار نفس الأسطر في عدة أماكن.",
        "situation": "تصميم برنامج يحتاج لطباعة ترويسة مزخرفة للشركة وخط فاصل متطابق في عدة مراحل من التنفيذ دون إعادة كتابتها.",
        "tp_code": """#include <iostream>

using namespace std;

// 1. التصريح بالدوال (Prototypes)
void afficherEnTete();
void dessinerLigne(int longueur, char motif);

int main() {
    afficherEnTete();
    cout << "البرنامج الرئيسي يعمل بنجاح." << endl;
    dessinerLigne(40, '=');
    cout << "نهاية المهمة الأولى." << endl;
    dessinerLigne(40, '-');

    return 0;
}

// 2. تعريف الدوال (Définition)
void afficherEnTete() {
    dessinerLigne(45, '*');
    cout << "*  Institut National de Formation Professionnelle  *" << endl;
    cout << "*        INT1204 - Developpement C++         *" << endl;
    dessinerLigne(45, '*');
}

void dessinerLigne(int longueur, char motif) {
    for (int i = 0; i < longueur; i++) {
        cout << motif;
    }
    cout << endl;
}"""
    },
    {
        "num": "14",
        "title": "الدوال ذات القيمة المرجعة (return) والوسائط",
        "competence": "أن يتقن المتربص إنشاء واستدعاء دوال تعيد قيمة معالجة (return) وتمرير المعاملات بالقيمة (Passage par valeur).",
        "savoir": "تحديد النوع المرجع للدالة، آلية عمل تعليمة return، والنسخ المستقل للوسائط في الذاكرة.",
        "savoir_faire": "برمجة دوال رياضية لحساب المساحات، القوة، وإيجاد العدد الأكبر بين قيمتين.",
        "savoir_etre": "جعل كل دالة تنجز مهمة محددة بدقة (Single Responsibility Principle).",
        "situation": "بناء مكتبة دوال حسابية تتضمن دالة لحساب مساحة المثلث ودالة لفحص هل العدد أولي أم لا.",
        "tp_code": """#include <iostream>

using namespace std;

// دالة لحساب القيمة العظمى
int trouverMax(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

// دالة لحساب مربع عدد
double calculerCarre(double x) {
    return x * x;
}

// دالة لفحص هل العدد زوجي
bool estPair(int n) {
    return (n % 2 == 0);
}

int main() {
    int x = 25, y = 42;
    cout << "أكبر قيمة بين " << x << " و " << y << " هي: " << trouverMax(x, y) << endl;

    double val = 7.5;
    cout << "مربع " << val << " هو: " << calculerCarre(val) << endl;

    int num = 18;
    cout << "هل العدد " << num << " زوجي؟ " << (estPair(num) ? "نعم" : "لا") << endl;

    return 0;
}"""
    },
    {
        "num": "15",
        "title": "نطاق المتغيرات والتحميل الزائد للدوال (Surcharge)",
        "competence": "أن يكون المتربص قادراً على التمييز بين المتغيرات المحلية (Local) والعامة (Global) واستخدام ميزة التحميل الزائد للدوال (Function Overloading).",
        "savoir": "مفهوم مدى حياة المتغير (Scope & Lifetime) وقواعد تمييز الدوال المحملة عبر بصمة الوسائط (Signature).",
        "savoir_faire": "إنشاء عدة دوال بنفس الاسم تجمع أعداداً صحيحة، أو أعداداً عشرية، أو تطبع أنواعاً مختلفة.",
        "savoir_etre": "تفادي الاستخدام العشوائي للمتغيرات العامة لحماية البيانات من التعديلات غير المقصودة.",
        "situation": "تطوير دالة حسابية باسم additionner تقبل جمع عددين صحيحين، أو جمع عددين حقيقيين، أو جمع ثلاثة أعداد بنفس الاسم.",
        "tp_code": """#include <iostream>

using namespace std;

// متغير عام (Variable Globale)
int compteurAppels = 0;

// التحميل الزائد للدوال (Surcharge des fonctions)
int additionner(int a, int b) {
    compteurAppels++;
    return a + b;
}

double additionner(double a, double b) {
    compteurAppels++;
    return a + b;
}

int additionner(int a, int b, int c) {
    compteurAppels++;
    return a + b + c;
}

int main() {
    cout << "جمع عددين صحيحين: " << additionner(10, 20) << endl;
    cout << "جمع عددين عشريين: " << additionner(12.5, 7.3) << endl;
    cout << "جمع ثلاثة أعداد: " << additionner(5, 15, 25) << endl;
    
    cout << "إجمالي عدد مرات استدعاء الدوال: " << compteurAppels << endl;

    return 0;
}"""
    },
    {
        "num": "16",
        "title": "مشروع تطبيقي تركيبي مخبري (Mini-Projet C++)",
        "competence": "أن يدمج المتربص المكتسبات المعرفية والعملية للسداسي الأول في بناء برنامج C++ متكامل ومنظم باستخدام الدوال والقوائم والشروط.",
        "savoir": "ربط المفاهيم الإجرائية وهندسة البرنامج التفاعلي وفق المواصفات التقنية.",
        "savoir_faire": "تطوير نظام إدارة نقاط ومداولات لفوج دراسي: إدخال الأسماء والمعدلات، حساب الإحصائيات، وعرض النتائج.",
        "savoir_etre": "تنظيم الكود وتوثيقه، والتعامل الاحترافي مع أخطاء الإدخال المحتملة.",
        "situation": "طلب مشروع برمجي كامل في نهاية السداسي لإدارة مداولات قسم دراسي في C++ مع إمكانية حساب أعلى وأدنى معدل ونسبة النجاح.",
        "tp_code": """#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

const int MAX = 20;

void afficherMenu() {
    cout << "\n========================================" << endl;
    cout << "   نظام إدارة المداولات المدرسية C++   " << endl;
    cout << "========================================" << endl;
    cout << "1. إدخال بيانات المتربصين" << endl;
    cout << "2. عرض كشف النقاط الإجمالي" << endl;
    cout << "3. عرض الإحصائيات (المعدل العام، أعلى وأدنى علامة)" << endl;
    cout << "4. إنهاء البرنامج" << endl;
    cout << "اختر عملية (1-4): ";
}

int main() {
    string noms[MAX];
    float notes[MAX];
    int nbStagiaires = 0;
    int choix;

    do {
        afficherMenu();
        cin >> choix;

        switch (choix) {
            case 1: {
                cout << "كم عدد المتربصين المراد تسجيلهم؟ ";
                cin >> nbStagiaires;
                for (int i = 0; i < nbStagiaires; i++) {
                    cout << "اسم المتربص [" << (i + 1) << "]: ";
                    cin >> noms[i];
                    do {
                        cout << "معدل المتربص (0 إلى 20): ";
                        cin >> notes[i];
                    } while (notes[i] < 0 || notes[i] > 20);
                }
                cout << "تم تسجيل البيانات بنجاح!" << endl;
                break;
            }
            case 2: {
                if (nbStagiaires == 0) {
                    cout << "تنبيه: لم يتم إدخال بيانات بعد!" << endl;
                } else {
                    cout << "\n" << left << setw(10) << "الرقم" 
                         << setw(20) << "الاسم" 
                         << setw(10) << "المعدل" 
                         << setw(15) << "الملاحظة" << endl;
                    cout << string(55, '-') << endl;
                    for (int i = 0; i < nbStagiaires; i++) {
                        cout << left << setw(10) << (i + 1)
                             << setw(20) << noms[i]
                             << setw(10) << fixed << setprecision(2) << notes[i]
                             << setw(15) << (notes[i] >= 10.0 ? "ناجح" : "راسب") << endl;
                    }
                }
                break;
            }
            case 3: {
                if (nbStagiaires == 0) {
                    cout << "تنبيه: لا توجد بيانات لحساب الإحصائيات!" << endl;
                } else {
                    float somme = 0, maxNote = notes[0], minNote = notes[0];
                    int admis = 0;
                    for (int i = 0; i < nbStagiaires; i++) {
                        somme += notes[i];
                        if (notes[i] > maxNote) maxNote = notes[i];
                        if (notes[i] < minNote) minNote = notes[i];
                        if (notes[i] >= 10.0) admis++;
                    }
                    cout << "\n=== إحصائيات الفوج ===" << endl;
                    cout << "المعدل العام للقسم: " << (somme / nbStagiaires) << " / 20" << endl;
                    cout << "أعلى علامة مسجلة: " << maxNote << endl;
                    cout << "أدنى علامة مسجلة: " << minNote << endl;
                    cout << "نسبة النجاح: " << ((float)admis / nbStagiaires * 100.0) << "%" << endl;
                }
                break;
            }
            case 4:
                cout << "تم إنهاء البرنامج. بالتوفيق!" << endl;
                break;
            default:
                cout << "خيار غير صالح!" << endl;
        }
    } while (choix != 4);

    return 0;
}"""
    },
    {
        "num": "17",
        "title": "التقييم التحصيلي والامتحان المخبري النهائي",
        "competence": "التحقق النهائي والموضوعي من اكتساب المتربص للكفاءة المعيارية الخاصة بالبرمجة الإجرائية C++ تحت ظروف الامتحان المخبري.",
        "savoir": "الإجابة عن الأسئلة التقنية حول بنية C++ والأنواع والدوال وتتبع الذاكرة.",
        "savoir_faire": "كتابة وتصحيح وتنفيذ برنامج C++ كامل على الحاسوب في المخبر يلبي مسألة حقيقية في زمن محدد.",
        "savoir_etre": "الهدوء، تنظيم ملف المشروع، وتسليم الكود المصدري النظيف في الوقت المحدد.",
        "situation": "الامتحان المخبري الرسمي لإنهاء مقياس C++ (الجزء الأول): مسألة تتضمن القوائم، الشروط، الحلقات، والدوال الحسابية.",
        "tp_code": """// موضوع الامتحان المخبري للسداسي الأول:
المطلوب إنجاز برنامج C++ كامل يحتوي على:
1. دالة ترحيبية وقائمة خدمات متعددة الخيارات (switch).
2. دالة لحساب ضريبة الدخل الإجمالي (IRG) وفق سلم الأجور.
3. حلقة تكرارية لفحص صحة مدخلات المستخدم واستبعاد القيم السالبة.
4. طباعة جدول النتائج منسقاً بدقة باستخدام مكتبة <iomanip>."""
    }
]

def generate_lesson_md(data):
    num = data["num"]
    title = data["title"]
    comp = data["competence"]
    savoir = data["savoir"]
    savoir_faire = data["savoir_faire"]
    savoir_etre = data["savoir_etre"]
    situation = data["situation"]
    tp_code = data["tp_code"]

    md = f"""# بطاقة تقنية بيداغوجية (Fiche de Préparation)

## 1. معلومات عامة (Informations Générales)

| العنصر | التفاصيل |
| :--- | :--- |
| **التخصص (Spécialité)** | تقني في الإعلام الآلي - خيار برمجة (INT1204 - Programmation BT) |
| **المقياس / الوحدة (Module)** | البرمجة بلغة إجرائية C++ (MQ3 - Programmation procédurale - الجزء 1) |
| **عنوان الدرس (Titre du cours)** | {num} - {title} |
| **الأسبوع والمدة (Semaine & Durée)** | الأسبوع {num} - 3 ساعات (أعمال تطبيقية ومخبرية 3H TP) |
| **المكان (Lieu)** | مخبر البرمجة (Laboratoire Informatique) |
| **الوسائل البيداغوجية (Moyens)** | السبورة، جهاز العرض، حواسيب متصلة بشبكة، بيئة تطوير C++ (Code::Blocks / VS Code / GCC) |

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
| **1. الانطلاق والتمهيد (Mise en train)** | 10% (18 د) | يطرح التحدي البرمجي أو الوضعية المشكلة ويستذكر المفاهيم الخوارزمية المقابلة | يحلل المشكلة ويسترجع البنية الخوارزمية التي درسها في مقياس MQ1 | ربط الخوارزمية النظرية بكيفية ترجمتها وتنفيذها الفعلي في C++ |
| **2. الاستكشاف (Exploration)** | 15% (27 د) | يشرح القواعد النحوية (Syntaxe C++) الخاصة بالمفهوم، ويوضح أخطاء الترجمة الشائعة | يدون صيغة الأوامر في دفتره، ويلاحظ المثال التوضيحي المكتوب على الشاشة | الشرح المركز لأوامر C++ ومكتباتها القياسية المرتبطة بالحصة |
| **3. الإنجاز والتطبيق (Réalisation & TP)** | 60% (108 د) | يوجه المتربصين، يشرف على كتابة الأكواد على الحواسيب، ويساعد في تصحيح أخطاء المترجم (Debugging) | يكتب الكود كاملاً في بيئة التطوير، يقوم بالترجمة (Compile & Run)، ويختبر البرنامج | الورشة المخبرية: كتابة الكود وتجربته على عدة حالات ومدخلات واقعية |
| **4. الحوصلة (Synthèse)** | 15% (27 د) | يستعرض أفضل الأكواد المنجزة، ويناقش الممارسات البرمجية المثلى وحفظ المشاريع | يشارك في تحليل الأخطاء، يسجل الملاحظات الذهبية، ويحفظ مشروعه المنفذ | ترسيخ قواعد البرمجة النظيفة (Clean Code) والتحضير للدرس القادم |

---

## 4. التقييم التكويني (Évaluation Formative)

| المؤشرات وشروط النجاح (Indicateurs) | معيار القبول والتحقق (Acquis) |
| :--- | :--- |
| 1. خلو البرنامج المكتوب من أخطاء الترجمة (Compilation Errors). | نجاح عملية البناء (Build Success - 0 Errors, 0 Warnings). |
| 2. صحة المخرجات وتنفيذ البرنامج لكافة الحالات المطلوبة. | تطابق نتائج شاشة الكونسول مع القيم الحسابية الصحيحة 100%. |
| 3. كتابة شفرة مصدرية نظيفة ومنسقة ومعلقة بالكامل. | سهولة قراءة وتتبع الكود واحترام معايير التسمية والإزاحة. |

---

# محتوى الدرس للمتربصين (Contenu du Cours)

## عنوان الدرس: {title}

---

### الوضعية المشكلة (Mise en situation):
{situation}

---

### 1. المتطلبات الأساسية (Prérequis):
* المعارف الخوارزمية المكتسبة في مقياس MQ1.
* التمكن من استخدام لوحة المفاتيح والرموز البرمجية الخاصة (;, {{}}, <<, >>, //).
* بيئة العمل: حاسوب مثبت عليه بيئة تطوير C++ (IDE) مع مترجم قياسي.

---

### 2. المفاهيم الأساسية وهيكلة العمل (Concepts Clés):
* **القاعدة النحوية بلغة C++:** الالتزام الصارم ببنية الأوامر وتضمين المكتبات الرأسية المناسبة `#include`.
* **نقاط الانتباه البرمجية:**
  - حساسية اللغة لحالة الأحرف (C++ est sensible à la casse).
  - وجوب إنهاء كل تعليمة برمجية بفاصلة منقوطة `;`.
  - تنظيم الكتل البرمجية بين الحاضنتين `{{` و `}}`.

---

### 3. التطبيق العملي المخبري (Travail Pratique - TP):
> **الهدف العملي للورشة:** كتابة وترجمة واختبار كود C++ تنفيذي كامل لحل المسألة المهنية.

```cpp
{tp_code}
```

---

### 4. التنفيذ، الاختبار والتحقق (Exécution, Test & Validation):
1. **الترجمة والتشغيل (Build & Run):** اضغط على الزر المخصص (مثل F9 في Code::Blocks) وتأكد من عدم وجود أخطاء في نافذة Build log.
2. **فحص شاشة المخرجات (Console Output):** أدخل قيماً تجريبية مختلفة وتأكد من سلامة المعالجة.
3. **تمرين تطبيقي فردي للتحدي (Exercice en autonomie):** 
   قم بتعديل الكود السابق لإضافة تحسينات إضافية ومعالجة استثناءات أخرى.

---

### خلاصة الدرس (Conclusion):
تعتبر لغة C++ إحدى أقوى لغات البرمجة العالمية لسرعتها الفائقة وتحكمها المباشر في موارد العتاد؛ وكل قاعدة تتقنها اليوم تمثل رصيداً تقنياً مباشراً لمستقبلك الاحترافي كمطور برمجيات.
"""
    safe_title = "".join(c for c in title if c not in r'\/:*?"<>|')
    file_name = f"{num} - {safe_title}.md"
    file_path = LESSONS_DIR / file_name
    file_path.write_text(md, encoding="utf-8")

def main():
    for d in lessons_data:
        generate_lesson_md(d)
    print("All 17 lessons for MQ3 (C++ Part 1) generated successfully in Arabic!")

if __name__ == "__main__":
    main()
