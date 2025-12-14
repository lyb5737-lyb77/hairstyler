
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <script type="module"> with <script>
new_content = content.replace('<script type="module">', '<script>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed type=module from index.html")
