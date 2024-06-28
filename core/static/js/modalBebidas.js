document.addEventListener('DOMContentLoaded', (event) => {
    const tarifasLink = document.getElementById('verTarifasBebidas');
    
    tarifasLink.addEventListener('click', () => {
        const imageUrl = '/static/img/preciosBebidas.png';
        const modalImage = document.getElementById('modalImage');
        modalImage.src = imageUrl;
    });
});