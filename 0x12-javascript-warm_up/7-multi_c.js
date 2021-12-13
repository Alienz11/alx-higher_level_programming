#!/usr/bin/node
const args = process.argv[2];
const words = 'C is fun';

if (Number.isNaN(args) || args === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < args) {
    console.log(words);
    i++;
  }
}
