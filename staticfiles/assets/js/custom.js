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

    // MODIFIED: Remove scroll event blocking which was preventing pull-to-refresh
    // Only prevent scroll propagation on desktop, not on mobile
    const sidebar = document.querySelector('.sidebar');
    const mainPanel = document.querySelector('.main-panel');

    // Check if it's not a mobile device (based on screen width)
    const isMobile = window.innerWidth <= 768;
    
    if (!isMobile) {
        if (sidebar) {
            sidebar.addEventListener('wheel', (e) => {
                e.stopPropagation();
            });
        }
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

// Password visibility toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    // Function to create and setup password toggle
    function setupPasswordToggle(passwordInput) {
        // Create container div
        const container = document.createElement('div');
        container.className = 'password-field-container';
        
        // Insert container before password input
        passwordInput.parentNode.insertBefore(container, passwordInput);
        
        // Move password input into container
        container.appendChild(passwordInput);
        
        // Create toggle button
        const toggleButton = document.createElement('button');
        toggleButton.type = 'button';
        toggleButton.className = 'password-toggle';
        toggleButton.innerHTML = '<i class="fas fa-eye"></i>';
        
        // Add toggle button to container
        container.appendChild(toggleButton);
        
        // Add click event listener
        toggleButton.addEventListener('click', function() {
            const type = passwordInput.type === 'password' ? 'text' : 'password';
            passwordInput.type = type;
            
            // Toggle icon
            toggleButton.innerHTML = `<i class="fas fa-eye${type === 'password' ? '' : '-slash'}"></i>`;
        });
    }
    
    // Setup toggle for all password fields
    const passwordFields = document.querySelectorAll('input[type="password"]');
    passwordFields.forEach(setupPasswordToggle);
});

document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('importForm');
  const loadingModal = document.getElementById('loadingModal');

  if (form && loadingModal) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading modal with animation
        loadingModal.style.display = 'block';
        setTimeout(() => loadingModal.classList.add('show'), 10);
      
      // Submit form
      const formData = new FormData(this);
      fetch(this.action, {
          method: 'POST',
          body: formData,
      })
      .then(response => {
          if (response.redirected) {
              window.location.href = response.url;
          }
      })
      .catch(error => {
          console.error('Error:', error);
          loadingModal.style.display = 'none';
          loadingModal.classList.remove('show');
          alert('حدث خطأ أثناء استيراد البيانات. يرجى المحاولة مرة أخرى.');
      });
  });
});

// Searchable Dropdown Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize searchable dropdowns
    initSearchableDropdowns();
    
    function initSearchableDropdowns() {
        const searchInputs = document.querySelectorAll('.search-input');
        
        searchInputs.forEach(input => {
            const targetId = input.getAttribute('data-target');
            const select = document.getElementById(targetId);
            
            if (!select) return;
            
            // Create dropdown container
            const dropdownOptions = document.createElement('div');
            dropdownOptions.className = 'dropdown-options';
            input.parentNode.appendChild(dropdownOptions);
            
            // Add a data attribute to track if an option was explicitly selected
            input.setAttribute('data-selection-made', 'false');
            
            // Populate dropdown options from select
            const options = Array.from(select.options);
            options.forEach(option => {
                if (option.value) { // Skip empty option if exists
                    const optionElement = document.createElement('div');
                    optionElement.className = 'dropdown-option';
                    optionElement.setAttribute('data-value', option.value);
                    optionElement.textContent = option.textContent;
                    dropdownOptions.appendChild(optionElement);
                    
                    // Set initial selected state
                    if (option.selected) {
                        optionElement.classList.add('selected');
                        input.value = option.textContent;
                        input.setAttribute('data-selection-made', 'true');
                    }
                    
                    // Handle option click
                    optionElement.addEventListener('click', function() {
                        select.value = this.getAttribute('data-value');
                        input.value = this.textContent;
                        input.setAttribute('data-selection-made', 'true');
                        dropdownOptions.classList.remove('show');
                        
                        // Update selected state
                        dropdownOptions.querySelectorAll('.dropdown-option').forEach(opt => {
                            opt.classList.remove('selected');
                        });
                        this.classList.add('selected');
                        
                        // Trigger change event on select
                        const event = new Event('change', { bubbles: true });
                        select.dispatchEvent(event);
                    });
                }
            });
            
            // Show dropdown on input focus
            input.addEventListener('focus', function() {
                dropdownOptions.classList.add('show');
            });
            
            // Filter options on input  
            input.addEventListener('input', function() {
                // When user types, mark that no selection has been made yet
                input.setAttribute('data-selection-made', 'false');
                select.value = ''; // Clear the select value
                
                const searchText = this.value.toLowerCase();
                const options = dropdownOptions.querySelectorAll('.dropdown-option');
                
                options.forEach(option => {
                    const optionText = option.textContent.toLowerCase();
                    if (optionText.startsWith(searchText)) {
                        option.classList.remove('hidden');
                    } else {
                        option.classList.add('hidden');
                    }
                });
            });
            
            // Close dropdown when clicking outside
            document.addEventListener('click', function(e) {
                if (!input.contains(e.target) && !dropdownOptions.contains(e.target)) {
                    dropdownOptions.classList.remove('show');
                    
                    // If no selection was made and input is not empty, clear it
                    if (input.getAttribute('data-selection-made') === 'false' && input.value.trim() !== '') {
                        input.value = '';
                        select.value = '';
                    }
                }
            });
            
            // Prevent form submission on enter key in search input
            input.addEventListener('keydown', function(e) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    
                    // Select first visible option
                    const firstVisibleOption = dropdownOptions.querySelector('.dropdown-option:not(.hidden)');
                    if (firstVisibleOption) {
                        firstVisibleOption.click();
                    }
                }
            });
        });
        
        // Add form submission validation
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.addEventListener('submit', function(e) {
                const searchInputs = this.querySelectorAll('.search-input');
                let preventSubmit = false;
                
                searchInputs.forEach(input => {
                    if (input.value.trim() !== '' && input.getAttribute('data-selection-made') === 'false') {
                        // User typed something but didn't select from dropdown
                        e.preventDefault();
                        preventSubmit = true;
                        
                        // Add visual feedback
                        input.style.borderColor = 'red';
                        input.style.boxShadow = '0 0 0 1px red';
                        
                        // Show error message
                        let errorMsg = input.parentNode.querySelector('.dropdown-error');
                        if (!errorMsg) {
                            errorMsg = document.createElement('div');
                            errorMsg.className = 'dropdown-error';
                            errorMsg.style.color = 'red';
                            errorMsg.style.fontSize = '12px';
                            errorMsg.style.marginTop = '5px';
                            input.parentNode.appendChild(errorMsg);
                        }
                        errorMsg.textContent = 'الرجاء اختيار قيمة من القائمة المنسدلة';
                    }
                });
                
                if (preventSubmit) {
                    // Scroll to the first error
                    const firstError = document.querySelector('.dropdown-error');
                    if (firstError) {
                        firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }
            });
        });
    }
});