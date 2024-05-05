/*
Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
When the user clicks on DIV#add_item: a new element is added to the list
When the user clicks on DIV#remove_item: the last element is removed from the list
When the user clicks on DIV#clear_list: all elements of the list are removed
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
You script must work when it imported from the HEAD tag
*/

// $(function() is the short form of $(document).ready(function()
$(function() {

    const addItem = $('DIV#add_item');
    const removeItem = $('DIV#remove_item');
    const clearList = $('DIV#clear_list');
    const list = $('UL.my_list');
    const allListItems = $('UL.my_list > li');

    
    addItem.click(function(){
        list.append("<li>Item</li>");
    });

    removeItem.click(function(){
        list.children().last().remove();
    });

    clearList.click(function(){
        list.empty();
    });

});
