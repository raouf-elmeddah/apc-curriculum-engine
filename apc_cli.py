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

def get_curricula():
    # Detect all curriculum directories
    currs = []
    for d in SCRIPT_DIR.iterdir():
        if d.is_dir() and ((d / "SEMESTRE_1").exists() or (d / "00_PROGRAMME_GLOBAL").exists()):
            currs.append(d)
    return sorted(currs, key=lambda x: x.name)

def show_status():
    curricula = get_curricula()
    if not curricula:
        print("❌ لم يتم العثور على أي مجلدات مناهج!")
        return

    print("=" * 75)
    print("   📊 إحصائيات المناهج التكوينية بالمقاربة بالكفاءات (APC Engine)")
    print("=" * 75)

    for c_dir in curricula:
        print(f"\n🎓 التخصص: {c_dir.name}")
        print("-" * 60)
        semesters = [d for d in c_dir.iterdir() if d.is_dir() and d.name.startswith("SEMESTRE_")]
        semesters.sort(key=lambda x: x.name)
        
        total_lessons = 0
        total_modules = 0
        
        for s in semesters:
            mods = [m for m in s.iterdir() if m.is_dir() and (m / "Lessons").exists()]
            s_lessons = sum(len(list((m / "Lessons").glob("*.md"))) for m in mods)
            total_modules += len(mods)
            total_lessons += s_lessons
            print(f"  📁 {s.name:<15} | المقاييس: {len(mods):<2} | الدروس: {s_lessons:<3} (17 أسبوعاً)")
            
        stage_dir = c_dir / "STAGE_PRATIQUE_MI"
        if stage_dir.exists():
            stage_docs = len(list(stage_dir.glob("*.md")))
            print(f"  📁 STAGE_PRATIQUE  | وثائق التربص والمرافقة: {stage_docs}")
            
        html_files = list(c_dir.glob("*_Syllabus.html"))
        if html_files:
            hf = html_files[0]
            html_status = f"✅ موجود ({hf.name} - {hf.stat().st_size / (1024*1024):.2f} MB)"
        else:
            html_status = "❌ غير مجمع"
            
        print(f"  📌 الإجمالي: {total_modules} مقاييس | {total_lessons} درساً (APC) | المنهاج التفاعلي: {html_status}")

    print("\n" + "=" * 75)

def build_syllabus():
    print("🚀 جاري بناء وتجميع المناهج التفاعلية HTML (Isolated Print Engine)...")
    builders = [
        ("INT1204 - Programmation BT", "build_html_syllabus.py"),
        ("INT04Q - Creation de sites web", "build_html_syllabus_int04q.py")
    ]
    for name, script in builders:
        script_path = SCRIPT_DIR / script
        if script_path.exists():
            print(f"\n🔨 تجميع منهاج: {name}...")
            subprocess.run([sys.executable, str(script_path)])
    print("\n✅ تم الانتهاء من تجميع المناهج بنجاح!")

def main():
    parser = argparse.ArgumentParser(
        description="APC Curriculum Engine - محرك المناهج التكوينية بالمقاربة بالكفاءات",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة الاستخدام (Examples):
  python apc_cli.py status      # عرض إحصائيات السداسيات والدروس
  python apc_cli.py build       # تجميع المنهاج التفاعلي HTML والطباعة المعزولة
        """
    )
    
    parser.add_argument(
        "action",
        choices=["status", "build"],
        nargs="?",
        default="status",
        help="الإجراء المطلوب تنفيذه (افتراضي: status)"
    )
    
    args = parser.parse_args()
    
    if args.action == "status":
        show_status()
    elif args.action == "build":
        build_syllabus()

if __name__ == "__main__":
    main()
