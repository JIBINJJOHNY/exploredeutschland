$(document).ready(function () {
  $("form#uploadImage").submit(function (e) {
      e.preventDefault();
      var formData = new FormData($(this)[0]);
      $.ajax({
          type: "POST",
          url: "{% url 'upload_image' review.id %}",
          data: formData,
          processData: false,
          contentType: false,
          success: function (data) {
              if (data.status === "success") {
                  // Handle success, e.g., display a success message and update the page.
                  alert("Image uploaded successfully!");
              } else {
                  // Handle errors, e.g., display an error message.
                  alert("Error uploading image: " + data.message);
              }
          },
          error: function () {
              // Handle AJAX error, e.g., display a generic error message.
              alert("An error occurred while processing your request.");
          },
      });
  });
});
