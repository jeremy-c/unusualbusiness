/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

console.log('Hello, World!');

var mainMenu = () => {
  let toggleEyebrows = function() {
    let howToEyebrow = $(this).children().first();
    let howToEye = howToEyebrow.siblings().first();

    howToEyebrow.toggleClass('is-hidden');
    howToEye.toggleClass('is-hidden');

    console.log('done');
  };

  let initMouseEvents = function() {
    let howToLink = $('.how-to-link');
    howToLink.on('mouseenter', toggleEyebrows);
    howToLink.on('mouseleave', toggleEyebrows);
  };

  return {
    initMouseEvents: initMouseEvents
  };
};

var featuredAgenda = () => {
  let initMouseEvents = function() {
    let agendaItemLink = $('.featured-agenda-item-link');

    agendaItemLink.on('mouseover', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.addClass('is-hover');
    });
    agendaItemLink.on('mouseout', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.removeClass('is-hover');
    });
  };

  return {
    initMouseEvents: initMouseEvents
  };
};

var featuredArticles = () => {
  let initSlider = function() {
    $('.slider').unslider({
      keys: false,
      arrows: false,
      nav: true
    });
  };

  return {
    initSlider: initSlider
  };
};

(function() {
  $(document).ready(function() {
    let MainMenu = mainMenu();
    MainMenu.initMouseEvents();

    let FeaturedArticles = featuredArticles();
    FeaturedArticles.initSlider();

    let FeaturedAgenda = featuredAgenda();
    FeaturedAgenda.initMouseEvents();
  });
})();
