/*
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
*/

const my_header = $('header');
//assign the div tag with id = red_header to a variable for reusability
const red_header = $('DIV#red_header');

red_header.click(function() {
    my_header.css('color', '#FF0000');
})
