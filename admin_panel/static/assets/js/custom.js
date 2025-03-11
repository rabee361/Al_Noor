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


function clickHandler(event) {
    if (!event.target.closest('.checkbox-cell')) {
        window.location.href = event.currentTarget.getAttribute('data-link');
    }
}



document.addEventListener('DOMContentLoaded', function() {
    // Get the modal
    const modal = document.getElementById('deleteConfirmModal');
    
    // Get all delete buttons
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    // Get the delete form and confirmation text
    const deleteForm = document.getElementById('deleteForm');
    const deleteConfirmText = document.getElementById('deleteConfirmText');
    
    // Get all close buttons
    const closeButtons = document.querySelectorAll('.close-modal');
    
    // Add click event listener to each delete button
    deleteButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Get data attributes
        const id = this.getAttribute('data-id');
        const name = this.getAttribute('data-name');
        const deleteUrl = this.getAttribute('data-delete-url');
        
        deleteForm.action = deleteUrl;
        
        // Show the modal
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent scrolling when modal is open
      });
    });
    
    // Add click event listener to close buttons
    closeButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Hide the modal
        modal.style.display = 'none';
        document.body.style.overflow = ''; // Restore scrolling
      });
    });
    
    // Close modal when clicking outside of it
    window.addEventListener('click', function(event) {
      if (event.target === modal) {
        // Hide the modal
        modal.style.display = 'none';
        document.body.style.overflow = ''; // Restore scrolling
      }
    });
    
    // Close modal when pressing Escape key
    document.addEventListener('keydown', function(event) {
      if (event.key === 'Escape' && modal.style.display === 'block') {
        modal.style.display = 'none';
        document.body.style.overflow = ''; // Restore scrolling
      }
    });
  });
  
  // Function to handle row clicks (already in your code)
  function clickHandler(event) {
    if (!event.target.closest('button')) {
      const link = event.currentTarget.dataset.link;
      if (link) {
        window.location.href = link;
      }
    }
  }