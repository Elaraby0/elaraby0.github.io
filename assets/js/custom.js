document.addEventListener('DOMContentLoaded', function() {
    const scrollArrow = document.getElementById('scrollArrow');
    const contentSection = document.getElementById('contentSection');
    if (scrollArrow && contentSection) {
        scrollArrow.addEventListener('click', function() {
            contentSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    }
});
