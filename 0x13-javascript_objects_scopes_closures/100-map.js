#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);

let newArr = [];
newArr = list.map((x, i) => x * i);
console.log(newArr);
