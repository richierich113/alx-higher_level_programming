/*
Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API.
*/

const movie_list = $('ul#list_movies');
apiUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";

$.getJSON(apiUrl, function(data) {
    const data_list = data.results;
    const data_list_num = data.results.length;
    console.log(data_list_num);
    for (let i = 0; i < data_list_num; i++) {
        movie_list.append("<li>" + data_list[i].title + "</li>");
    }
});


/*
Alternate solution that works as well
$(document).ready(function () {
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        type: "GET",
        dataType: "json",
        success: function (data) {
            console.log(data);
            for (let i = 0; i < data.results.length; i++) {
                $("#list_movies").append("<li>" + data.results[i].title + "</li>");
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
});
*/
