// train_details.js
document.addEventListener('DOMContentLoaded', function() {
    // Fetch random train details from the server
    fetch('/get_random_train/')
        .then(response => response.json())
        .then(data => {
            // Display train details
            document.getElementById('train-title').innerText = data.trainTitle;
            document.getElementById('dept-info').innerText = `${data.deptTiming} ${data.deptStation} ${data.deptDate}`;
            document.getElementById('des-info').innerText = `${data.desTiming} ${data.desStation} ${data.desDate}`;
        })

        .catch(error => console.error('Error fetching train details:', error));
        document.getElementById('booking-form').addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent the form from submitting
            
            // Your booking logic here
            
            // Show the confirmation message
            document.getElementById('confirmation-message').style.display = 'block';
        });
});
