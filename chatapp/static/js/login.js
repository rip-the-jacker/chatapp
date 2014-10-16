jQuery(document).ready(function($) {
   $('#login').click(function() {
       $.ajax({
           url: '/api/v1/user/login/',
           type: 'POST',
           contentType:"application/json",
           data: JSON.stringify({username: $('#username').val(), password: $('#password').val()}),
           success:function(){
               window.open('/chat_view','_self')
           }
       })
   }) 
});