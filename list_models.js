
const API_KEY = "AIzaSyCDLQxtK8MRFPkbM0lgW6l1rJjoO9dTj-s";

async function listModels() {
    try {
        console.log("Fetching available models...");

        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${API_KEY}`, {
            headers: {
                'Referer': 'http://localhost:8080/'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.models) {
            console.log("\nAvailable Models:");
            data.models.forEach(model => {
                // Filter for models that might support image generation or are generally useful
                console.log(`- Name: ${model.name}`);
                console.log(`  Display Name: ${model.displayName}`);
                console.log(`  Supported Generation Methods: ${model.supportedGenerationMethods.join(", ")}`);
                console.log("---");
            });
        } else {
            console.log("No models found or error in response:", data);
        }

    } catch (error) {
        console.error("Error fetching models:", error);
    }
}

listModels();
