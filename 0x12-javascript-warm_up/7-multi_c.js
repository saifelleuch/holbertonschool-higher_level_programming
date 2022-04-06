#!/usr/bin/node
const convert = parseInt(process.argv[2]);
let i = 0;
if (isNaN(convert) || convert === 0) {
  console.log('Missing number of occurrences');
} else {
  while (i < convert) {
    console.log('C is fun');
    i++;
  }
}
