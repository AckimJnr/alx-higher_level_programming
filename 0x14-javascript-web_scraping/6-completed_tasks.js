#!/usr/bin/node
// counts completed tasks
const request = require('request');
const apiUrl = process.argv[2];

// Make a GET request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    process.exit(1);
  }

  const todos = JSON.parse(body);

  const completedTasks = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasks[userId]) {
        completedTasks[userId]++;
      } else {
        completedTasks[userId] = 1;
      }
    }
  });
  console.log(completedTasks);
});
