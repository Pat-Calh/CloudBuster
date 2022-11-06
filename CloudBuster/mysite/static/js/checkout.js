function refresh()
{
  $("#movies").html("<tr><td>Title:</td><td style='padding-left:5em'>Stock:</td><td style='padding-left:5em'>Checked out:</td><td style='padding-left:5em'>Select:</td></tr>");
  $.get("/checkoutHandler").done(function(data){
    for (i=0;i<data.length;i++)
    {
      $("#movies").append("<tr><td>"+data[i].title+"</td><td style='padding-left:5em'>"+data[i].inStock+"</td><td style='padding-left:5em'>"+data[i].total+"</td><td style='padding-left:5em'><input type='radio' name='movieRadio' value="+data[i].title+"></td></tr>");
    }
  });
}

$(function(){
  refresh()
  $("#submit").bind("click", function(){
    $.post("/checkout/",{"email":$("#email").val()},
      function(data){
        exists = data.exists;
        if(exists=="true"){
            $("#user").html("<tr><td>First Name:</td><td style='padding-left:2em'>Last Name:</td><td style='padding-left:2em'>Checked Out Movies:</td></tr>"); 
            $("#user").append("<tr><td>"+data.fName+"</td><td style='padding-left:2em'>"+data.lName+"</td><td style='padding-left:2em'>"+data.movies+"</td></tr>");
        }else{
          $("#user").html("<h1 style='color:red'>Account does not exist</h1>")
          $("#user").append("<a href='/account/'>Create new account?</a>")
        }
      }
    );
  });
});


$(function(){
  $("#button").bind("click", function(){
    var radioValue = $("input[name='movieRadio']:checked").val();
    $.post("/checkoutHandler/",{"email":$("#email").val(), "movie":radioValue},
      function(data){
        exists = data.exists;
        if(exists=="true"){
            $("#user").html("<tr><td>First Name:</td><td style='padding-left:2em'>Last Name:</td><td style='padding-left:2em'>Checked Out Movies:</td></tr>"); 
            $("#user").append("<tr><td>"+data.fName+"</td><td style='padding-left:2em'>"+data.lName+"</td><td style='padding-left:2em'>"+data.movies+"</td></tr>");
        }else{
          $("#user").html("<h1 style='color:red'>Account does not exist</h1>")
          $("#user").append("<a href='/account/'>Create new account?</a>")
        }
      }
    );
  });
});

