$(document).ready(function () {
  $(".delete-review-button").click(function (e) {
      e.preventDefault();
      var reviewId = $(this).data("review-id");
      $.ajax({
          type: "POST",
          url: "{% url 'delete_review' review.id %}",
          data: {
              csrfmiddlewaretoken: "{{ csrf_token }}",
          },
          success: function (data) {
              if (data.status === "success") {
                  // Handle success, e.g., display a success message and update the page.
                  alert("Review deleted successfully!");
              } else {
                  // Handle errors, e.g., display an error message.
                  alert("Error deleting review: " + data.message);
              }
          },
          error: function () {
              // Handle AJAX error, e.g., display a generic error message.
              alert("An error occurred while processing your request.");
          },
      });
  });
});
