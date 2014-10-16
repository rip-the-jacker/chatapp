var transport = WebSocket;
var endpoint = 'ws://localhost:4242/ec';
var connection = new Omnibus(transport, endpoint);
var channel = connection.openChannel('chatapp')
channel.on('new_msg', function(event) {
  var message = event.data.payload.text;
  var user = event.data.payload.username;
  $('#chat_area').append('<div><span>'+user+'</span>:<span>'+message+'</span><div>');
});