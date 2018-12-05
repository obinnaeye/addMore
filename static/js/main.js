$(document).ready(function(){
  $("button").click(function(){
    const title = $("#title").val()
    const description = $("#description").val()
    const client = $("#client").val()
    const product_area = $("#area").val()
    const target_date = $("#date").val()
    const client_priority = $("#priority").val()
    $.ajax({
      type: 'POST',
      url: "http://127.0.0.1:5000/feature-request",
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
        console.log(result)
      }
    });
  });
});