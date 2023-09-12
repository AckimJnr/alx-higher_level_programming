#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  const input = process.argv[2];

  const integerValue = parseInt(input);

  if (!isNaN(integerValue)) {
    for (let i = 0; i < integerValue; i++) console.log('C is fun');
  } else {
    console.log('Not a number');
  }
}
