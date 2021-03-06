$(document).ready(function(){
  function error_display(title, description, priority, target_date) {
    $("small").hide();
    if (!title) {
      $("#title-error").show()
    }
    if (!description) {
      $("#description-error").show()
    }
    if (!priority) {
      $("#priority-error").show()
    }
    if (!target_date) {
      $("#date-error").show()
    }

    const deadline = new Date(target_date);
    const today   = new Date();
    if (deadline <= today) {
      $("#date-error").show()
    }


  }
  $("#submit").click(function(){
    const title = $("#title").val().trim()
    const description = $("#description").val().trim()
    const client = $("#client").val()
    const product_area = $("#area").val()
    const target_date = $("#date").val()
    const client_priority = $("#priority").val().trim()
    if (!title || !description || !client || !target_date) {
      error_display(title, description, client_priority, target_date)
    } else {
      const origin = window.location.origin;
      $.ajax({
        type: 'POST',
        url: origin + "/feature-request",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({
          Title: title, 
          Description: description,
          ClientID: client,
          ProductArea: product_area,
          TargetDate: target_date,
          ClientPriority: client_priority
        }),
        success: function(result){
          $(".screen-cover").css('display', 'flex');
          $(window).scrollTop(0);
        }
      });
    }
  });

  $("#dismiss").click(function() {
    $(".screen-cover").css('display', 'none');
  });
});