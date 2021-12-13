#!/usr/bin/node
/**
 * add - Adds the second and third arguments on the command line.
 * @a - second arguments on the command line.
 * @b - third arguments on the command line.
 */

function add (a, b) {
  return a + b;
}

console.log(
  add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]))
);
