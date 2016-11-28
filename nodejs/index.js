var express = require('express');
var app = express();

var com = require("serialport");
var EEm = require('events').EventEmitter;
var emitter = new EEm();

const PORT = "/dev/ttyACM0";

var serialPort = new com(PORT, {
    baudrate: 9600,
    parser: com.parsers.readline('\r\n')
})

serialPort.on('open',function() {
	console.log('Port open');
	emitter.on('open', function(led){
		serialPort.write(led.toString{});
	});
});

serialPort.on('data', function(data) {
	console.log(data);
});

app.use('/public', express.static(__dirname + '/public/'));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/public/index.html');
})

app.listen(3000, function(){
  console.log('listening on *:3000');
});

function sendValue(ledId, color){
	var led = {
		id:ledId, 
		color:color
		toString:function(){
			return led.id+'-'+led.color+'\n';
		}
	};

	emitter.emit('open', led);
}
