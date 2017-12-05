$(document).ready(function () {
    $(function(){
        getPostList();
        document.getElementById('main').style.display = 'inline';
    });

});

function getPostList()
{
    $.ajax
   ({
      type: 'GET',
      headers:
      {
         'Accept': 'application/json',
         'Content-Type': 'application/json'
      },
      url: "/post_list",
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
      }
   });
}

function write_post()
{
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
      url: "/write_post",
      async: false,
      data: json_data,

      success: function(result){
        register_pet_list()

      },
      statusCode:{
         409:function(msg){
            alert(msg.responseText);
         },
      }
   });
}

function Btn_write_post()
{
    document.getElementById('main').style.display = 'none';
    document.getElementById('write_post').style.display = 'inline';
}