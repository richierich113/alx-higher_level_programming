/*
Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
*/

const my_header = $('header');
const red_header = $('div#red_header');

red_header.click(function () {
    my_header.addClass('red');
});
