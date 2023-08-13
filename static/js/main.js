// main.js
$(document).ready(function() {
  // Animate the story boxes on hover
  $(".story-box").hover(function() {
    $(this).addClass("hovered");
  }, function() {
    $(this).removeClass("hovered");
  });

  // Add click event for the buttons
  $(".btn-comment").click(function() {
    // Add your comment functionality here
    alert("Comment button clicked!");
  });

  $(".btn-like").click(function() {
    // Add your like functionality here
    alert("Like button clicked!");
  });

  $(".btn-share").click(function() {
    // Add your share functionality here
    alert("Share button clicked!");
  });
});
