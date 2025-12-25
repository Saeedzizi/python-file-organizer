import os
import shutil
import hashlib
import matplotlib.pyplot as plt
from datetime import datetime

# Global Configurations
TARGET_DIR = "./my_files"
ACCENT_COLOR = "#ffdb70" # Saeed's Website Golden Accent

def get_file_hash(file_path):
    """Creates a digital fingerprint to detect duplicate files"""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def organize_and_analyze():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"⚠️ Directory '{TARGET_DIR}' was missing. Created successfully.")
        print("Action: Please put some files inside 'my_files' and run again.")
        return

    file_stats = {}
    hashes = {}
    duplicates = 0
    total_moved = 0

    print(f"🚀 Processing started at {datetime.now().strftime('%H:%M:%S')}")

    for filename in os.listdir(TARGET_DIR):
        path = os.path.join(TARGET_DIR, filename)
        
        # Process only files (ignore directories)
        if os.path.isfile(path):
            # 1. Duplicate Detection (using MD5 Hashing)
            f_hash = get_file_hash(path)
            if f_hash in hashes:
                os.remove(path)
                duplicates += 1
                continue
            hashes[f_hash] = filename

            # 2. Analyze Extension and Size (MB)
            ext = os.path.splitext(filename)[1].lower() or ".others"
            size_mb = os.path.getsize(path) / (1024 * 1024)
            file_stats[ext] = file_stats.get(ext, 0) + size_mb

            # 3. File Organization
            dest_folder = os.path.join(TARGET_DIR, ext.replace('.', ''))
            if not os.path.exists(dest_folder): 
                os.makedirs(dest_folder)
            
            shutil.move(path, os.path.join(dest_folder, filename))
            total_moved += 1

    # 4. Generate Visual Report for Website
    if file_stats:
        generate_chart(file_stats)
        print(f"✅ {total_moved} files moved to their respective folders.")
        print(f"🗑️ {duplicates} duplicate files were identified and removed.")
    else:
        print("ℹ️ No files found to process.")

def generate_chart(stats):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    
    extensions = list(stats.keys())
    sizes = list(stats.values())

    plt.bar(extensions, sizes, color=ACCENT_COLOR)
    plt.title("File Distribution Analysis (MB)", fontsize=14, pad=20)
    plt.xlabel("File Extensions")
    plt.ylabel("Total Size (MB)")
    
    # Save the chart for the portfolio website
    plt.savefig("portfolio_stats.png", transparent=True)
    print("📊 Analysis Chart (portfolio_stats.png) generated successfully.")

if __name__ == "__main__":
    organize_and_analyze()
    print("✨ Task completed.")