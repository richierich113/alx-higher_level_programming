/*
Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:

The <header> element must always have one class: red or green, never both in the same time and never empty.
If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
*/

const my_header = $('header');
const toggle_header = $('DIV#toggle_header'); //Selectors are case insensitive so DIV can be div or DiV or dIV etc

toggle_header.click(function() {
    if (my_header.hasClass('red')) {
        my_header.removeClass('red');
        my_header.addClass('green');
    } else {
        my_header.removeClass('green');
        my_header.addClass('red');
    }
});
