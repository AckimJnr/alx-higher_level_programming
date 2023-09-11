#!/usr/bin/node

const numArguments = process.argv.length - 2;

if (numArguments === 0) {
  printMessage('No argument');
} else if (numArguments === 1) {
  printMessage('Argument found');
} else {
  printMessage('Arguments found');
}

function printMessage (message) {
  console.log(message);
}
