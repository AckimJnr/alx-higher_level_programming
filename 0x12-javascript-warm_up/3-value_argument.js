#!/usr/bin/node

let argLen = 0;

while (process.argv[argLen]) argLen++;

if (argLen > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
