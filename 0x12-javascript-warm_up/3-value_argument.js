#!/usr/bin/node
const arg = process.argv[2];
const len = process.argv.length;
if (len === 2) {
  console.log('No argument');
} else {
  console.log(arg);
}
