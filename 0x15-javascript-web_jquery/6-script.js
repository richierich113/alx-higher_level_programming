/*
Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
*/

const my_header = $('header');
const update_header = $('DIV#update_header');

update_header.click(function() {
    my_header.text('New Header!!!');
});
