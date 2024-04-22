document.addEventListener('DOMContentLoaded', function() {
    const bookButtons = document.querySelectorAll('.book-button');
    const modal = document.getElementById('booking-modal');
    const closeModalButton = modal.querySelector('.close');

    // Event listener for book buttons
    bookButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const trainId = button.getAttribute('data-train-id');
            // Perform booking confirmation here (AJAX request, form submission, etc.)
            // For demonstration purposes, just show the booking modal
            modal.style.display = 'block';
        });
    });

    // Event listener to close the modal
    closeModalButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Close modal if user clicks outside of it
    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
    
    // Optional: Event listener for form submission
    document.getElementById('booking-form').addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the form from submitting
        
        // Your booking logic here
        
        // Show the confirmation message
        document.getElementById('confirmation-message').style.display = 'block';
    });
});
