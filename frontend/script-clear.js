// Ao clicar no botão com id "clear-btn"
document.getElementById("clear-btn")
    .addEventListener("click", async (e) => {
        e.preventDefault();
        // Faz requisição a: http://localhost:8000/clear  
        await fetch(`${backendURL}/clear`, {
            method: "DELETE",
        });
    });