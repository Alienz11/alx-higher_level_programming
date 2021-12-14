#!/usr/bin/node
let num = 0;
/**
 * Logs a message to the console.
 * @item {String} - The message to be logged.
 */
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};
