import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):
    # Перевірка існування директорії призначення та створення, якщо не існує
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            # Отримання розширення файлу
            extension = os.path.splitext(file)[1][1:]
            # Створення піддиректорії з назвою розширення, якщо не існує
            dest_subdir = os.path.join(dest_dir, extension)
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            # Копіювання файлу до відповідної піддиректорії
            shutil.copy(source_file_path, dest_subdir)

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Recursive file copying and sorting')
    parser.add_argument('source_dir', type=str, help='Source directory path')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Destination directory path')
    args = parser.parse_args()

    try:
        copy_files(args.source_dir, args.dest_dir)
        print("Files copied and sorted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()