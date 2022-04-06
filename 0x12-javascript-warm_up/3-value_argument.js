#!/usr/bin/node
const arg = process.argv[2];
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
