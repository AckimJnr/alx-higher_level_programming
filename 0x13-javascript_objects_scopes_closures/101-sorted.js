#!/usr/bin/node
const data = require('./101-data');

const initialDict = data.dict;
const sortedDict = {};

for (const userId in initialDict) {
  const occurrences = initialDict[userId];

  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }

  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
