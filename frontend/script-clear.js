document.getElementById("clear-btn")
    .addEventListener("click", async (e) => {
        e.preventDefault();
    
        await fetch(`${backendURL}/clear`, {
            method: "DELETE",
        });
    });