$(document).ready(function () {
  $(".delete-image-button").click(function (e) {
      e.preventDefault();
      var imageId = $(this).data("image-id");
      var reviewId = $(this).data("review-id");
      $.ajax({
          type: "POST",
          url: "{% url 'delete_image' review.id image.id %}",
          data: {
              csrfmiddlewaretoken: "{{ csrf_token }}",
          },
          success: function (data) {
              if (data.status === "success") {
                  // Handle success, e.g., display a success message and update the page.
                  alert("Image deleted successfully!");
              } else {
                  // Handle errors, e.g., display an error message.
                  alert("Error deleting image: " + data.message);
              }
          },
          error: function () {
              // Handle AJAX error, e.g., display a generic error message.
              alert("An error occurred while processing your request.");
          },
      });
  });
});
