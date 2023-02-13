const fs = require('fs')
const http = require('http')

const server = http.createServer(function (req, res) {

  // FS=FileSystem
  fs.readFile('./bot.js', function (err, data) {
    res.end("THehosf!")
  })

}).listen(8005, function () {

  console.log('server running at http://127.31.128.93:8005')

})
