jQuery(document).ready(function($) {
   $('#signup').click(function() {
       $.ajax({
           url: '/api/v1/create_user/',
           type: 'POST',
           contentType:"application/json",
           data: JSON.stringify({username: $('#username').val(), password: $('#password').val()}),
           success:function(){
               window.open('/chat_view','_self')
           }
       })
   }) 
});