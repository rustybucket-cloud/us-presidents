document.querySelector('#submit').addEventListener('click', () => {
    console.log("hello")
    const name = document.querySelector('#name').value
    window.location.href = `http://192.168.87.64:5000/presidents/${name}`
})