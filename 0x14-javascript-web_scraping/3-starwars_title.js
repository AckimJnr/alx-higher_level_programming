#!/usr/bin/node
// make s a GET reqiest to a url
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = Number(process.argv[2]);
const url = baseUrl + movieId;
request(url, (error, response, body) => {
  if (error) console.log(error);
  const movie = JSON.parse(body);
  console.log(movie.title);
});
