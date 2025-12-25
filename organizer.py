import os
import shutil

# مسیری که فایل‌های شلوغ آنجاست را مشخص کن (مثلاً پوشه دانلود یا دسکتاپ)
folder_path = "./my_project_files"

# اگر پوشه وجود ندارد، آن را می‌سازد
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"پوشه {folder_path} ساخته شد. چند فایل داخلش بریز!")

def organize_files():
    for filename in os.listdir(folder_path):
        # جدا کردن نام فایل از پسوند
        name, extension = os.path.splitext(filename)
        extension = extension[1:].lower() # حذف نقطه از پسوند

        if extension:
            # ساخت پوشه مخصوص برای آن پسوند (مثلاً پوشه png)
            target_folder = os.path.join(folder_path, extension)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            
            # انتقال فایل به پوشه مربوطه
            shutil.move(os.path.join(folder_path, filename), os.path.join(target_folder, filename))
            print(f"فایل {filename} به پوشه {extension} منتقل شد.")

if __name__ == "__main__":
    organize_files()
    print("تمام فایل‌ها با موفقیت مرتب شدند! 🔥")