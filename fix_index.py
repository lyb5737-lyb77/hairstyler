
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix maleLabels (lines 267-268 in 1-based index, so 266-267 in 0-based)
# But lines might have shifted if I made edits.
# I will search for the broken lines.

new_lines = []
skip_next = False

for i in range(len(lines)):
    if skip_next:
        skip_next = False
        continue
    
    line = lines[i]
    if 'const maleLabels' in line and '슬릭' in line and not '슬릭백' in line:
        # Found the broken maleLabels line
        next_line = lines[i+1]
        combined = line.strip() + next_line.strip()
        # Clean up the join
        combined = combined.replace('슬릭            백', '슬릭백') # Adjust spacing if needed
        # Actually, let's just replace the whole line with the correct one
        new_lines.append('            const maleLabels = ["텍스처 크롭", "아이비 리그 컷", "쉼표 머리", "가르마 펌", "시스루 댄디", "롱 트림", "리프 컷", "소프트 투블럭", "슬릭백", "맨 번"];\n')
        skip_next = True
    elif 'const femaleLabels' in line and '땋은' in line and not '땋은 머리' in line:
        # Found the broken femaleLabels line
        next_line = lines[i+1]
        # Replace with correct one
        new_lines.append('            const femaleLabels = ["히피 펌", "레이어드 C컬", "보브 컷", "긴 웨이브", "허쉬 컷", "풀뱅", "발레아쥬 컬러", "반묶음", "숏컷", "땋은 머리"];\n')
        skip_next = True
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed index.html")
