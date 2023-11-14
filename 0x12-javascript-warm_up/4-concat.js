#!/usr/bin/node

/*
A script that prints two arguments passed to it, in the following format: “ is ”
You must use console.log(...) to print all output
You are not allowed to use var
*/

const argv = process.argv;
// Passed arguments start from index 2 (ie 0 1 2)

const arg1 = argv[2];
const arg2 = argv[3];

//console.log(`${arg1} is ${arg2}`);
console.log('arg1 ' + 'is ' + 'arg2');
