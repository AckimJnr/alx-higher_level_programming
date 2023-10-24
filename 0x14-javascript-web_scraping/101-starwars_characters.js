#!/usr/bin/node
const request = require('request');

// Check if the Movie ID is provided as a command line argument
if (process.argv.length < 3) {
  console.log('Usage: node starWarsCharacters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Define the Star Wars API URL for the movie with the provided ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the API to get information about the movie
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);

  if (movieData.characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  // Iterate through the character URLs in the same order as listed in the film response
  const characterUrls = movieData.characters;

  const printCharacter = (index) => {
    if (index >= characterUrls.length) {
      return;
    }

    const characterUrl = characterUrls[index];
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
      } else if (charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
        printCharacter(index + 1); // Continue to the next character
      }
    });
  };

  // Start printing characters from the first character URL
  printCharacter(0);
});
