#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
APC Curriculum Engine - Master CLI
محرك المناهج التكوينية بالمقاربة بالكفاءات (الجمهورية الجزائرية الديمقراطية الشعبية)
=============================================================================
"""

import sys
import argparse
import pathlib
import subprocess
import io

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
CURRICULUM_DIR = SCRIPT_DIR / "INT1204 - Programmation BT"

def show_status():
    print("=" * 70)
    print("   📊 إحصائيات المنهاج التكويني (INT1204 - Programmation BT)")
    print("=" * 70)
    if not CURRICULUM_DIR.exists():
        print("❌ لم يتم العثور على مجلد المنهاج!")
        return

    semesters = [d for d in CURRICULUM_DIR.iterdir() if d.is_dir() and d.name.startswith("SEMESTRE_")]
    semesters.sort(key=lambda x: x.name)
    
    total_lessons = 0
    total_modules = 0
    
    for s in semesters:
        mods = [m for m in s.iterdir() if m.is_dir() and (m / "Lessons").exists()]
        s_lessons = sum(len(list((m / "Lessons").glob("*.md"))) for m in mods)
        total_modules += len(mods)
        total_lessons += s_lessons
        print(f"📁 {s.name:<15} | المقاييس: {len(mods):<2} | الدروس: {s_lessons:<3} (17 أسبوعاً)")
        
    stage_dir = CURRICULUM_DIR / "STAGE_PRATIQUE_MI"
    stage_docs = len(list(stage_dir.glob("*.md"))) if stage_dir.exists() else 0
    print(f"📁 STAGE_PRATIQUE  | وثائق التربص الميداني والمرافقة: {stage_docs}")
    
    html_file = CURRICULUM_DIR / "منهاج_البرمجة_التفاعلي_Syllabus.html"
    html_status = f"✅ موجود ({html_file.stat().st_size / (1024*1024):.2f} MB)" if html_file.exists() else "❌ غير مجمع"
    
    print("-" * 70)
    print(f"إجمالي المقاييس : {total_modules}")
    print(f"إجمالي الدروس   : {total_lessons} درساً بالمقاربة بالكفاءات (APC)")
    print(f"المنهاج التفاعلي: {html_status}")
    print("=" * 70)

def build_syllabus():
    print("🚀 جاري بناء وتجميع المنهاج التفاعلي HTML (Isolated Print Engine)...")
    res = subprocess.run([sys.executable, str(SCRIPT_DIR / "build_html_syllabus.py")])
    if res.returncode == 0:
        html_file = CURRICULUM_DIR / "منهاج_البرمجة_التفاعلي_Syllabus.html"
        print(f"✅ تم تجميع المنهاج بنجاح: {html_file.name}")
    else:
        print("❌ حدث خطأ أثناء تجميع المنهاج التفاعلي.")

def enrich_curriculum():
    print("🚀 جاري إثراء كافة الدروس بالمحتوى التطبيقي والمخبري الشامل...")
    res = subprocess.run([sys.executable, str(SCRIPT_DIR / "populate_entire_curriculum_rich.py")])
    if res.returncode == 0:
        print("✅ تم إثراء الدروس بنجاح!")
        build_syllabus()
    else:
        print("❌ حدث خطأ أثناء إثراء الدروس.")

def main():
    parser = argparse.ArgumentParser(
        description="APC Curriculum Engine - محرك المناهج التكوينية بالمقاربة بالكفاءات",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة الاستخدام (Examples):
  python apc_cli.py status      # عرض إحصائيات السداسيات والدروس
  python apc_cli.py build       # تجميع المنهاج التفاعلي HTML والطباعة المعزولة
  python apc_cli.py enrich      # إثراء الدروس بمحتوى نظري وتطبيقي شامل
        """
    )
    
    parser.add_argument(
        "action",
        choices=["status", "build", "enrich"],
        nargs="?",
        default="status",
        help="الإجراء المطلوب تنفيذه (افتراضي: status)"
    )
    
    args = parser.parse_args()
    
    if args.action == "status":
        show_status()
    elif args.action == "build":
        build_syllabus()
    elif args.action == "enrich":
        enrich_curriculum()

if __name__ == "__main__":
    main()
