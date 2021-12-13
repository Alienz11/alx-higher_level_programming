#!/usr/bin/node
const args = process.argv[2];

if (args === undefined) {
  console.log(1);
} else {
  let i = Number.parseInt(args);
  let sum = 0;
  while (i > 0) {
    sum += i;
    i--;
  }
  console.log(sum);
}
