#!/usr/bin/node

/*
Write a script that reads and prints the content of a file.
  -The first argument is the file path
  -The content of the file must be read in `utf-8`
  -If an error occurred during the reading, print the error object
  (In the format below)
*/

// Include fs module
const fs = require('fs');

// The first passed argument: filePath
const filePath = process.argv.slice(2)[0];

// Use fs.readFile() method to read file
fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
