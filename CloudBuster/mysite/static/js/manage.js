function refresh()
{
  $("#movies").html("<tr><td>Title:</td><td style='padding-left:5em'>In-Stock:</td><td style='padding-left:5em'>Checked Out:</td></tr>");
  $.get("/manageHandler").done(function(data){
    for (i=0;i<data.length;i++)
    {
      $("#movies").append("<tr><td>"+data[i].title+"</td><td style='padding-left:5em'>"+data[i].inStock+"</td><td style='padding-left:5em'>"+data[i].total+"</td><td><input id='button' type='button' name='"+data[i].title+"' value='-'/></td><td><input id='button' name='"+data[i].title+"' type='button' value='+'/></td></tr>");
    }
  });
}

$(function(){
  refresh();
  $("#submit").bind("click", function(){
    $.post("/manageHandler/",{"add":$("#add").val()},
    function(data){
      $("#error").html(data.error);
      refresh();
    }
    );
  });
});

$(function(){
  //TODO: Fix/Figure out why generated table buttons wont click.
  $("#button").bind("click", function(){
    $.post("/manageStock/",{"add":$("#add").val()},
    function(data){
      $("#error").html(data.error);
      refresh();
    }
    );
  });
});






