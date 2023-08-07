#!/usr/bin/node

const request = require('request');

const film = process.argv[2];

const fetchCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

const main = () => {
  request.get(`https://swapi-api.alx-tools.com/api/films/${film}`, async (err, _, body) => {
    if (err) {
      console.log(err);
      return;
    }
    try {
      const characters = JSON.parse(body).characters;
      const characterPromises = characters.map(fetchCharacterName);
      const characterNames = await Promise.all(characterPromises);
      console.log(characterNames.join('\n'));
    } catch (error) {
      console.log(error);
    }
  });
};

main();
