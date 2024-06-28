document.addEventListener('DOMContentLoaded', (event) => {
    const tarifasLink = document.getElementById('verTarifasLinkBase');
    
    tarifasLink.addEventListener('click', () => {
        const imageUrl = '/static/img/preciosSalas.png';
        const modalImage = document.getElementById('modalImage');
        modalImage.src = imageUrl;
    });
});