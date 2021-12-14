#!/usr/bin/node
/**
 * Reverses an array.
 * @list {Array} - The array to reverse.
 * @returns The reversed array.
 */
exports.esrever = function (list) {
  const n = list.length;
  const reversedList = [];

  for (let i = 0; i < n; i++) {
    reversedList.push(list[n - 1 - i]);
  }
  return reversedList;
};
