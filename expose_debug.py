
import os

file_path = 'd:\\develop\\hairstyler\\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "window.appElements = elements;"
replacement = "window.appElements = elements;\n        window.CONFIG = CONFIG;"

if target in content:
    if "window.CONFIG = CONFIG;" not in content:
        content = content.replace(target, replacement)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully exposed CONFIG.")
    else:
        print("CONFIG already exposed.")
else:
    print("Target string not found.")
