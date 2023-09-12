#!/usr/bin/node

const argLength = process.argv.length;

if (argLength > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
