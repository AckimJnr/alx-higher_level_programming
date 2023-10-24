#!/usr/bin/node
// reads the contents of a file
const fs = require('fs');
if (process.argv.length >= 3) {
  const filepath = process.argv[2];

  fs.readFile(filepath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
