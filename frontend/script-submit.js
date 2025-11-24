document.getElementById("form")
    .addEventListener("submit", async (e) => {
        e.preventDefault();
    
        const temperatura = parseFloat(document.getElementById(tempInputId).value);
        const humidade = parseFloat(document.getElementById(humInputId).value);

        await fetch(`${backendURL}/data`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                temperatura: temperatura,
                humidade: humidade
            })
        });
    });