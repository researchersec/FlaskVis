var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    console.log('Websocket connected!');
});

socket.on('update_data', function(data) {
    // Update chart data here
});
