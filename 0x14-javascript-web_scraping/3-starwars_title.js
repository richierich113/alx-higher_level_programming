#!/usr/bin/node

/*
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
    -The first argument is the movie ID
    -You must use the [Star wars API](https://swapi-api.hbtn.io/) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`
    -You must use the module `request`
*/

// Include request module
const request = require('request');

// The first passed argument: movieID
const movieID = process.argv.slice(2)[0];

// URL to be requested
const url = `https://swapi-api.hbtn.io/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  // Check if status code is 200 (OK)
  if (response.statusCode !== 200) {
    return console.error(`Error: Status code ${response.statusCode}`);
  }
  // Parse JSON body and print movie title
  const movie = JSON.parse(body);
  console.log(movie.title);
});
