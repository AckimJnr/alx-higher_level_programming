#!/usr/bin/node
// make s a GET reqiest to a url
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/?id=';
const movieId = Number(process.argv[2]);
const url = baseUrl + movieId;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const movies = JSON.parse(body);

  for (const movie of movies.results) {
    if (movie.episode_id === movieId) {
      console.log(movie.title);
    }
  }
});
