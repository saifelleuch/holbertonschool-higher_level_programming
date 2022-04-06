#!/usr/bin/node
let convert = parseInt(process.argv[2]);
let i = 0;
if (isNaN(convert) || convert === 0) {
    console.log('Missing number of occurrences');
} else if (convert < 0) {
    return;
} else {
    while (i < convert) {
        console.log('C is fun');
        i++;
    }
}