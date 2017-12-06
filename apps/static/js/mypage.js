
$(document).ready(function () {
    $(function(){
        getUser();

    });
    $( "#kinds_button" ).change(function() {
      show_kinds_kinds();
    });
});


function getUser()
{
    $.ajax
   ({
      type: 'GET',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: "/getUser",
      async: false,

      success: function(result){
            user=result.results;

            $("#username").html(user.id);
            $("#pro-id").html(user.id);
            $("#pro-name").html(user.username);
            $("#pro-phoneNum").html(user.phoneNum);
            $("#pro-email").html(user.email);
            $("#pro-address").html(user.address);


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

function deleteMyCookie()
{
    var expireDate = new Date();
    var cookieName="pet_session";
    expireDate.setDate( expireDate.getDate() - 1 );
    document.cookie = cookieName + "= " + "; expires=" + expireDate.toGMTString() + "; path=/";
    location.reload('/')
}

function goMain()
{
    $.ajax
   ({
      type: 'GET',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: "/",
      async: false,

      success: function(result){


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

function register_pet_list()
{
    document.getElementById('register_button').style.display = 'inline';
    document.getElementById('register_wrap').style.display = 'none';
    document.getElementById('table_header').style.display = 'inline';
    document.getElementById('default').style.display = 'none';

    $.ajax
   ({
      type: 'GET',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: "/register_list",
      async: false,

      success: function(result){
        table=result.results;
        all_html=""
        for(var i=0; i<table.length; i++)
        {
            all_html+="<tr>";
            all_html+="<th scope=\"row\" align=\"center\">"+(i+1)+"</th>";
            all_html+="<td>"+table[i].kinds+"</td>";
            all_html+="<td>"+table[i].kinds_kinds+"</td>";
            if(table[i].is_free==1)
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O</td>";
            }
            else
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X</td>";
            }

            all_html+="<td>"+table[i].price+"</td>";
            if(table[i].gender==1)
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;남</td>";
            }
            else
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;여</td>";
            }
            if(table[i].is_Neutralization==1)
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O</td>";
            }
            else
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X</td>";
            }

            all_html+="<td>"+table[i].weight+"kg</td>";
            all_html+="<td>"+table[i].height+"cm</td>";
            all_html+="</tr>";
        }

        document.getElementById('table_header').style.display = 'inline';

        $("#list").html(all_html);

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

function print_register_page()
{
    show_kinds();
    document.getElementById('register_button').style.display = 'none';
    document.getElementById('register_wrap').style.display = 'inline';
    document.getElementById('table_header').style.display = 'none';
}





function show_kinds()
{

        $.ajax
       ({
          type: 'GET',
          headers:
          {
             'Accept': 'application/json',
             'Content-Type': 'application/json'
          },
          url: "/show_kinds",
          async: false,

          success: function(result){
            table=result.results;
            all_html="<option value=\"\">선택</option>"
            for(var i=0; i<table.length; i++)
            {
                all_html+="<option value=\""+table[i]+"\">"+table[i]+"</option>";
            }
            $("#kinds_list").html(all_html);

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

function show_kinds_kinds()
{
        var kinds = $("#kinds_list").val();

        data={'kinds':kinds};
        json_data=JSON.stringify(data);

        $.ajax
       ({
          type: 'POST',
          headers:
          {
             'Accept': 'application/json',
             'Content-Type': 'application/json'
          },
          url: "/show_kinds_kinds",
          async: false,
          data: json_data,

          success: function(result){
            table=result.results;
            all_html="<option value=\"\">선택</option>"
            for(var i=0; i<table.length; i++)
            {
                all_html+="<option value=\""+table[i]+"\">"+table[i]+"</option>";
            }
            $("#kinds_kinds_list").html(all_html);

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

function register()
{
    var e = document.getElementById("kinds_list");

    var kinds = e.options[e.selectedIndex].value;

    e = document.getElementById("kinds_kinds_list");
    kinds_kinds = e.options[e.selectedIndex].value;

    //is_free
    var radios = document.getElementsByName('is_free');
    var is_free=""
    for (var i = 0, length = radios.length; i < length; i++)
    {
         if (radios[i].checked)
         {
              is_free=radios[i].value;
              break;
         }
    }

    //price
    var price = $("#price").val();
    if (price=="")
    {
        price=0
    }

    //is_Neutralization
    radios = document.getElementsByName('is_Neutralization');
    var is_Neutralization=""
    for (var i = 0, length = radios.length; i < length; i++)
    {
         if (radios[i].checked)
         {
              is_Neutralization=radios[i].value;
              break;
         }
    }

    //gender
    radios = document.getElementsByName('gender');
    var gender=""
    for (var i = 0, length = radios.length; i < length; i++)
    {
         if (radios[i].checked)
         {
              gender=radios[i].value;
              break;
         }
    }


    //weight
    var weight = $("#weight").val();


    //height
    var height = $("#height").val();

    //helth
    var helth = $("#helth").val();

    data = {'kinds': kinds, 'kinds_kinds': kinds_kinds, 'is_free': is_free,
           'price': price, 'gender': gender, 'is_Neutralization':is_Neutralization, 'weight':weight,
           'height':height,'helth':helth}
    json_data=JSON.stringify(data);

    $.ajax
   ({
      type: 'POST',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: "/register",
      async: false,
      data: json_data,

      success: function(result){
        register_pet_list()

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


function report_list()
{
    document.getElementById('register_button').style.display = 'none';
    document.getElementById('register_wrap').style.display = 'none';
    document.getElementById('table_header').style.display = 'none';
    document.getElementById('default').style.display = 'none';
    document.getElementById('report_wrap').style.display = 'inline';

    $.ajax
   ({
      type: 'GET',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: "/report_my_list",
      async: false,

      success: function(result){
        table=result.results;
        all_html=""
        for(var i=0; i<table.length; i++)
        {
            all_html+="<tr>";
            all_html+="<th scope=\"row\" align=\"center\">"+(i+1)+"</th>";
            all_html+="<td>"+table[i].kinds+"</td>";
            all_html+="<td>"+table[i].kinds_kinds+"</td>";
            if(table[i].is_free==1)
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O</td>";
            }
            else
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X</td>";
            }

            all_html+="<td>"+table[i].price+"</td>";
            if(table[i].gender==1)
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;남</td>";
            }
            else
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;여</td>";
            }
            if(table[i].is_Neutralization==1)
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O</td>";
            }
            else
            {
                all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X</td>";
            }

            all_html+="<td>"+table[i].weight+"kg</td>";
            all_html+="<td>"+table[i].height+"cm</td>";
            all_html+="</tr>";
        }

        document.getElementById('table_header').style.display = 'inline';

        $("#list").html(all_html);

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


function print_reporting_page()
{
    show_report_type();
    document.getElementById('register_button').style.display = 'none';
    document.getElementById('register_wrap').style.display = 'none';
    document.getElementById('table_header').style.display = 'none';
    document.getElementById('register_wrap').style.display = 'inline';
}