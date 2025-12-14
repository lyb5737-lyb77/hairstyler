
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Insert visual debug at start of script
# Look for 'const CONFIG = {'
found_config = False
for i, line in enumerate(lines):
    if 'const CONFIG = {' in line:
        lines.insert(i, '        document.body.insertAdjacentHTML("afterbegin", "<h1 style=\'color:red; z-index:9999; position:fixed; top:0; left:0; background:white;\'>DEBUG: SCRIPT STARTED</h1>");\n')
        found_config = True
        break

if not found_config:
    print("Could not find CONFIG to insert log")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Modified index.html with visual debug")
