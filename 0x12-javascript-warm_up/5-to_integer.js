#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  const input = process.argv[2];

  const integerValue = parseInt(input);

  if (!isNaN(integerValue)) {
    console.log(`My number: ${integerValue}`);
  } else {
    console.log('Not a number');
  }
}
