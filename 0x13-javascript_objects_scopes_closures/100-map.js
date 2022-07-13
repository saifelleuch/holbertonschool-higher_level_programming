#!/usr/bin/node
// imports an array and computes a new array

const list = require('./100-data.js').list;
console.log(list);

let newArray = [];
newArray = list.map((x, i) => x * i);
console.log(newArray);
