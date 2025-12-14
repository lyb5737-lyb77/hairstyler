
import os

file_path = 'd:\\develop\\hairstyler\\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'window.appState = state;' in line:
        continue
    if 'window.appElements = elements;' in line:
        continue
    if 'window.CONFIG = CONFIG;' in line:
        continue
    if '// Expose for debugging' in line:
        continue
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Debug exposure removed.")
