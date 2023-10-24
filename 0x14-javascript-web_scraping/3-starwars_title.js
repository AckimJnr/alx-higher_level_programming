#!/usr/bin/node
// make s a GET reqiest to a url
const request = require('request');

const baseUrl = "https://swapi-api.alx-tools.com/api/films/?id=";       
request(url, (error, response, body) => {
  if (error) console.log(error);
  console.log('code: ' + response.statusCode);
        console.log(body);
});
