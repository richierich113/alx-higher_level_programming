#!/usr/bin/node

/*
Write a script that prints all characters of a Star Wars movie:
  -The first argument is the Movie ID - example: `3` = "Return of the Jedi"
  -Display one character name per line
  -You must use the [Star wars API](https://swapi-api.hbtn.io)
  -You must use the module `request`
*/

// Include request module
const request = require('request');

// Function to get character info
function getCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(`Failed to fetch character data (${response.statusCode})`);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

// The first passed argument: movieID
const movieID = process.argv.slice(2)[0];

// URL of the movie
const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieID}`;

// Request movie data
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  // Parse JSON body
  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Print characters sequentially
  Promise.all(characterUrls.map(getCharacter))
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => {
      console.error(error);
    });
});
