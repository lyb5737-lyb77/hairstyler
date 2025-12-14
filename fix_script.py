
import os

file_path = r'd:\develop\hairstyler\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Remove lines 170-228 (inclusive)
# But wait, line numbers might change if I modify the list.
# I should identify the blocks by content.

new_lines = []
skip = False
for line in lines:
    if 'async function fileToGenerativePart(file) {' in line:
        skip = True
    
    if not skip:
        new_lines.append(line)
    
    if skip and 'elements.generateBtn.querySelector(\'.loader\').classList.add(\'hidden\');' in line:
        # This is inside the first generateHairstyle.
        # I need to find the closing brace of the function.
        pass
    
    if skip and line.strip() == '}' and len(new_lines) > 0 and 'elements.generateBtn.querySelector' in lines[lines.index(line)-2]:
         # This is risky.
         pass

# Let's use a simpler approach.
# I know the exact lines from view_file.
# 170 to 228.
# 472 to 532.

# But I need to be careful about 0-indexing.
# Line 170 in view_file is index 169.
# Line 228 is index 227.

# Remove 170-228 first.
# lines[169:228] -> remove.

# But wait, if I remove lines, the indices for the second block change.
# So I should handle the second block first?
# Or just calculate the offset.

# Let's do it by content matching to be robust.

final_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Block 1: fileToGenerativePart + generateHairstyle (SDK)
    if 'async function fileToGenerativePart(file) {' in line:
        # Skip until end of generateHairstyle
        # I know it ends before 'function init() {'
        while 'function init() {' not in lines[i]:
            i += 1
        continue

    # Block 2: verifyPassword + generateHairstyle (Fetch)
    if 'if (sumInput === sum) { // Success state.remainingCount +=extraCount;' in line:
        # Replace this block with correct code
        correct_code = """            if (sumInput === sum) {
                // Success
                state.remainingCount += extraCount;
                saveUsageCount();
                elements.authModal.classList.add('hidden');
                alert(`인증 성공! ${extraCount}회가 충전되었습니다.`);
                closeStyleDetail(); 
            } else {
                alert("비밀번호가 일치하지 않습니다.");
            }
        }

        async function generateHairstyle() {
            console.log("generateHairstyle called");
            if (state.remainingCount <= 0) {
                closeStyleDetail();
                showAuthModal();
                return;
            }

            if (!CONFIG.API_KEY || CONFIG.API_KEY === "YOUR_API_KEY_HERE") {
                closeStyleDetail();
                return alert("소스코드의 CONFIG.API_KEY에 유효한 API Key를 입력해주세요.");
            }

            if (!state.userImageFile) {
                closeStyleDetail();
                return alert("먼저 본인의 사진을 업로드해주세요.");
            }

            setLoading(true);

            try {
                // Prepare prompts and images
                const userImageBase64 = await fileToBase64(state.userImageFile);
                const currentStyles = state.styles[state.selectedGender];
                if (!currentStyles || !currentStyles[state.selectedStyleIndex]) {
                    throw new Error("선택된 스타일 정보를 찾을 수 없습니다.");
                }

                const selectedStyle = currentStyles[state.selectedStyleIndex];
                const styleImageBase64 = selectedStyle.src.split(',')[1];

                const prompt = `Generate a high-quality, photorealistic image of the person in the User Photo with the hairstyle from the Reference Hairstyle image. The person should look exactly like the User Photo but with the new hairstyle. The hairstyle should match the Reference Hairstyle. Ensure seamless blending and realistic lighting.`;

                // Imagen 3 REST API Call
                const url = `https://generativelanguage.googleapis.com/v1beta/models/${CONFIG.MODEL_NAME}:predict?key=${CONFIG.API_KEY}`;
                
                const requestBody = {
                    instances: [
                        {
                            prompt: prompt,
                            image: { bytesBase64Encoded: userImageBase64 }
                        }
                    ],
                    parameters: {
                        sampleCount: 1,
                        aspectRatio: "1:1",
                        personGeneration: "allow_adult"
                    }
                };

                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requestBody)
                });

                if (!response.ok) {
                    const errorText = await response.text();
                    throw new Error(`API Error: ${response.status} ${response.statusText} - ${errorText}`);
                }

                const data = await response.json();
                console.log("API Response:", data);

                let generatedImageBase64 = null;
                if (data.predictions && data.predictions[0] && data.predictions[0].bytesBase64Encoded) {
                    generatedImageBase64 = `data:image/png;base64,${data.predictions[0].bytesBase64Encoded}`;
                } else if (data.predictions && data.predictions[0] && data.predictions[0].mimeType && data.predictions[0].bytesBase64Encoded) {
                    generatedImageBase64 = `data:${data.predictions[0].mimeType};base64,${data.predictions[0].bytesBase64Encoded}`;
                }

                if (generatedImageBase64) {
                    state.remainingCount--;
                    saveUsageCount();
                    elements.resultImage.src = generatedImageBase64;
                    closeStyleDetail();
                    elements.resultSection.classList.remove('hidden');
                    
                    elements.downloadBtn.onclick = () => {
                        const link = document.createElement('a');
                        link.href = generatedImageBase64;
                        link.download = `hairstyle-result-${Date.now()}.png`;
                        link.click();
                    };
                } else {
                    throw new Error("이미지 생성 데이터가 응답에 없습니다.");
                }

            } catch (error) {
                console.error("Error:", error);
                if (error.message.includes("400") || error.message.includes("404")) {
                    alert("Imagen 3 모델 호출 실패. 설정이나 API 키 권한을 확인해주세요.\\n" + error.message);
                } else {
                    alert("오류가 발생했습니다: " + error.message);
                }
            } finally {
                setLoading(false);
            }
        }
"""
        final_lines.append(correct_code)
        
        # Skip lines until end of corrupted block
        # It ends at line 532: '                }'
        # But I need to be careful.
        # The corrupted block ends when 'function fileToBase64' starts (line 534).
        while 'function fileToBase64(file) {' not in lines[i]:
            i += 1
        continue

    final_lines.append(line)
    i += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print("Fixed index.html content")
