
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'if (input.length < 2) return alert("잘못된 비밀번호 형식입니다."); const extraCountStr = input.slice(-1); // Last' in line:
        # Found the start of corruption
        new_lines.append('            if (input.length < 2) return alert("잘못된 비밀번호 형식입니다.");\n')
        new_lines.append('            \n')
        new_lines.append('            const extraCountStr = input.slice(-1); // Last digit\n')
        new_lines.append('            const sumInputStr = input.slice(0, -1); // Rest\n')
        new_lines.append('            const extraCount = parseInt(extraCountStr, 10);\n')
        new_lines.append('            const sumInput = parseInt(sumInputStr, 10);\n')
        new_lines.append('\n')
        new_lines.append('            if (isNaN(extraCount) || isNaN(sumInput)) {\n')
        new_lines.append('                return alert("숫자만 입력해주세요.");\n')
        new_lines.append('            }\n')
        continue
    
    if 'digit const sumInputStr = input.slice(0, -1); // Rest const extraCount=parseInt(extraCountStr, 10);' in line:
        continue # Skip corrupted line
    
    if 'const sumInput = parseInt(sumInputStr, 10); if (isNaN(extraCount) || isNaN(sumInput)) {' in line:
        continue # Skip corrupted line
        
    if 'return' in line and 'alert("숫자만 입력해주세요.");' in lines[lines.index(line)+1]:
         # This matches the 'return' followed by alert in the corrupted block
         # But I need to be careful not to match other returns.
         # In the corrupted block:
         # 411:                 return
         # 412:                 alert("숫자만 입력해주세요.");
         continue

    if 'alert("숫자만 입력해주세요.");' in line:
        continue

    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed corrupted block in index.html")
