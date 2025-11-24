setInterval(() => {
    const imgElement = document.getElementById('chart-img')
    imgElement.src = `${backendURL}/chart?ts=` + Date.now()
}, 3000)