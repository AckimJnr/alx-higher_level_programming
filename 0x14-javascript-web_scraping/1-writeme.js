#!/usr/bin/node
// Write input data to a file
const fs = require('fs');

if (process.argv.length >= 4) {
  const filepath = process.argv[2];
  const content = process.argv[3];

  fs.writeFile(filepath, content, err => {
    if (err) {
      console.error(err);
    }
  });
}
