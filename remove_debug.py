
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove visual debug line
new_lines = [line for line in lines if "DEBUG: SCRIPT STARTED" not in line]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Removed visual debug from index.html")
