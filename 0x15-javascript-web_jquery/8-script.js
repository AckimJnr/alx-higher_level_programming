$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const list = $('#list_movies');

    $.each(movies, function (index, movie) {
      const title = $('<li></li>').text(movie.title);
      list.append(title);
    });
  });
});
