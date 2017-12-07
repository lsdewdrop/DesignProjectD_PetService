$(document).ready(function () {
    document.getElementById('register').style.display = 'inline';
    document.getElementById('contents').style.display = 'inline';
    document.getElementById('viewButton').style.display = 'inline';
    document.getElementById('modify_post').style.display = 'none';

});

function modify_page()
{
    document.getElementById('register').style.display = 'none';
    document.getElementById('contents').style.display = 'none';
    document.getElementById('viewButton').style.display = 'none';
    document.getElementById('modify_post').style.display = 'inline';
}