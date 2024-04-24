#!/usr/bin/node

/*
Write a script that prints all characters of a Star Wars movie:
  -The first argument is the Movie ID - example: `3` = "Return of the Jedi"
  -Display one character name by line **in the same order of the list "characters" in the `/films/` response**
  -You must use the [Star wars API](https://swapi-api.hbtn.io)
  -You must use the module `request`
*/

const request = require('request');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// Function to fetch character name from URL
function getCharacterName (characterUrl) {
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

// Request film data
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Fetch character names sequentially and print them
  characterUrls.reduce((promiseChain, characterUrl) => {
    return promiseChain.then(() => {
      return getCharacterName(characterUrl)
        .then(characterName => {
          console.log(characterName);
        })
        .catch(error => {
          console.error(error);
        });
    });
  }, Promise.resolve());
});
