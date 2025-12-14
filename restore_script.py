
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Add type="module" back
for i, line in enumerate(lines):
    if '<script>' in line:
        lines[i] = line.replace('<script>', '<script type="module">')
        break

# 2. Add import at the top of the script
# Find the line with "DEBUG: Script started..." or "const CONFIG"
insert_pos = -1
for i, line in enumerate(lines):
    if 'const CONFIG = {' in line:
        insert_pos = i
        break

if insert_pos != -1:
    lines.insert(insert_pos, '        import { GoogleGenerativeAI } from "@google/generative-ai";\n')

# 3. Add generateHairstyle and fileToGenerativePart functions
# Find the end of setupEventListeners or before init()
insert_func_pos = -1
for i, line in enumerate(lines):
    if 'function init() {' in line:
        insert_func_pos = i
        break

if insert_func_pos != -1:
    functions_code = """
        async function fileToGenerativePart(file) {
            return new Promise((resolve) => {
                const reader = new FileReader();
                reader.onloadend = () => resolve({
                    inlineData: {
                        data: reader.result.split(',')[1],
                        mimeType: file.type
                    }
                });
                reader.readAsDataURL(file);
            });
        }

        async function generateHairstyle() {
            if (!state.selectedStyleIndex && state.selectedStyleIndex !== 0) {
                alert("스타일을 선택해주세요!");
                return;
            }

            if (!elements.userPhotoInput.files[0]) {
                alert("사진을 업로드해주세요!");
                return;
            }

            const styleLabel = state.selectedGender === 'male' 
                ? maleLabels[state.selectedStyleIndex] 
                : femaleLabels[state.selectedStyleIndex];

            elements.generateBtn.disabled = true;
            elements.generateBtn.querySelector('.btn-text').textContent = "생성 중...";
            elements.generateBtn.querySelector('.loader').classList.remove('hidden');

            try {
                const genAI = new GoogleGenerativeAI(CONFIG.API_KEY);
                const model = genAI.getGenerativeModel({ model: CONFIG.MODEL_NAME });

                const imageFile = elements.userPhotoInput.files[0];
                const imageBytes = await fileToGenerativePart(imageFile);

                const prompt = `Change the hairstyle of the person in this image to ${styleLabel}. Keep the face and background exactly the same. High quality, realistic.`;

                const result = await model.generateContent([prompt, imageBytes]);
                const response = await result.response;
                // Assuming the model returns text or we handle it. 
                // For now, let's log the response.
                console.log("Generation result:", response);
                
                // If it returns an image, we need to handle it.
                // But let's first get the API call working.
                
            } catch (error) {
                console.error("Generation error:", error);
                alert("생성 중 오류가 발생했습니다: " + error.message);
            } finally {
                elements.generateBtn.disabled = false;
                elements.generateBtn.querySelector('.btn-text').textContent = "이 스타일로 생성하기 ✨";
                elements.generateBtn.querySelector('.loader').classList.add('hidden');
            }
        }
    """
    lines.insert(insert_func_pos, functions_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Restored script content in index.html")
