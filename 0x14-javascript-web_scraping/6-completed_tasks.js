#!/usr/bin/node

/*
Write a script that computes the number of tasks completed by user id.
  -The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
  -Only print users with completed task
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
  const todos = JSON.parse(body);

  // Filter completed tasks and compute counts by user ID
  const completedTasksByUser = todos.reduce((acc, todo) => {
    if (todo.completed) {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
    }
    return acc;
  }, {});

  console.log(completedTasksByUser);
});
