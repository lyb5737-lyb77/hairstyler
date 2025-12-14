
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Content around line 110:")
for i in range(108, 115):
    if i < len(lines):
        print(f"{i+1}: {repr(lines[i])}")

print("\nContent around line 266:")
for i in range(264, 275):
    if i < len(lines):
        print(f"{i+1}: {repr(lines[i])}")

# Insert log at start of script
# Look for 'const CONFIG = {'
found_config = False
for i, line in enumerate(lines):
    if 'const CONFIG = {' in line:
        lines.insert(i, '        console.log("DEBUG: Script started via Python injection");\n')
        found_config = True
        break

if not found_config:
    print("Could not find CONFIG to insert log")

# Insert log in init
# Look for 'function init() {'
found_init = False
for i, line in enumerate(lines):
    if 'function init() {' in line:
        lines.insert(i+1, '            console.log("DEBUG: init() called via Python injection");\n')
        found_init = True
        break

if not found_init:
    print("Could not find init() to insert log")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Modified index.html")
