$(document).ready(function () {
   ft_more();
});

function ft_more() {
   $(".icon_view").click(function () {
      $(".ft_more_area").show();
      $(".toggle_btn ").addClass("icon_hide");
      $(".toggle_btn ").removeClass("icon_view");
   });
   $(".icon_hide").click(function () {
      $(".ft_more_area").hide();
      $(".toggle_btn ").addClass("icon_view");
      $(".toggle_btn ").removeClass("icon_hide");
   });
}