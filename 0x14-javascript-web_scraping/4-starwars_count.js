#!/usr/bin/node

/*
Write a script that prints the number of movies where the character "Wedge Antilles" is present.
  -The first argument is the API URL of the [Star wars API](https://swapi-api.hbtn.io/): `https://swapi-api.hbtn.io/api/films/`
  -Wedge Antilles is character ID `18` - your script **must** use this ID for filtering the result of the API
  -You must use the module `request`
*/

// Include request module
const request = require('request');

// The first passed argument: url
const apiUrl = process.argv.slice(2)[0];

request(apiUrl, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  // Parse JSON body
  const jsonData = JSON.parse(body);

  // Initialize count
  const count = jsonData.results.reduce((total, movie) => {
    // Check if Wedge Antilles is present in characters list
    if (movie.characters.some(char => char.includes('18'))) {
      return total + 1;
    }
    return total;
  }, 0);

  console.log(count);
});
