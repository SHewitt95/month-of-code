"use strict";

$(document).ready(function() {

  var pr_button = $('#programmer-button'),
      jr_button = $('#journalist-button'),
      written = $('#written-work'),
      items = $('#item-box');

  written.hide();

  pr_button.on('click', function() {
    written.hide();
    items.show();
  })

  jr_button.on('click', function() {
    items.hide();
    written.show();
  })

})
