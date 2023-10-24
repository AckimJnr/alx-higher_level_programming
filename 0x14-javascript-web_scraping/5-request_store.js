#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Check if both URL and file path are provided as command line arguments
if (process.argv.length < 4) {
  console.log('Usage: node fetchAndStore.js <URL> <file-path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing to the file:', err);
      process.exit(1);
    }
  });
});
