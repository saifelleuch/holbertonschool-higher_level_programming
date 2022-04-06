#!/usr/bin/node
if (typeof (process.argv[2]) !== 'number') {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
