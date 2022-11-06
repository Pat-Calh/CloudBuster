$(function(){
  $("#submit").bind("click", function(){
    $.post("/accountHandler/",{"fName":$("#fName").val(),"lName":$("#lName").val(),"email":$("#email").val()},
      function(data){
        success = data.success;
        var msg = "<h4 style='color:red'>Account already exists</h4>";
        if(success=="true"){
          msg = "<h4 style='color:blue'>Account successfully created</h4>";          
        }
        $("#msg").html("<h2 style='color:red'>"+msg+"</h2>");
      }
    );
  });
});