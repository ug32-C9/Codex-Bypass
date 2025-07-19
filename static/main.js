async function resolveURL() {
    const input = document.getElementById("urlInput").value;
    const resultDiv = document.getElementById("result");

    if (!input) {
        resultDiv.textContent = "Please enter a URL.";
        return;
    }

    resultDiv.textContent = "Bypassing...";

    try {
        const res = await fetch("/api/resolve", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: input })
        });

        const data = await res.json();

        if (data.result) {
            resultDiv.innerHTML = `✅ Bypassed URL: <a href="${data.result}" target="_blank">${data.result}</a>`;
        } else {
            resultDiv.innerHTML = `❌ Error: ${data.error}`;
        }
    } catch (err) {
        resultDiv.textContent = "⚠️ Something went wrong.";
        console.error(err);
    }
      }
