"use strict";

$(document).ready(function() {
  var boxes = $('.box');

  boxes.on('click', function() {
    var $self = $(this);

    var number = Math.random()*255;

    var messyHex = number.toString(16);

    var realHex = '#' + messyHex.slice(3,9);

    $self.css('background-color', realHex);
  })
})
