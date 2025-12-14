const API_KEY = "AIzaSyD7BfV8h4XWqhKMn06vUJ4TN0o5UaiB8vY";
const MODEL_NAME = "imagen-3.0-generate-001";

async function testModel(version) {
    const url = `https://generativelanguage.googleapis.com/${version}/models/${MODEL_NAME}:predict?key=${API_KEY}`;
    console.log(`Testing ${version}... URL: ${url}`);

    // Minimal dummy payload
    const requestBody = {
        instances: [{ prompt: "test" }],
        parameters: { sampleCount: 1 }
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody)
        });

        if (response.ok) {
            console.log(`SUCCESS: ${version} works!`);
            return true;
        } else {
            console.log(`FAILED: ${version} status ${response.status}`);
            const text = await response.text();
            console.log(`Error: ${text}`);
            return false;
        }
    } catch (e) {
        console.log(`ERROR: ${version} exception ${e.message}`);
        return false;
    }
}

async function run() {
    console.log("Starting tests...");
    await testModel('v1beta');
    await testModel('v1');
}

run();
