#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML Syllabus Builder for INT04Q: Création de sites web statiques et dynamiques
Includes Isolated Iframe Multi-Page A4 Printing Engine and official APC Lesson Plan.
"""

import os
import sys
import json
import re
import pathlib

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR / "INT04Q - Creation de sites web"
OUTPUT_HTML = ROOT_DIR / "منهاج_إنشاء_المواقع_التفاعلي_Syllabus.html"

def extract_lesson_parts(content):
    parts = re.split(r'^#{1,3}\s*محتوى الدرس.*$', content, maxsplit=1, flags=re.MULTILINE)
    if len(parts) > 1:
        teacher_part = parts[0].strip()
        student_part = "# محتوى الدرس والورشة المخبرية (للمتربص)\n\n" + parts[1].strip()
    else:
        teacher_part = content.strip()
        student_part = "محتوى الدرس للمتربص غير مفصول في هذا الملف."
    return teacher_part, student_part

def generate_apc_plan_markdown(sem_name, mod_code, mod_name, w_num, title, duree_str, comp_text):
    clean_duree = duree_str.split('(')[0].strip() if '(' in duree_str else duree_str
    
    return f"""<div class="country-header" style="text-align: center; margin-bottom: 1rem;">
<h2 style="text-align: center; font-size: 1.25rem; font-weight: 800; color: #0f172a; margin-bottom: 0.2rem;">الجمهورية الجزائرية الديمقراطية الشعبية</h2>
<h3 style="text-align: center; font-size: 1.05rem; font-weight: 700; color: #475569; margin-top: 0;">وزارة التكوين والتعليم المهنيين</h3>
</div>

<h3 class="plan-main-title" style="text-align: center; font-size: 1.2rem; font-weight: 800; color: #0369a1; margin-bottom: 1rem;">📋 مخطط درس بالمقاربة بالكفاءات</h3>

<div class="plan-meta-card" dir="rtl" style="direction: rtl !important; text-align: right !important; background-color: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; font-size: 0.95rem; line-height: 1.8;">
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>التخصص:</strong> شهادة التأهيل المهني (CQP) - إنشاء المواقع الإلكترونية الثابتة والديناميكية (INT04Q)</div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>المستوى:</strong> تأهيل مهني - 06 أشهر (340 ساعة)</div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>المقياس:</strong> <span dir="rtl">{mod_name} ({mod_code})</span></div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>عنوان الدرس:</strong> {w_num} - {title}</div>
  <div style="direction: rtl !important; text-align: right !important; margin-bottom: 3px;"><strong>المدة الزمنية:</strong> {clean_duree}</div>
  <div style="direction: rtl !important; text-align: right !important;"><strong>الكفاءة المستهدفة:</strong> {comp_text} باحترام قواعد السلامة والمعايير التقنية.</div>
</div>

---

| مراحل الدرس | نشاط الأستاذ | نشاط المتربص | الوسائل البيداغوجية | التقويم |
| :---: | :--- | :--- | :--- | :--- |
| **1- وضعية الإنطلاق** | - طرح أسئلة تمهيدية حول سياق وأهمية موضوع ({title}).<br>- عرض نموذج أو وضعية مشكلة واقعية محفزة من سوق العمل الرقمي.<br>- ربط الدرس بالممارسة اليومية في بيئة تطوير المواقع. | - الإجابة على الأسئلة التمهيدية.<br>- ملاحظة النموذج ومناقشة المعطيات.<br>- المشاركة في بناء فرضيات الحل. | - السبورة<br>- عارض البيانات (Data Show)<br>- كراس المتربص | تقويم تشخيصي / شفوي |
| **2- بناء التعلمات** | - تقديم وشرح مفاهيم ({title}) وتفكيك عناصرها المنطقية.<br>- شرح خطوات الإنجاز وتوضيح المعايير التقنية وقواعد كتابة الكود والتصميم.<br>- تقديم أمثلة توضيحية ومقارنات تطبيقية. | - الاستماع والانتباه للشرح.<br>- تدوين القواعد والمصطلحات في الكراس.<br>- طرح الأسئلة وطلب التوضيحات عند الحاجة. | - جهاز العرض الرقمي<br>- وثائق تقنية ودليل المرجع<br>- بيئة التطوير والبرمجيات | أسئلة ومتابعة مرحلية |
| **3- التطبيق** | - تكليف المتربص بإنجاز خطوات الورشة التطبيقية خطوة بخطوة على الحاسوب.<br>- تقديم التوجيهات الفردية وتصحيح الأخطاء أثناء العمل المخبري. | - تنفيذ خطوات العمل البرمجي أو الفني بدقة على الحاسوب.<br>- استعمال الأدوات والبرمجيات بطريقة صحيحة ومحترفة. | - حواسيب المخبر المتصلة بشبكة<br>- بيئة التطوير (IDE / البرمجيات المخصصة)<br>- بطاقة العمل المخبري (Fiche TP) | ملاحظة الأداء ومراقبة الكود |
| **4- التقويم النهائي** | - طرح أسئلة شفوية حول مراحل الإنجاز وخوارزمية الحل.<br>- تقديم تمرين عملي تطبيقي فردي لاختبار التحكم في المهارة. | - الإجابة على الأسئلة الشفوية باقتضاب ودقة.<br>- إنجاز التمرين العملي الفردي باستقلالية في الوقت المحدد. | - ورقة عمل / تمرين اختباري<br>- جهاز الحاسوب وأدوات العمل | تقويم تحصيلي فردي |
| **5- الإدماج والاستثمار** | - وضع المتربص في وضعية مهنية جديدة توظف مهارة ({title}) في مشروع موقع ويب متكامل.<br>- مناقشة الإنجاز وتصحيح الأخطاء واقتراح تحسينات الأداء. | - توظيف المكتسبات المعرفية والمهارية في حل الوضعية الجديدة.<br>- تقديم مقترحات لتحسين جودة وتجاوب العمل المنجز. | - مختلف الوسائل والبرمجيات المتاحة في المخبر | تقويم إدماجي |

---

**الخلاصة:**  
من خلال هذا الدرس، تمكن المتربص من اكتساب المعارف والمهارات المتعلقة بـ **{title}** وتوظيفها في وضعيات مهنية واقعية مع احترام قواعد السلامة والمعايير التقنية للويب.

---

<br>

| **التاريخ:** .................................................... | **توقيع الأستاذ:** .................................................... |
| :---: | :---: |
"""

def extract_comp_from_teacher(teacher_text):
    match = re.search(r'\*\s*\*\*الكفاءة المستهدفة[^\*]*\*\*[:\s]*([^\n\r]+)', teacher_text)
    if match:
        val = match.group(1).strip()
        return val.replace('[', '').replace(']', '').strip()
    return "أن يكون المتربص قادراً على إنجاز مهارات الدرس وتطبيقها عملياً"

def extract_duree_from_teacher(teacher_text):
    match = re.search(r'\*\*الأسبوع والمدة[^\*]*\*\*[:\s]*([^\n\r\|]+)', teacher_text)
    if match:
        val = match.group(1).strip()
        return val
    return "2 ساعات أسبوعياً"

def gather_all_data():
    data = {
        "specialty": "شهادة التأهيل المهني (CQP) - إنشاء المواقع الإلكترونية الثابتة والديناميكية (INT04Q)",
        "semesters": {}
    }
    
    sem_dirs = [
        ("SEMESTRE_1", "دورة التأهيل المهني (6 أشهر - 17 أسبوعاً)"),
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
                
                w_match = re.match(r'^(\d+)', clean_title)
                w_num = w_match.group(1) if w_match else "01"
                raw_lesson_title = re.sub(r'^\d+\s*-\s*', '', clean_title)
                
                comp_text = extract_comp_from_teacher(t_part)
                duree_text = extract_duree_from_teacher(t_part)
                
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
    <title>الحقيبة البيداغوجية والمنهاج التفاعلي - إنشاء المواقع الإلكترونية (INT04Q)</title>
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
            background-color: #0f172a;
            color: #1e293b;
        }
        code, pre {
            font-family: 'JetBrains Mono', monospace;
        }
        /* Custom scrollbar */
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

        /* Typography & Markdown styling */
        .markdown-body {
            font-family: 'Tajawal', sans-serif;
            line-height: 1.8;
            color: #1e293b;
            font-size: 1rem;
        }
        .markdown-body h1 {
            font-size: 1.55rem;
            font-weight: 800;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        .markdown-body h2 {
            font-size: 1.35rem;
            font-weight: 700;
            color: #1e3a8a;
            margin-top: 1.3rem;
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
            margin-bottom: 0.85rem;
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
        }
        .markdown-body blockquote {
            border-right: 4px solid #3b82f6;
            background-color: #f8fafc;
            padding: 0.75rem 1rem;
            margin: 1rem 0;
            color: #475569;
            border-radius: 0 4px 4px 0;
        }
    </style>
</head>
<body class="h-screen flex flex-col overflow-hidden bg-slate-900">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900 border-b border-slate-800 text-white shrink-0 z-30 shadow-md">
        <div class="px-4 py-2.5 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <span class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-2 rounded-xl text-lg font-black shadow-lg">🌐</span>
                <div>
                    <h1 class="text-sm font-black tracking-wide flex items-center gap-2">
                        إنشاء المواقع الإلكترونية الثابتة والديناميكية (INT04Q)
                        <span class="text-[10px] bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2 py-0.5 rounded-full font-bold">CQP - 340H</span>
                    </h1>
                    <p class="text-[11px] text-slate-400 font-medium">المعهد الوطني للتكوين والتعليم المهنيين - قاسي الطاهر (INFEP) | المقاربة بالكفاءات (APC)</p>
                </div>
            </div>

            <!-- Print Actions -->
            <div class="flex items-center gap-2">
                <button onclick="printIsolated('teacher')" title="طباعة البطاقة التقنية الخاصة بالأستاذ" class="bg-blue-600 hover:bg-blue-700 active:scale-95 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-all shadow-md">
                    <span>👨‍🏫</span>
                    <span class="hidden sm:inline">طباعة البطاقة التقنية</span>
                </button>
                <button onclick="printIsolated('plan')" title="طباعة مخطط الدرس الرسمي بالمقاربة بالكفاءات مع خانة التوقيع" class="bg-amber-600 hover:bg-amber-700 active:scale-95 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-all shadow-md">
                    <span>📋</span>
                    <span class="hidden sm:inline">طباعة مخطط الدرس (APC)</span>
                </button>
                <button onclick="printIsolated('student')" title="طباعة محتوى الدرس الشامل والورشة المخبرية للمتربصين" class="bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-all shadow-md">
                    <span>👨‍🎓</span>
                    <span class="hidden sm:inline">طباعة درس المتربص</span>
                </button>
            </div>
        </div>

        <!-- Modules Bar -->
        <div class="px-4 py-1.5 bg-slate-950/70 border-t border-slate-800/80 flex items-center gap-2 overflow-x-auto" id="module-bar">
            <!-- Dynamic Module Buttons -->
        </div>
    </header>

    <!-- Main Workspace -->
    <div class="flex-1 flex overflow-hidden bg-slate-100">
        
        <!-- Left Sidebar: Lessons Index -->
        <aside class="w-80 bg-white border-l border-slate-200/90 flex flex-col shrink-0 z-10 shadow-sm">
            <div class="p-3 border-b border-slate-200 flex flex-col gap-2 bg-slate-50/50">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-black text-slate-800 flex items-center gap-1.5">
                        <span>📑</span> فهرس الدروس (17 أسبوعاً)
                    </span>
                    <span id="lesson-count-badge" class="text-[10px] bg-blue-100 text-blue-800 font-black px-2 py-0.5 rounded-full">17 درساً</span>
                </div>
                <div class="relative">
                    <input type="text" id="lesson-search" oninput="filterLessons()" placeholder="بحث في عناوين الدروس..." class="w-full text-xs bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500">
                </div>
            </div>

            <!-- Lessons List -->
            <div class="flex-1 overflow-y-auto p-2 space-y-1" id="lessons-list">
                <!-- Injected via JavaScript -->
            </div>
        </aside>

        <!-- Right Content Area -->
        <main class="flex-1 flex flex-col overflow-hidden bg-white">
            
            <!-- Content Header & Tabs -->
            <div class="border-b border-slate-200 px-6 py-3 flex items-center justify-between shrink-0 bg-white shadow-xs">
                <div>
                    <div class="flex items-center gap-2 mb-1">
                        <span id="current-badge-week" class="text-[11px] font-black px-2 py-0.5 rounded bg-blue-100 text-blue-700">الأسبوع 01</span>
                        <span id="current-badge-mod" class="text-[11px] font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-700">MQ1</span>
                    </div>
                    <h2 id="current-lesson-title" class="text-base font-black text-slate-900 line-clamp-1">عنوان الدرس</h2>
                </div>

                <!-- Tabs Switching -->
                <div class="flex items-center gap-1.5 bg-slate-100 p-1 rounded-xl border border-slate-200">
                    <button id="tab-teacher-btn" onclick="setTab('teacher')" class="px-3.5 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 text-slate-600 hover:text-slate-900">
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
                    <button id="tab-both-btn" onclick="setTab('both')" class="px-3 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 text-slate-600 hover:text-slate-900" title="عرض الوثائق الثلاث معاً">
                        <span>📑</span>
                        <span>الكل</span>
                    </button>
                    <button id="tab-prog-btn" onclick="setTab('prog')" class="px-3 py-2 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 text-slate-600 hover:text-slate-900" title="التدرج البيداغوجي لـ 17 أسبوعاً">
                        <span>🗓️</span>
                        <span>التدرج (17)</span>
                    </button>
                </div>
            </div>

            <!-- Scrollable Content Body -->
            <div class="flex-1 overflow-y-auto p-8 max-w-5xl mx-auto w-full" id="main-container">
                
                <!-- 1. TEACHER CONTAINER -->
                <div id="teacher-content-container" class="markdown-body"></div>

                <!-- 2. OFFICIAL APC LESSON PLAN CONTAINER -->
                <div id="plan-content-container" class="markdown-body hidden"></div>

                <!-- 3. STUDENT CONTAINER -->
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
            buildModuleBar();
        });

        function buildModuleBar() {
            const container = document.getElementById('module-bar');
            container.innerHTML = "";
            
            const modules = CURRICULUM_DATA.semesters[currentSemesterKey].modules;
            const modKeys = Object.keys(modules);
            
            if (modKeys.length === 0) {
                container.innerHTML = "<span class='text-xs text-slate-400'>لا توجد مقاييس</span>";
                return;
            }

            currentModuleKey = modKeys[0];

            modKeys.forEach(mKey => {
                const mod = modules[mKey];
                const btn = document.createElement('button');
                btn.id = `mod-btn-${mKey}`;
                const mCode = mKey.split('_')[0];
                btn.className = `px-3 py-1 rounded-lg text-xs font-bold transition-all shrink-0 flex items-center gap-1.5 ${mKey === currentModuleKey ? 'bg-slate-700 text-white border border-slate-600 shadow-sm' : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'}`;
                btn.innerHTML = `<span class="bg-blue-600/30 text-blue-400 px-1.5 py-0.5 rounded text-[10px] font-black">${mCode}</span> <span>${mod.title.replace(mCode, '').trim()}</span>`;
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
                const mCode = k.split('_')[0];
                if (btn) {
                    if (k === mKey) {
                        btn.className = 'px-3 py-1 rounded-lg text-xs font-bold transition-all shrink-0 flex items-center gap-1.5 bg-slate-700 text-white border border-slate-600 shadow-sm';
                    } else {
                        btn.className = 'px-3 py-1 rounded-lg text-xs font-bold transition-all shrink-0 flex items-center gap-1.5 text-slate-400 hover:text-slate-200 hover:bg-slate-800';
                    }
                }
            });

            buildLessonsList();
            selectLesson(0);
        }

        function buildLessonsList() {
            const container = document.getElementById('lessons-list');
            container.innerHTML = "";
            
            const mod = CURRICULUM_DATA.semesters[currentSemesterKey].modules[currentModuleKey];
            document.getElementById('lesson-count-badge').textContent = `${mod.lessons.length} درساً`;

            mod.lessons.forEach((l, idx) => {
                const btn = document.createElement('button');
                btn.id = `lesson-btn-${idx}`;
                btn.className = `w-full text-right p-3 rounded-xl transition-all border flex flex-col gap-1 ${idx === currentLessonIndex ? 'bg-blue-50 border-blue-400 text-blue-900 shadow-sm ring-2 ring-blue-500/20' : 'bg-white border-slate-200/90 text-slate-800 hover:bg-slate-50 hover:border-slate-300'}`;
                
                const weekMatch = l.title.match(/^(\\d+)/);
                const weekNum = weekMatch ? weekMatch[1] : (idx + 1);
                const titleText = l.title.replace(/^\\d+\\s*-\\s*/, '');

                btn.innerHTML = `
                    <div class="flex items-center justify-between w-full">
                        <span class="text-[10px] font-black px-2 py-0.5 rounded bg-slate-100 text-slate-600">الأسبوع ${weekNum}</span>
                        <span class="text-[10px] text-slate-400 font-bold">17 أسبوعاً</span>
                    </div>
                    <span class="text-xs font-bold line-clamp-2 leading-relaxed">${titleText}</span>
                `;
                btn.onclick = () => selectLesson(idx);
                container.appendChild(btn);
            });
        }

        function selectLesson(idx) {
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
                        <h2>المعهد الوطني للتكوين المهني (INFEP) - تخصص إنشاء المواقع الإلكترونية INT04Q</h2>
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
    print("Gathering curriculum database from INT04Q markdown files...")
    data = gather_all_data()
    data_json = json.dumps(data, ensure_ascii=False)
    
    html_content = HTML_TEMPLATE.replace("__CURRICULUM_JSON__", data_json)
    OUTPUT_HTML.write_text(html_content, encoding="utf-8")
    print(f"✅ تم تجميع منهاج إنشاء المواقع التفاعلي بنجاح: {OUTPUT_HTML.name} ({OUTPUT_HTML.stat().st_size / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    main()
