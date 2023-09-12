#!/usr/bin/node

const inputA = process.argv[2];

const a = isNaN(parseInt(inputA)) ? 1 : parseInt(inputA);

const factResult = factorial(a);

console.log(factResult);

function factorial (number) {
  if (number <= 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
