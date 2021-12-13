#!/usr/bin/node
const num = Number.parseInt(process.argv[2]);
const alp = "X";
let str = "";


if (Number.isNaN(num) || num === undefined) {
  console.log('Missing size');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      str += alp + "";;
    }
    console.log(str);
  }
}
