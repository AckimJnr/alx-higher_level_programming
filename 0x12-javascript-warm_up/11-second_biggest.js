#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const integers = args.map(Number);
  const uniqueIntegers = [...new Set(integers)];

  const sortedIntegers = uniqueIntegers.sort((a, b) => b - a);

  console.log(sortedIntegers[1]);
}
