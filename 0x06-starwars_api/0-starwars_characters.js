#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const cast = JSON.parse(body).characters;
    extract(cast, 0);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});

const extract = (cast, i) => {
  if (i === cast.length) {
    return;
  }

  request(cast[i], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }

    try {
      console.log(JSON.parse(body).name);
      extract(cast, i + 1);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}
