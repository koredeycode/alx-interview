#!/usr/bin/node

const request = require('request');

const film = process.argv[2];

const main = () => {
  request.get(`https://swapi-api.alx-tools.com/api/films/${film}`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const characters = JSON.parse(body).characters;
    const charactersName = characters.map(
      (url) => new Promise((resolve, reject) => {
        request(url, (perr, _, pbody) => {
          if (perr) {
            reject(perr);
          }
          resolve(JSON.parse(pbody).name);
        });
      })
    );
    Promise.all(charactersName).then(names => console.log(names.join('\n'))).catch(allErr => console.log(allErr));
  });
};
main();
