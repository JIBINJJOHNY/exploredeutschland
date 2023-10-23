$(document).ready(function () {
  $("form#editReview").submit(function (e) {
      e.preventDefault();
      var formData = new FormData($(this)[0]);
      $.ajax({
          type: "POST",
          url: "{% url 'edit_review' review.id %}",
          data: formData,
          processData: false,
          contentType: false,
          success: function (data) {
              if (data.status === "success") {
                  // Handle success, e.g., display a success message and update the page.
                  alert("Review updated successfully!");
              } else {
                  // Handle errors, e.g., display an error message.
                  alert("Error updating review: " + data.message);
              }
          },
          error: function () {
              // Handle AJAX error, e.g., display a generic error message.
              alert("An error occurred while processing your request.");
          },
      });
  });
});
