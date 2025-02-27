// Sample node.js web app for Pluralsight Docker CI course
// For demonstration purposes only
'use strict';
const path = require('path');

var express = require('express'),
    app = express();

app.set('views', 'views');
app.set('view engine', 'pug');

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(8080);
module.exports.getApp = app;
