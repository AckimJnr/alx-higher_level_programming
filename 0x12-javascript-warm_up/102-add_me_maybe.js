#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  const incrementedNum = number + 1;
  theFunction(incrementedNum);
}

module.exports.addMeMaybe = addMeMaybe;
