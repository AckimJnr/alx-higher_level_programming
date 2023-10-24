#!/usr/bin/node
// make s a GET reqiest to a url
const request = require('request');

if (process.argv >= 3) {
  const url = process.argv[2];

  request(url, (error, response, body) => {
    if (error) console.log(error);

    console.log('code: ' + response.statusCode);
  });
}
