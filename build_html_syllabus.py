# -*- coding: utf-8 -*-
"""
Interactive and Print-Ready HTML Syllabus Compiler
With 3 Dedicated Resources per Lesson:
1. 👨‍🏫 البطاقة التقنية البيداغوجية (للأستاذ)
2. 📋 مخطط درس بالمقاربة بالكفاءات (مطابق لنموذج وزارة التكوين المهني)
3. 👨‍🎓 محتوى الدرس والورشة التطبيقية (للمتربص)
All with isolated multi-page A4 printing (20mm/15mm margins) and signature blocks.
"""
import os
import glob
import json
import re
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR / "INT1204 - Programmation BT"
OUTPUT_HTML = ROOT_DIR / "منهاج_البرمجة_التفاعلي_Syllabus.html"

def extract_lesson_parts(content):
    parts = re.split(r'^#{1,3}\s*محتوى الدرس.*$', content, maxsplit=1, flags=re.MULTILINE)
    if len(parts) > 1:
        teacher_part = parts[0].strip()
        student_part = "# محتوى الدرس للمتربصين\n\n" + parts[1].strip()
    else:
        teacher_part = content.strip()
        student_part = "محتوى الدرس للمتربص غير مفصول في هذا الملف."
    return teacher_part, student_part

def generate_apc_plan_markdown(sem_name, mod_code, mod_name, w_num, title, duree_str, comp_text):
    niveau = "سنة أولى (1ère Année)" if ("الأول" in sem_name or "الثاني" in sem_name) else "سنة ثانية (2ème Année)"
    clean_duree = duree_str.split('(')[0].strip() if '(' in duree_str else duree_str
    
    return f"""<div class="country-header" style="text-align: center; margin-bottom: 1rem;">
<h2 style="text-align: center; font-size: 1.25rem; font-weight: 800; color: #0f172a; margin-bottom: 0.2rem;">الجمهورية الجزائرية الديمقراطية الشعبية</h2>
<h3 style="text-align: center; font-size: 1.05rem; font-weight: 700; color: #475569; margin-top: 0;">وزارة التكوين والتعليم المهنيين</h3>
</div>

<h3 class="plan-main-title" style="text-align: center; font-size: 1.2rem; font-weight: 800; color: #0369a1; margin-bottom: 1rem;">📋 مخطط درس بالمقاربة بالكفاءات</h3>

<div class="plan-meta-card" dir="rtl" style="direction: rtl !important; text-align: right !important; background-color: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; font-size: 0.95rem; line-height: 1.8;">
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>التخصص:</strong> تقني في الإعلام الآلي - خيار برمجة (INT1204 - BT)</div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>المستوى:</strong> تقني - {niveau}</div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>المقياس:</strong> <span dir="rtl">{mod_name} ({mod_code})</span></div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>عنوان الدرس:</strong> {w_num} - {title}</div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>المدة الزمنية:</strong> {clean_duree}</div>
  <div style="direction: rtl !important; text-align: right !important;"><strong>الكفاءة المستهدفة:</strong> {comp_text} باحترام قواعد السلامة والمعايير التقنية.</div>
</div>

---

| مراحل الدرس | نشاط الأستاذ | نشاط المتربص | الوسائل البيداغوجية | التقويم |
| :--- | :--- | :--- | :--- | :--- |
| **1- وضعية الإنطلاق** | - طرح أسئلة تمهيدية حول سياق وأهمية موضوع ({title}).<br>- عرض نموذج أو وضعية مشكلة واقعية محفزة.<br>- ربط الدرس بالممارسة اليومية في بيئة العمل البرمجية. | - الإجابة على الأسئلة التمهيدية.<br>- ملاحظة النموذج ومناقشة المعطيات.<br>- المشاركة في بناء فرضيات الحل. | - السبورة<br>- عارض البيانات (Data Show)<br>- كراس المتربص | تقويم تشخيصي / شفوي |
| **2- بناء التعلمات** | - تقديم وشرح مفاهيم ({title}) وتفكيك عناصرها المنطقية.<br>- شرح خطوات الإنجاز وتوضيح المعايير التقنية وقواعد كتابة الكود.<br>- تقديم أمثلة توضيحية ومقارنات تطبيقية. | - الاستماع والانتباه للشرح.<br>- تدوين القواعد والمصطلحات في الكراس.<br>- طرح الأسئلة وطلب التوضيحات عند الحاجة. | - جهاز العرض الرقمي<br>- وثائق تقنية ودليل المرجع<br>- بيئة التطوير والبرمجيات | أسئلة ومتابعة مرحلية |
| **3- التطبيق** | - تكليف المتربص بإنجاز خطوات الورشة التطبيقية خطوة بخطوة.<br>- تقديم التوجيهات الفردية وتصحيح الأخطاء أثناء العمل المخبري. | - تنفيذ خطوات العمل البرمجي أو الفني بدقة على الحاسوب.<br>- استعمال الأدوات والبرمجيات بطريقة صحيحة ومحترفة. | - حواسيب المخبر المتصلة بشبكة<br>- بيئة التطوير (IDE / البرمجيات المخصصة)<br>- بطاقة العمل المخبري (Fiche TP) | ملاحظة الأداء ومراقبة الكود |
| **4- التقويم النهائي** | - طرح أسئلة شفوية حول مراحل وخوارزمية الحل.<br>- تقديم تمرين عملي تطبيقي فردي لاختبار التحكم في المهارة. | - الإجابة على الأسئلة الشفوية باقتضاب ودقة.<br>- إنجاز التمرين العملي الفردي باستقلالية في الوقت المحدد. | - ورقة عمل / تمرين اختباري<br>- جهاز الحاسوب وأدوات العمل | تقويم تحصيلي فردي |
| **5- الإدماج والاستثمار** | - وضع المتربص في وضعية مهنية جديدة توظف مهارة ({title}) في مشروع متكامل.<br>- مناقشة الإنجاز وتصحيح الأخطاء واقتراح تحسينات الأداء. | - توظيف المكتسبات المعرفية والمهارية في حل الوضعية الجديدة.<br>- تقديم مقترحات لتحسين جودة الكود والعمل المنجز. | - مختلف الوسائل والبرمجيات المتاحة في المخبر | تقويم إدماجي |

---

**الخلاصة:**  
من خلال هذا الدرس، تمكن المتربص من اكتساب المعارف والمهارات المتعلقة بـ **{title}** وتوظيفها في وضعيات مهنية مختلفة مع احترام قواعد السلامة والمعايير التقنية.

---

<br>

| **التاريخ:** .................................................... | **توقيع الأستاذ:** .................................................... |
| :--- | :--- |
"""

def extract_comp_from_teacher(teacher_text):
    match = re.search(r'\*\s*\*\*الكفاءة المستهدفة[^\*]*\*\*[:\s]*([^\n\r]+)', teacher_text)
    if match:
        val = match.group(1).strip()
        # Clean up any trailing brackets
        return val.replace('[', '').replace(']', '').strip()
    return "أن يكون المتربص قادراً على إنجاز مهارات الدرس وتطبيقها عملياً"

def extract_duree_from_teacher(teacher_text):
    match = re.search(r'\*\*الأسبوع والمدة[^\*]*\*\*[:\s]*([^\n\r\|]+)', teacher_text)
    if match:
        val = match.group(1).strip()
        return val
    return "4 ساعات (2H نظري / 2H تطبيقي)"

def gather_all_data():
    data = {
        "specialty": "تقني في الإعلام الآلي - خيار برمجة (INT1204 - BT)",
        "semesters": {}
    }
    
    sem_dirs = [
        ("SEMESTRE_1", "السداسي الأول (S1)"),
        ("SEMESTRE_2", "السداسي الثاني (S2)"),
        ("SEMESTRE_3", "السداسي الثالث (S3)"),
        ("SEMESTRE_4", "السداسي الرابع (S4)"),
    ]
    
    for s_folder, s_name in sem_dirs:
        sem_path = ROOT_DIR / s_folder
        if not sem_path.exists():
            continue
            
        data["semesters"][s_folder] = {
            "name": s_name,
            "modules": {}
        }
        
        mod_dirs = [d for d in sem_path.iterdir() if d.is_dir() and (d / "Lessons").exists()]
        mod_dirs.sort(key=lambda x: x.name)
        
        for m_dir in mod_dirs:
            mod_key = m_dir.name
            mod_code = mod_key.split('_')[0]
            mod_title = mod_key.replace("_", " ")
            clean_mod_name = mod_key.replace(mod_code + '_', '').replace('_', ' ')
            
            fiche_text = ""
            fiche_file = m_dir / "Fiche_Module.md"
            if fiche_file.exists():
                fiche_text = fiche_file.read_text(encoding="utf-8")
                
            prog_text = ""
            for p_name in ["Progression_17_Semaines.md", "Progression_Semaines.md"]:
                pf = m_dir / p_name
                if pf.exists():
                    prog_text = pf.read_text(encoding="utf-8")
                    break
                    
            lessons = []
            lesson_files = sorted(list((m_dir / "Lessons").glob("*.md")), key=lambda x: x.name)
            for lf in lesson_files:
                raw_text = lf.read_text(encoding="utf-8")
                t_part, s_part = extract_lesson_parts(raw_text)
                clean_title = lf.stem
                
                # Extract week number
                w_match = re.match(r'^(\d+)', clean_title)
                w_num = w_match.group(1) if w_match else "01"
                raw_lesson_title = re.sub(r'^\d+\s*-\s*', '', clean_title)
                
                comp_text = extract_comp_from_teacher(t_part)
                duree_text = extract_duree_from_teacher(t_part)
                
                # Generate official APC Lesson Plan
                plan_part = generate_apc_plan_markdown(
                    s_name, mod_code, clean_mod_name, w_num, raw_lesson_title, duree_text, comp_text
                )
                
                lessons.append({
                    "filename": lf.name,
                    "title": clean_title,
                    "teacher": t_part,
                    "plan": plan_part,
                    "student": s_part
                })
                
            data["semesters"][s_folder]["modules"][mod_key] = {
                "title": mod_title,
                "fiche": fiche_text,
                "progression": prog_text,
                "lessons": lessons
            }
            
    return data

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة البيداغوجية والمنهاج التفاعلي - تقني في البرمجة (INT1204 - BT)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Marked.js for fast Markdown parsing -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <!-- Google Fonts: Tajawal and JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Tajawal:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'Tajawal', sans-serif;
            background-color: #f8fafc;
            color: #0f172a;
        }

        code, pre {
            font-family: 'JetBrains Mono', monospace;
            direction: ltr;
            text-align: left;
        }

        /* Custom Scrollbars */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }

        /* Markdown Rendered Typography */
        .markdown-body h1 {
            font-size: 1.65rem;
            font-weight: 800;
            color: #1e3a8a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
            margin-top: 1.25rem;
            margin-bottom: 1rem;
        }
        .markdown-body h2 {
            font-size: 1.35rem;
            font-weight: 700;
            color: #1e40af;
            margin-top: 1.2rem;
            margin-bottom: 0.75rem;
        }
        .markdown-body h3 {
            font-size: 1.15rem;
            font-weight: 700;
            color: #0369a1;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }
        .markdown-body p {
            line-height: 1.85;
            margin-bottom: 0.95rem;
            color: #334155;
            text-align: justify;
        }
        .markdown-body ul, .markdown-body ol {
            padding-right: 1.5rem;
            margin-bottom: 1rem;
            list-style-type: disc;
        }
        .markdown-body ol {
            list-style-type: decimal;
        }
        .markdown-body li {
            margin-bottom: 0.35rem;
            line-height: 1.7;
        }
        table, .markdown-body table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
            margin-bottom: 1.5rem;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            border: 1px solid #cbd5e1;
            direction: rtl !important;
        }
        th, .markdown-body th {
            background-color: #f1f5f9;
            color: #0f172a;
            font-weight: 700;
            padding: 0.65rem 0.85rem;
            border: 1px solid #cbd5e1;
            text-align: center !important;
            font-size: 0.9rem;
            vertical-align: middle;
        }
        td, .markdown-body td {
            padding: 0.6rem 0.85rem;
            border: 1px solid #e2e8f0;
            color: #334155;
            font-size: 0.88rem;
            line-height: 1.6;
            text-align: right !important;
            direction: rtl !important;
            vertical-align: top;
        }
        .country-header, .country-header * {
            text-align: center !important;
        }
        .plan-meta-card, .plan-meta-card * {
            direction: rtl !important;
            text-align: right !important;
            unicode-bidi: embed !important;
        }
        .markdown-body tr:nth-child(even) {
            background-color: #f8fafc;
        }
        .markdown-body pre {
            background-color: #0f172a;
            color: #f8fafc;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin: 1rem 0;
            border: 1px solid #1e293b;
            font-size: 0.9rem;
            line-height: 1.5;
        }
        .markdown-body code {
            background-color: #f1f5f9;
            color: #0284c7;
            padding: 0.15rem 0.35rem;
            border-radius: 0.25rem;
            font-size: 0.9em;
        }
        .markdown-body pre code {
            background-color: transparent;
            color: inherit;
            padding: 0;
            font-size: 0.88em;
        }
        .markdown-body blockquote {
            border-right: 4px solid #3b82f6;
            background-color: #eff6ff;
            padding: 0.75rem 1rem;
            margin: 1rem 0;
            border-radius: 0 0.375rem 0.375rem 0;
            color: #1e40af;
        }

        /* NATIVE PRINT STYLES */
        @media print {
            @page {
                size: A4 portrait;
                margin: 20mm 15mm 20mm 15mm !important;
            }
            html, body {
                height: auto !important;
                min-height: 100% !important;
                overflow: visible !important;
                position: static !important;
                background: white !important;
                color: black !important;
                font-size: 11pt !important;
                display: block !important;
            }
            .no-print, header, #sidebar, #top-controls, #tab-bar, #module-bar, .action-buttons {
                display: none !important;
            }
            #main-container {
                display: block !important;
                height: auto !important;
                overflow: visible !important;
                padding: 0 !important;
                margin: 0 !important;
                width: 100% !important;
                position: static !important;
            }
            #content-card {
                box-shadow: none !important;
                border: none !important;
                padding: 0 !important;
                margin: 0 !important;
                width: 100% !important;
                height: auto !important;
                overflow: visible !important;
                display: block !important;
                position: static !important;
            }
            .markdown-body {
                display: block !important;
                height: auto !important;
                overflow: visible !important;
                width: 100% !important;
            }
            .markdown-body table {
                border: 1pt solid black !important;
                page-break-inside: avoid;
            }
            .markdown-body th {
                background-color: #f2f2f2 !important;
                color: black !important;
                border: 1pt solid black !important;
            }
            .markdown-body td {
                border: 1pt solid black !important;
                color: black !important;
            }
            .markdown-body pre {
                border: 1pt solid #666 !important;
                background-color: #fafafa !important;
                color: black !important;
                page-break-inside: avoid;
                white-space: pre-wrap !important;
            }
        }
    </style>
</head>
<body class="flex flex-col h-screen overflow-hidden">

    <!-- Top Navigation Header -->
    <header class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white border-b border-slate-800 shadow-lg px-6 py-3 flex-shrink-0 z-30 no-print">
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center font-black text-xl shadow-md border border-blue-400/30">
                    💻
                </div>
                <div>
                    <h1 class="text-lg md:text-xl font-black tracking-wide text-white flex items-center gap-2">
                        المنهاج البيداغوجي الرقمي الشامل
                        <span class="text-xs bg-blue-600 text-white px-2 py-0.5 rounded-full font-bold">INT1204 - BT</span>
                    </h1>
                    <p class="text-xs text-slate-400">تقني في الإعلام الآلي - خيار برمجة | وزارة التكوين والتعليم المهنيين (INFEP)</p>
                </div>
            </div>

            <!-- Semester Pills -->
            <div id="semester-selector" class="flex items-center gap-1.5 bg-slate-800/80 p-1.5 rounded-xl border border-slate-700/60 shadow-inner">
                <!-- dynamically loaded -->
            </div>

            <!-- Global Action Controls (3 Separate Clean Print Buttons) -->
            <div class="flex items-center gap-2">
                <button onclick="printIsolated('teacher')" title="طباعة البطاقة التقنية الخاصة بالأستاذ" class="bg-indigo-600 hover:bg-indigo-700 active:scale-95 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-all shadow-md">
                    <span>👨‍🏫</span>
                    <span>طباعة البطاقة التقنية</span>
                </button>
                <button onclick="printIsolated('plan')" title="طباعة مخطط الدرس الرسمي بالمقاربة بالكفاءات مع خانة التوقيع" class="bg-amber-600 hover:bg-amber-700 active:scale-95 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-all shadow-md">
                    <span>📋</span>
                    <span>طباعة مخطط الدرس (APC)</span>
                </button>
                <button onclick="printIsolated('student')" title="طباعة درس وورشات المتربص كاملة" class="bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-all shadow-md">
                    <span>👨‍🎓</span>
                    <span>طباعة درس المتربص</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Sub-Header: Modules Strip -->
    <div id="module-bar" class="bg-white border-b border-slate-200 px-6 py-2.5 flex items-center gap-2 overflow-x-auto shadow-sm flex-shrink-0 z-20 no-print">
        <!-- populated dynamically -->
    </div>

    <!-- Main Content Workspace (Sidebar + Viewer) -->
    <div class="flex flex-1 overflow-hidden">
        
        <!-- Sidebar: Lessons List -->
        <aside id="sidebar" class="w-80 md:w-96 bg-slate-50 border-l border-slate-200 flex flex-col flex-shrink-0 overflow-hidden shadow-inner no-print">
            <!-- Search & Filter -->
            <div class="p-3 border-b border-slate-200 bg-white">
                <div class="relative">
                    <input type="text" id="lesson-search" oninput="filterLessons()" placeholder="بحث في عناوين الدروس والأفواج..." 
                           class="w-full pl-3 pr-9 py-2 text-xs bg-slate-100 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all text-slate-800">
                    <span class="absolute right-3 top-2.5 text-slate-400 text-xs">🔍</span>
                </div>
            </div>

            <!-- List Container -->
            <div id="lessons-list" class="flex-1 overflow-y-auto p-3 space-y-2">
                <!-- dynamic buttons -->
            </div>

            <!-- Footer Stats -->
            <div class="p-3 border-t border-slate-200 bg-slate-100 text-center text-xs text-slate-500 font-medium">
                المجموع السداسي: <span id="module-hours-badge" class="font-bold text-slate-700">17 أسبوعاً</span>
            </div>
        </aside>

        <!-- Main Document Area -->
        <main id="main-container" class="flex-1 overflow-y-auto bg-slate-100/60 p-4 md:p-6 flex flex-col">
            
            <!-- Workspace Top Bar & Tabs -->
            <div id="top-controls" class="bg-white rounded-2xl shadow-sm border border-slate-200/80 p-4 mb-4 flex flex-col md:flex-row items-center justify-between gap-4 no-print">
                <div>
                    <div class="flex items-center gap-2 mb-1">
                        <span id="current-badge-week" class="bg-blue-100 text-blue-700 text-xs font-black px-2.5 py-0.5 rounded-full">الأسبوع 01</span>
                        <span id="current-badge-mod" class="bg-slate-100 text-slate-600 text-xs font-semibold px-2 py-0.5 rounded">MQ1</span>
                    </div>
                    <h2 id="current-lesson-title" class="text-lg md:text-xl font-black text-slate-800">عنوان الدرس يظهر هنا</h2>
                </div>

                <!-- Tabs: 3 Main Resources + All/Prog -->
                <div id="tab-bar" class="flex items-center gap-1 bg-slate-100 p-1.5 rounded-xl border border-slate-200 flex-wrap">
                    <button id="tab-teacher-btn" onclick="setTab('teacher')" class="px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 shadow-sm bg-white text-blue-700 border border-slate-200">
                        <span>👨‍🏫</span>
                        <span>البطاقة التقنية (للأستاذ)</span>
                    </button>
                    <button id="tab-plan-btn" onclick="setTab('plan')" class="px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 text-slate-600 hover:text-slate-900">
                        <span>📋</span>
                        <span>مخطط الدرس (APC)</span>
                    </button>
                    <button id="tab-student-btn" onclick="setTab('student')" class="px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 text-slate-600 hover:text-slate-900">
                        <span>👨‍🎓</span>
                        <span>محتوى الدرس (للمتربص)</span>
                    </button>
                    <button id="tab-both-btn" onclick="setTab('both')" class="px-3 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1 text-slate-600 hover:text-slate-900">
                        <span>📄</span>
                        <span>عرض الكل</span>
                    </button>
                    <button id="tab-prog-btn" onclick="setTab('prog')" class="px-3 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1 text-slate-600 hover:text-slate-900">
                        <span>🗓️</span>
                        <span>التدرج 17 أسبوعاً</span>
                    </button>
                </div>
            </div>

            <!-- Content Card -->
            <div id="content-card" class="bg-white rounded-2xl shadow-sm border border-slate-200/80 p-6 md:p-10 flex-1">
                
                <!-- 1. TEACHER CONTENT CONTAINER -->
                <div id="teacher-content-container" class="markdown-body"></div>

                <!-- 2. OFFICIAL APC PLAN CONTAINER -->
                <div id="plan-content-container" class="markdown-body hidden"></div>

                <!-- 3. STUDENT CONTENT CONTAINER -->
                <div id="student-content-container" class="markdown-body hidden"></div>

                <!-- 4. PROGRESSION CONTAINER -->
                <div id="prog-content-container" class="markdown-body hidden"></div>

            </div>

        </main>

    </div>

    <!-- Embedded Curriculum Database -->
    <script>
        const CURRICULUM_DATA = __CURRICULUM_JSON__;

        let currentSemesterKey = "SEMESTRE_1";
        let currentModuleKey = "";
        let currentLessonIndex = 0;
        let currentActiveTab = "teacher";

        marked.setOptions({
            gfm: true,
            breaks: true
        });

        window.addEventListener('DOMContentLoaded', () => {
            buildSemesterSelector();
            selectSemester("SEMESTRE_1");
        });

        function buildSemesterSelector() {
            const container = document.getElementById('semester-selector');
            container.innerHTML = "";
            const semKeys = Object.keys(CURRICULUM_DATA.semesters);
            
            semKeys.forEach((key, idx) => {
                const sem = CURRICULUM_DATA.semesters[key];
                const btn = document.createElement('button');
                btn.id = `sem-btn-${key}`;
                btn.className = `px-3 py-1.5 rounded-lg text-xs font-black transition-all ${key === currentSemesterKey ? 'bg-blue-600 text-white shadow-sm' : 'text-slate-300 hover:text-white hover:bg-slate-700/60'}`;
                btn.textContent = sem.name;
                btn.onclick = () => selectSemester(key);
                container.appendChild(btn);
            });
        }

        function selectSemester(semKey) {
            currentSemesterKey = semKey;
            
            Object.keys(CURRICULUM_DATA.semesters).forEach(k => {
                const btn = document.getElementById(`sem-btn-${k}`);
                if (btn) {
                    if (k === semKey) {
                        btn.className = 'px-3 py-1.5 rounded-lg text-xs font-black transition-all bg-blue-600 text-white shadow-sm';
                    } else {
                        btn.className = 'px-3 py-1.5 rounded-lg text-xs font-black transition-all text-slate-300 hover:text-white hover:bg-slate-700/60';
                    }
                }
            });

            buildModuleBar();
        }

        function buildModuleBar() {
            const container = document.getElementById('module-bar');
            container.innerHTML = "";
            
            const modules = CURRICULUM_DATA.semesters[currentSemesterKey].modules;
            const modKeys = Object.keys(modules);
            
            if (modKeys.length === 0) {
                container.innerHTML = "<span class='text-xs text-slate-400'>لا توجد مقاييس في هذا السداسي</span>";
                return;
            }

            currentModuleKey = modKeys[0];

            modKeys.forEach(mKey => {
                const mod = modules[mKey];
                const btn = document.createElement('button');
                btn.id = `mod-btn-${mKey}`;
                btn.className = `px-3.5 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all border flex items-center gap-1.5 ${mKey === currentModuleKey ? 'bg-blue-50 text-blue-700 border-blue-300 shadow-sm' : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50'}`;
                
                const shortCode = mKey.split('_')[0];
                btn.innerHTML = `<span class="bg-blue-100 text-blue-800 text-[10px] px-1.5 py-0.5 rounded font-black">${shortCode}</span> <span>${mod.title.replace(shortCode, '').trim()}</span>`;
                btn.onclick = () => selectModule(mKey);
                container.appendChild(btn);
            });

            selectModule(currentModuleKey);
        }

        function selectModule(mKey) {
            currentModuleKey = mKey;
            
            const modules = CURRICULUM_DATA.semesters[currentSemesterKey].modules;
            Object.keys(modules).forEach(k => {
                const btn = document.getElementById(`mod-btn-${k}`);
                if (btn) {
                    if (k === mKey) {
                        btn.className = 'px-3.5 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all border flex items-center gap-1.5 bg-blue-50 text-blue-700 border-blue-300 shadow-sm ring-2 ring-blue-500/20';
                    } else {
                        btn.className = 'px-3.5 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all border flex items-center gap-1.5 bg-white text-slate-600 border-slate-200 hover:bg-slate-50';
                    }
                }
            });

            renderLessonsList();
        }

        function renderLessonsList() {
            const listEl = document.getElementById('lessons-list');
            listEl.innerHTML = "";
            
            const mod = CURRICULUM_DATA.semesters[currentSemesterKey].modules[currentModuleKey];
            const lessons = mod.lessons;
            
            document.getElementById('module-hours-badge').textContent = `${lessons.length} أسبوعاً معتمداً`;

            if (lessons.length === 0) {
                listEl.innerHTML = "<div class='text-center py-8 text-xs text-slate-400'>لا توجد دروس مسجلة بعد لهذا المقياس</div>";
                return;
            }

            lessons.forEach((l, idx) => {
                const btn = document.createElement('button');
                btn.id = `lesson-btn-${idx}`;
                btn.className = `w-full text-right p-3 rounded-xl transition-all border flex flex-col gap-1 ${idx === 0 ? 'bg-blue-50 border-blue-400 text-blue-900 shadow-sm' : 'bg-white border-slate-200/90 text-slate-800 hover:bg-slate-50 hover:border-slate-300'}`;
                
                const weekMatch = l.title.match(/^(\\d+)/);
                const weekNum = weekMatch ? weekMatch[1] : (idx + 1);
                const displayTitle = l.title.replace(/^\\d+\\s*-\\s*/, '');

                btn.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="bg-blue-100 text-blue-800 text-[10px] font-black px-2 py-0.5 rounded">الأسبوع ${weekNum}</span>
                        <span class="text-[10px] text-slate-400">مكتمل APC</span>
                    </div>
                    <span class="text-xs font-bold leading-relaxed line-clamp-2">${displayTitle}</span>
                `;
                btn.onclick = () => loadLesson(idx);
                listEl.appendChild(btn);
            });

            loadLesson(0);
        }

        function loadLesson(idx) {
            currentLessonIndex = idx;
            const mod = CURRICULUM_DATA.semesters[currentSemesterKey].modules[currentModuleKey];
            const lesson = mod.lessons[idx];
            
            mod.lessons.forEach((_, i) => {
                const b = document.getElementById(`lesson-btn-${i}`);
                if (b) {
                    if (i === idx) {
                        b.className = 'w-full text-right p-3 rounded-xl transition-all border flex flex-col gap-1 bg-blue-50 border-blue-400 text-blue-900 shadow-sm ring-2 ring-blue-500/20';
                    } else {
                        b.className = 'w-full text-right p-3 rounded-xl transition-all border flex flex-col gap-1 bg-white border-slate-200/90 text-slate-800 hover:bg-slate-50 hover:border-slate-300';
                    }
                }
            });

            const weekMatch = lesson.title.match(/^(\\d+)/);
            const weekNum = weekMatch ? weekMatch[1] : (idx + 1);
            document.getElementById('current-badge-week').textContent = `الأسبوع ${weekNum}`;
            document.getElementById('current-badge-mod').textContent = currentModuleKey.split('_')[0];
            document.getElementById('current-lesson-title').textContent = lesson.title;

            document.getElementById('teacher-content-container').innerHTML = marked.parse(lesson.teacher || '');
            document.getElementById('plan-content-container').innerHTML = marked.parse(lesson.plan || '');
            document.getElementById('student-content-container').innerHTML = marked.parse(lesson.student || '');
            document.getElementById('prog-content-container').innerHTML = marked.parse(mod.progression || '');

            normalizeFormatting(document.getElementById('teacher-content-container'));
            normalizeFormatting(document.getElementById('plan-content-container'));
            normalizeFormatting(document.getElementById('student-content-container'));
            normalizeFormatting(document.getElementById('prog-content-container'));

            setTab(currentActiveTab);
            document.getElementById('main-container').scrollTo({ top: 0, behavior: 'smooth' });
        }

        function normalizeFormatting(container) {
            if (!container) return;
            container.querySelectorAll('table').forEach(tbl => {
                tbl.style.direction = 'rtl';
            });
            container.querySelectorAll('th').forEach(th => {
                th.style.textAlign = 'center';
                th.removeAttribute('align');
            });
            container.querySelectorAll('td').forEach(td => {
                td.style.textAlign = 'right';
                td.style.direction = 'rtl';
                td.removeAttribute('align');
            });
            container.querySelectorAll('h1, h2, h3, h4, h5, p, div').forEach(el => {
                if (el.textContent && el.textContent.includes('الجمهورية الجزائرية الديمقراطية الشعبية')) {
                    el.style.textAlign = 'center';
                    el.classList.add('text-center');
                }
            });
        }

        function setTab(tab) {
            currentActiveTab = tab;
            
            const teacherEl = document.getElementById('teacher-content-container');
            const planEl = document.getElementById('plan-content-container');
            const studentEl = document.getElementById('student-content-container');
            const progEl = document.getElementById('prog-content-container');

            const btnTeacher = document.getElementById('tab-teacher-btn');
            const btnPlan = document.getElementById('tab-plan-btn');
            const btnStudent = document.getElementById('tab-student-btn');
            const btnBoth = document.getElementById('tab-both-btn');
            const btnProg = document.getElementById('tab-prog-btn');

            [btnTeacher, btnPlan, btnStudent, btnBoth, btnProg].forEach(btn => {
                btn.className = 'px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 text-slate-600 hover:text-slate-900';
            });

            // Hide all by default
            teacherEl.classList.add('hidden');
            planEl.classList.add('hidden');
            studentEl.classList.add('hidden');
            progEl.classList.add('hidden');

            if (tab === 'teacher') {
                btnTeacher.className = 'px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 bg-white text-blue-700 border border-slate-200 shadow-sm';
                teacherEl.classList.remove('hidden');
            } else if (tab === 'plan') {
                btnPlan.className = 'px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 bg-white text-amber-700 border border-slate-200 shadow-sm';
                planEl.classList.remove('hidden');
            } else if (tab === 'student') {
                btnStudent.className = 'px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 bg-white text-emerald-700 border border-slate-200 shadow-sm';
                studentEl.classList.remove('hidden');
            } else if (tab === 'both') {
                btnBoth.className = 'px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 bg-white text-purple-700 border border-slate-200 shadow-sm';
                teacherEl.classList.remove('hidden');
                planEl.classList.remove('hidden');
                studentEl.classList.remove('hidden');
            } else if (tab === 'prog') {
                btnProg.className = 'px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 bg-white text-amber-700 border border-slate-200 shadow-sm';
                progEl.classList.remove('hidden');
            }
        }

        /* 
         * ISOLATED IFRAME PRINT ENGINE
         * Solves the single-page print cutoff and guarantees 20mm/15mm A4 margins on all pages.
         */
        function printIsolated(type) {
            const mod = CURRICULUM_DATA.semesters[currentSemesterKey].modules[currentModuleKey];
            const lesson = mod.lessons[currentLessonIndex];
            const isPlan = (type === 'plan');
            
            let rawContent = "";
            let title = "";
            if (type === 'teacher') {
                rawContent = lesson.teacher;
                title = 'البطاقة التقنية البيداغوجية (للأستاذ)';
            } else if (type === 'plan') {
                rawContent = lesson.plan;
                title = 'مخطط درس بالمقاربة بالكفاءات (Plan de Leçon)';
            } else {
                rawContent = lesson.student;
                title = 'محتوى الدرس والورشة المخبرية (للمتربص)';
            }

            if (isPlan) {
                // Remove duplicate headers from body so print-header serves as the single official top banner
                rawContent = rawContent.replace(/<div class="country-header"[\\s\\S]*?<\\/div>/gi, '');
                rawContent = rawContent.replace(/<h3 class="plan-main-title"[\\s\\S]*?<\\/h3>/gi, '');
            }
            
            const parsedHTML = marked.parse(rawContent || '');
            const semName = CURRICULUM_DATA.semesters[currentSemesterKey].name;

            // Create hidden iframe
            const iframe = document.createElement('iframe');
            iframe.style.position = 'fixed';
            iframe.style.right = '0';
            iframe.style.bottom = '0';
            iframe.style.width = '0';
            iframe.style.height = '0';
            iframe.style.border = '0';
            document.body.appendChild(iframe);

            const doc = iframe.contentWindow.document;
            doc.open();
            doc.write(`
                <!DOCTYPE html>
                <html lang="ar" dir="rtl">
                <head>
                    <meta charset="UTF-8">
                    <title>${title} - ${lesson.title}</title>
                    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
                    <style>
                        @page {
                            size: A4 portrait;
                            margin: 20mm 15mm 20mm 15mm !important;
                        }
                        * {
                            box-sizing: border-box;
                        }
                        html, body {
                            margin: 0;
                            padding: 0;
                            background: #ffffff;
                            color: #000000;
                            font-family: 'Tajawal', sans-serif;
                            font-size: 11pt;
                            line-height: 1.65;
                            direction: rtl !important;
                            text-align: right !important;
                            unicode-bidi: embed !important;
                        }
                        .print-header {
                            border-bottom: 2pt solid #0f172a;
                            padding-bottom: 8pt;
                            margin-bottom: 14pt;
                            text-align: center;
                        }
                        .print-header h4 {
                            margin: 0 0 4pt 0;
                            font-size: 10pt;
                            color: #334155;
                            font-weight: bold;
                        }
                        .print-header h2 {
                            margin: 0 0 6pt 0;
                            font-size: 14pt;
                            color: #000;
                            font-weight: 800;
                        }
                        .print-header p {
                            margin: 0;
                            font-size: 9.5pt;
                            color: #475569;
                        }
                        .bubble-title {
                            display: inline-block;
                            border: 2pt dashed #0f172a;
                            border-radius: 25px;
                            padding: 4pt 20pt;
                            margin: 6pt 0 12pt 0;
                            font-weight: 800;
                            font-size: 13pt;
                            background-color: #f8fafc;
                        }
                        .country-header, .plan-main-title {
                            display: none !important;
                        }
                        .plan-meta-card {
                            direction: rtl !important;
                            text-align: right !important;
                            border: 1.5pt solid #0f172a !important;
                            border-radius: 4pt !important;
                            padding: 8pt 12pt !important;
                            margin-bottom: 12pt !important;
                            background-color: #fdfdfd !important;
                            font-size: 10pt !important;
                            line-height: 1.8 !important;
                            page-break-inside: avoid;
                        }
                        .plan-meta-card div, .plan-meta-card strong, .plan-meta-card span {
                            direction: rtl !important;
                            text-align: right !important;
                            unicode-bidi: embed !important;
                        }
                        table {
                            width: 100%;
                            border-collapse: collapse;
                            margin: 12pt 0;
                            page-break-inside: avoid;
                            direction: rtl !important;
                        }
                        th {
                            background-color: #f1f5f9 !important;
                            color: #000 !important;
                            border: 1pt solid #475569 !important;
                            padding: 6pt 8pt;
                            font-size: 9.5pt;
                            font-weight: bold;
                            text-align: center !important;
                            vertical-align: middle;
                        }
                        td {
                            border: 1pt solid #64748b !important;
                            padding: 5pt 8pt;
                            font-size: 9pt;
                            color: #000 !important;
                            text-align: right !important;
                            direction: rtl !important;
                            vertical-align: top;
                        }
                        .print-header h4, .print-header h5, .print-header h2, .print-header p {
                            text-align: center !important;
                        }
                        tr:nth-child(even) {
                            background-color: #f8fafc !important;
                        }
                        h1 {
                            font-size: 14pt;
                            font-weight: 800;
                            color: #0f172a;
                            border-bottom: 1.5pt solid #475569;
                            padding-bottom: 4pt;
                            margin-top: 14pt;
                            margin-bottom: 8pt;
                            page-break-after: avoid;
                        }
                        h2 {
                            font-size: 12.5pt;
                            font-weight: 700;
                            color: #1e3a8a;
                            margin-top: 12pt;
                            margin-bottom: 6pt;
                            page-break-after: avoid;
                        }
                        h3 {
                            font-size: 11.5pt;
                            font-weight: 700;
                            color: #0369a1;
                            margin-top: 10pt;
                            margin-bottom: 4pt;
                            page-break-after: avoid;
                        }
                        p {
                            margin-bottom: 8pt;
                            text-align: justify;
                            direction: rtl !important;
                            unicode-bidi: embed !important;
                        }
                        ul, ol {
                            direction: rtl !important;
                            text-align: right !important;
                            padding-right: 20pt !important;
                            padding-left: 0 !important;
                            margin-right: 0 !important;
                            margin-bottom: 10pt;
                            list-style-position: inside;
                        }
                        li {
                            direction: rtl !important;
                            text-align: right !important;
                            unicode-bidi: embed !important;
                            margin-bottom: 4pt;
                        }
                        pre {
                            direction: ltr !important;
                            text-align: left !important;
                            background: #f8fafc !important;
                            border: 1pt solid #94a3b8 !important;
                            border-radius: 4pt;
                            padding: 8pt 10pt;
                            font-family: 'JetBrains Mono', monospace;
                            font-size: 8.5pt;
                            line-height: 1.45;
                            white-space: pre-wrap;
                            word-break: break-all;
                            margin: 10pt 0;
                            page-break-inside: avoid;
                        }
                        code {
                            font-family: 'JetBrains Mono', monospace;
                            background: #f1f5f9;
                            padding: 1pt 3pt;
                            font-size: 8.5pt;
                        }
                        blockquote {
                            border-right: 3pt solid #2563eb;
                            background-color: #f8fafc;
                            padding: 6pt 10pt;
                            margin: 10pt 0;
                            font-size: 9.5pt;
                            page-break-inside: avoid;
                        }
                    </style>
                </head>
                <body>
                    <div class="print-header">
                        <h4>الجمهورية الجزائرية الديمقراطية الشعبية</h4>
                        <h5 style="margin: 0 0 4pt 0; font-size: 9.5pt; color: #475569; font-weight: bold; text-align: center;">وزارة التكوين والتعليم المهنيين</h5>
                        <h2>المعهد الوطني للتكوين المهني (INFEP) - تخصص تقني في البرمجة INT1204</h2>
                        <div class="bubble-title">${title}</div>
                        <p>المقياس: ${mod.title} | ${lesson.title} | ${semName}</p>
                    </div>
                    <div>
                        ${parsedHTML}
                    </div>
                </body>
                </html>
            `);
            normalizeFormatting(doc.body);
            if (isPlan) {
                doc.querySelectorAll('.country-header, .plan-main-title').forEach(el => el.remove());
            }
            doc.close();

            iframe.contentWindow.focus();
            setTimeout(() => {
                iframe.contentWindow.print();
                setTimeout(() => {
                    document.body.removeChild(iframe);
                }, 2000);
            }, 500);
        }

        function filterLessons() {
            const query = document.getElementById('lesson-search').value.toLowerCase().trim();
            const mod = CURRICULUM_DATA.semesters[currentSemesterKey].modules[currentModuleKey];
            mod.lessons.forEach((l, idx) => {
                const btn = document.getElementById(`lesson-btn-${idx}`);
                if (btn) {
                    if (l.title.toLowerCase().includes(query)) {
                        btn.classList.remove('hidden');
                    } else {
                        btn.classList.add('hidden');
                    }
                }
            });
        }
    </script>
</body>
</html>
"""

def main():
    print("Gathering curriculum database from markdown files...")
    data = gather_all_data()
    
    data_json = json.dumps(data, ensure_ascii=False)
    final_html = HTML_TEMPLATE.replace("__CURRICULUM_JSON__", data_json)
    
    OUTPUT_HTML.write_text(final_html, encoding="utf-8")
    print("Beautiful HTML Syllabus regenerated with official Plan de Lecon APC and 3 print options!")

if __name__ == "__main__":
    main()
