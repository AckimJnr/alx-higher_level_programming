#!/usr/bin/node

const input = process.argv[2];

const integerValue = parseInt(input);

if (!isNaN(integerValue)) {
  for (let i = 0; i < integerValue; i++) {
    for (let j = 0; j < integerValue; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
