/*
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
*/

//This ensures that the code inside the function is executed
//once the HTML document is fully loaded and ready for interaction.
$(function() {
    $('header').css('color', '#FF0000');
});

//This is the extended form of the code above
/*$(document).ready(function() {
  $('header').css('color', '#FF0000');
});
*/
