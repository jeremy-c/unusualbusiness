/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

console.log('Hello, World!');

var featuredAgenda = () => {
  let initMouseEvents = function() {
    let agendaItemLink = $('.featured-agenda-item-link');

    agendaItemLink.on('mouseover', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.addClass('is-hovered');
    });
    agendaItemLink.on('mouseout', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.removeClass('is-hovered');
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
    let FeaturedArticles = featuredArticles();
    FeaturedArticles.initSlider();

    let FeaturedAgenda = featuredAgenda();
    FeaturedAgenda.initMouseEvents();
  });
})();
