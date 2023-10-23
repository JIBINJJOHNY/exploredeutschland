$(document).ready(function () {
    $("#rating").rateYo({
        starWidth: "20px",  // Customize the star size as needed
        rating: 0,          // Initial rating (0 by default)
        ratedFill: "#FFD700",  // Fill color for rated stars
        normalFill: "#A0A0A0",  // Fill color for normal stars
        halfStar: true,    // Allow half stars
        onSet: function (rating, rateYoInstance) {
            // Set the value of the hidden input field to the selected rating
            $("#rating_input").val(rating);
        }
    });
});
