import os
import shutil
import hashlib
import matplotlib.pyplot as plt
from datetime import datetime

# تنظیمات اصلی
TARGET_DIR = "./my_files"
ACCENT_COLOR = "#ffdb70" # رنگ طلایی وب‌سایت سعید

def get_file_hash(file_path):
    """ایجاد یک اثر انگشت برای تشخیص فایل‌های تکراری"""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def organize_and_analyze():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print("⚠️ پوشه خالی بود، ساخته شد. فایل‌هایت را داخل my_files بریز.")
        return

    file_stats = {}
    hashes = {}
    duplicates = 0
    total_moved = 0

    print(f"🚀 شروع پردازش در {datetime.now().strftime('%H:%M:%S')}")

    for filename in os.listdir(TARGET_DIR):
        path = os.path.join(TARGET_DIR, filename)
        
        if os.path.isfile(path):
            # ۱. تشخیص فایل تکراری
            f_hash = get_file_hash(path)
            if f_hash in hashes:
                os.remove(path)
                duplicates += 1
                continue
            hashes[f_hash] = filename

            # ۲. تحلیل پسوند و حجم
            ext = os.path.splitext(filename)[1].lower() or "others"
            size_mb = os.path.getsize(path) / (1024 * 1024)
            file_stats[ext] = file_stats.get(ext, 0) + size_mb

            # ۳. جابجایی
            dest_folder = os.path.join(TARGET_DIR, ext.replace('.', ''))
            if not os.path.exists(dest_folder): os.makedirs(dest_folder)
            shutil.move(path, os.path.join(dest_folder, filename))
            total_moved += 1

    # ۴. تولید نمودار برای وب‌سایت
    if file_stats:
        generate_chart(file_stats)
        print(f"✅ {total_moved} فایل جابجا شد.")
        print(f"🗑️ {duplicates} فایل تکراری حذف شد.")

def generate_chart(stats):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    names = list(stats.keys())
    values = list(stats.values())

    plt.bar(names, values, color=ACCENT_COLOR)
    plt.title("تحلیل توزیع فایل‌ها (MB)", fontsize=14, pad=20)
    plt.savefig("portfolio_stats.png", transparent=True) # ذخیره برای سایت
    print("📊 نمودار تحلیل (portfolio_stats.png) ساخته شد.")

if __name__ == "__main__":
    organize_and_analyze()