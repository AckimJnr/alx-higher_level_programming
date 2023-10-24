#!/usr/bin/node
// make s a GET reqiest to a url
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/?id=';
const movieId = process.argv[2];
const url = baseUrl + movieId;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const movieData = JSON.parse(body);
  console.log(movieData.results[0].title);
});
