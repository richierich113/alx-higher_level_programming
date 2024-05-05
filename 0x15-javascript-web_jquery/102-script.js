/*
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate
The translation of “Hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
You script must work when imported from the <head> tag
*/

$(document).ready(function () {
    // Select the translate button and the input field using jQuery
    const translateButton = $("INPUT#btn_translate");
    const helloDiv = $("div#hello");

    // Attach a click event listener to the translate button
    translateButton.click(function () {
        // Retrieve the language code from the input field
        const languageCode = $("INPUT#language_code").val();

        // Construct the API URL with the language code
        const apiUrl = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;

        // Make a GET request to the API
        $.get(apiUrl, function (data) {
            // Update the text of the helloDiv with the translation
            helloDiv.text(data.hello);
        });
    });
});
