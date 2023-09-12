#!/usr/bin/node

const inputA = process.argv[2];
const inputB = process.argv[3];

const a = parseInt(inputA);

const b = parseInt(inputB);

console.log(add(a, b));

function add (a, b) {
  return a + b;
}
