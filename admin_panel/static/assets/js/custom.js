// Theme toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeToggleBtn = document.getElementById('themeToggle');
    const icon = themeToggleBtn.querySelector('i');
    
    // Check for saved theme preference or default to 'dark'
    const currentTheme = localStorage.getItem('theme') || 'dark';
    document.body.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    // Toggle theme when button is clicked
    themeToggleBtn.addEventListener('click', function() {
        const currentTheme = document.body.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        document.body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });

    // Update icon based on theme
    function updateThemeIcon(theme) {
        if (theme === 'dark') {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        } else {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    }

    // Add smooth hover effect for action buttons
    const actionButtons = document.querySelectorAll('.action-button');
    
    actionButtons.forEach(button => {
        button.addEventListener('mouseover', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
        
        button.addEventListener('mouseout', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = 'none';
        });
    });

    // Prevent scroll event propagation
    const sidebar = document.querySelector('.sidebar');
    const mainPanel = document.querySelector('.main-panel');

    if (sidebar) {
        sidebar.addEventListener('wheel', (e) => {
            e.stopPropagation();
        });
    }

    if (mainPanel) {
        mainPanel.addEventListener('wheel', (e) => {
            e.stopPropagation();
        });
    }

    // Remove perfect scrollbar
    if (typeof PerfectScrollbar !== 'undefined') {
        const scrollElements = document.querySelectorAll('.sidebar, .main-panel');
        scrollElements.forEach(element => {
            if (element._ps) {
                element._ps.destroy();
            }
            element.classList.remove('ps');
            element.classList.remove('ps--active-y');
            element.classList.remove('ps--active-x');
        });
    }
});
