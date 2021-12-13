#!/usr/bin/node
const args = process.argv[2];
const words = 'C is fun';

let i = 0;
while (i < args) {
  console.log(words);
  i++;
}
