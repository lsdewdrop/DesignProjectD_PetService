$(document).ready(function () {
    $(function(){
        if (document.location.href!='http://127.0.0.1:5000/search')
        {
            getPostList(1);
        }
        document.getElementById('main').style.display = 'inline';
        document.getElementById('checkbox_wrap').style.display = 'inline';
    });

});

function getPetList()
{
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
            all_html="<option value=\"\">애완동물 선택</option>"

            for(var i=0; i<table.length; i++)
            {
                if(table[i].gender==1)
                {
                    all_html+="<option value=\""+table[i].id+" "+table[i].kinds+" "+table[i].kinds_kinds+" 여\">"+table[i].id+"  "+table[i].kinds+" "+table[i].kinds_kinds+" 여</option>";
                }
                else
                {
                    all_html+="<option value=\""+table[i].id+" "+table[i].kinds+" "+table[i].kinds_kinds+" 남\">"+table[i].id+"  "+table[i].kinds+" "+table[i].kinds_kinds+" 남</option>";
                }

            }
            $("#pet_list").html(all_html);

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

function getPostList(num)
{
     $.ajax
       ({
          type: 'GET',
          headers:
          {
             'Accept': 'application/json',
             'Content-Type': 'application/json'
          },
          url: "/post_list/"+num,
          async: false,

          success: function(result){
            table=result.results;
            all_html=""
            for(var i=0; i<table.length-1; i++)
            {
                all_html+="<tr>";
                all_html+="<th scope=\"row\" align=\"center\">"+table[i].no+"</th>";
                all_html+="<td>"+table[i].kinds+"</td>";
                all_html+="<td>"+table[i].kinds_kinds+"</td>";
                if(table[i].gender==1)
                {
                    all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;여</td>";
                }
                else
                {
                    all_html+="<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;남</td>";
                }

                all_html+="<td><a href=\"/view/"+table[i].no+"\">"+table[i].title+"</a></td>";
                all_html+="<td>"+table[i].auth_id+"</td>";
                all_html+="<td>"+table[i].time+"</td>";
                all_html+="</tr>";
            }

            document.getElementById('main').style.display = 'inline';

            $("#post_list").html(all_html);

            page_html=""
            for(var i =1; i<table[table.length-1]+1; i++)
            {
                page_html+="<label onclick=getPostList("+i+") style=\"padding-right:5px;\">"+i+"</label>"

            }

            $("#page_num").html(page_html);



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


function Btn_write_post()
{
    document.getElementById('checkbox_wrap').style.display = 'none';
    document.getElementById('main').style.display = 'none';
    document.getElementById('write_post').style.display = 'inline';
    getPetList();
}



