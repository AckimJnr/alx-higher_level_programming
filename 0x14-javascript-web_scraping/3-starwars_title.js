#!/usr/bin/node
// make s a GET reqiest to a url
// prints the title of a star wars episode
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  console.log('code: ' + response.statusCode);
	console.log(body)
});
