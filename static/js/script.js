document.addEventListener('DOMContentLoaded', function() {
    // Pagination functionality
    const paginationLinks = document.querySelectorAll('.pagination a');
    paginationLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const page = this.getAttribute('data-page');
            loadPage(page);
        });
    });

    function loadPage(page) {
        const currentPath = window.location.pathname;
        const newUrl = `${currentPath}?page=${page}`;
        window.location.href = newUrl;
    }

    // Tile hover effect
    const tiles = document.querySelectorAll('.tile');
    tiles.forEach(tile => {
        tile.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'transform 0.3s ease';
        });
        tile.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

});