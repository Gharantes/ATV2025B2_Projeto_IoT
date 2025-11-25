// Cada 3 segundos
setInterval(() => {
    const imgElement = document.getElementById('chart-img')
    // Altera o sufixo do "src" da imagem.
    // Iso vai forçar a imagem a recarregar, 
    // E com isso, já vai buscar o gráfico novo, se existir um.  
    imgElement.src = `${backendURL}/chart?ts=` + Date.now()
}, 3000)