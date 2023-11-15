#!/usr/bin/node
const num = process.argv[2];
const display = () => {
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
};
isNaN(num)
  ? (console.log('Missing number of occurences'))
  : (display());
