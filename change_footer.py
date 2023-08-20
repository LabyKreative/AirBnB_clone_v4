#!/usr/bin/python3
# a script that change <footer>Best School</footer> to <footer>Holberton School>
import os
import re

def change_footer_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Use a case-insensitive regex to find and replace <footer> tags
    new_content = re.sub(r'<footer>.*?</footer>', '<footer>Holberton School</footer>', content, flags=re.IGNORECASE)

    with open(file_path, 'w') as f:
        f.write(new_content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                change_footer_content(file_path)

if __name__ == "__main__":
    current_dir = os.getcwd()
    process_directory(current_dir)
    print("Footer content changed in HTML files.")
