$('#review-form').on('submit', function(event) {
    event.preventDefault();
    if (userIsAuthenticated) { // Replace 'userIsAuthenticated' with your logic to check if the user is authenticated
        $.ajax({
            type: 'POST',
            url: '/add_review/',
            data: $(this).serialize(),
            success: function(data) {
                if (data.status === 'success') {
                    // Refresh the review list or update it with the new review.
                    // Example: Load the list of reviews again using AJAX.
                } else {
                    // Handle the error.
                }
            }
        });
    } else {
        // Display a message or modal asking the user to log in.
    }
});
