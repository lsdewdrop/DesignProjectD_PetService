

function login(){
    var id = $("#id").val();
    var passwd = $("#password").val();


    data={'id':id, 'passwd': passwd};
    json_data=JSON.stringify(data);

    $.ajax
    ({
        type: 'POST',
        headers:
        {
           'Accept': 'application/json',
           'Content-Type': 'application/json'
        },
        url: '/login_view',
        async: false,
        data: json_data,
        success: function(result){
           location.href="/";
        },
        statusCode:{
            404:function(msg){
                alert(msg.responseText);
            },
            400:function(msg){
                alert(msg.responseText);
            }
		}
    });
}

function signup(){
    var id = $("#user-id").val();
    var username = $("#name").val();
    var passwd = $("#password").val();
    var email = $("#email").val();
    var phoneNum = $("#phone").val();
    var address = $("#address").val();

    data={'username':username, 'passwd': passwd, 'email': email, 'id':id, 'phoneNum':phoneNum, 'address':address};
    json_data=JSON.stringify(data);

    $.ajax
   ({
      type: 'PUT',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: '/signup',
      async: false,
      data: json_data,
      success: function(result){
         alert("signup success");
          location.href="/";
      },
      statusCode:{
         409:function(msg){
            alert(msg.responseText);
         },
         400:function(msg){
            alert(msg.responseText);
         }
      }
   });
}

