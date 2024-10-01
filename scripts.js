const toggleButton = document.getElementById('theme-toggle');
const icon = toggleButton.querySelector('i');

const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    document.body.classList.add('dark-theme');
    icon.classList.replace('fa-moon', 'fa-sun');
} else {
    document.body.classList.add('light-theme');
    icon.classList.replace('fa-sun', 'fa-moon');
}

function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    document.body.classList.toggle('light-theme')
    if (document.body.classList.contains('dark-theme')) {
        icon.classList.replace('fa-moon', 'fa-sun');
        localStorage.setItem('theme', 'dark');
    } else {
        icon.classList.replace('fa-sun', 'fa-moon');
        localStorage.setItem('theme', 'light');
    }
}

// apply function when button click
toggleButton.addEventListener('click', toggleTheme);





window.addEventListener('DOMContentLoaded', (event) => {
    const elements = document.querySelectorAll('.fade-up');

    elements.forEach((element, index) => {
        // Add a slight delay for each element if needed
        setTimeout(() => {
            element.classList.add('fade-up-visible');
        }, index * 100); // Increase delay by 200ms for each element
    });
});

window.addEventListener('DOMContentLoaded', () => {
    const gifImage = document.getElementById('gifImage');
    // Reload the gif by resetting its src
    gifImage.src = gifImage.src;
});