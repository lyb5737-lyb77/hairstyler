
import os

file_path = 'd:\\develop\\hairstyler\\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement 1: CONFIG object
target_config = """        const CONFIG = {
            MODEL_NAME: "gemini-3-pro-image-preview",
            // IMPORTANT: Replace with your actual API Key
            API_KEY: "AIzaSyCDLQxtK8MRFPkbM0lgW6l1rJjoO9dTj-s"
        };"""

replacement_config = """        const CONFIG = {
            MODEL_NAME: "gemini-3-pro-image-preview",
            // 중요: 이것은 기본적인 난독화 기술입니다.
            // 결정적인 공격자가 키를 찾는 것을 막을 수는 없습니다.
            // 실제 보안을 위해서는 Google Cloud Console에서 HTTP 리퍼러 제한을 사용하세요.
            KEY_PART1: "AIzaSyCDLQxtK8MRFPkb",
            KEY_PART2: "M0lgW6l1rJjoO9dTj-s"
        };"""

# Replacement 2: Validation logic
target_validation = """            if (!CONFIG.API_KEY || CONFIG.API_KEY === "YOUR_API_KEY_HERE") {
                closeStyleDetail();
                return alert("소스코드의 CONFIG.API_KEY에 유효한 API Key를 입력해주세요.");
            }"""

replacement_validation = """            // API Key 재조합
            const API_KEY = CONFIG.KEY_PART1 + CONFIG.KEY_PART2;

            if (!API_KEY || API_KEY === "YOUR_API_KEY_HERE") {
                closeStyleDetail();
                return alert("소스코드의 CONFIG.API_KEY에 유효한 API Key를 입력해주세요.");
            }"""

if target_config in content:
    content = content.replace(target_config, replacement_config)
    print("Replaced CONFIG object.")
else:
    print("Target CONFIG object not found.")
    # Debug: print surrounding lines
    start_idx = content.find("const CONFIG = {")
    if start_idx != -1:
        print("Found 'const CONFIG = {' at index", start_idx)
        print("Surrounding content:\n", content[start_idx:start_idx+200])

if target_validation in content:
    content = content.replace(target_validation, replacement_validation)
    print("Replaced validation logic.")
else:
    print("Target validation logic not found.")
    # Debug
    start_idx = content.find("if (!CONFIG.API_KEY")
    if start_idx != -1:
        print("Found 'if (!CONFIG.API_KEY' at index", start_idx)
        print("Surrounding content:\n", content[start_idx:start_idx+200])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
