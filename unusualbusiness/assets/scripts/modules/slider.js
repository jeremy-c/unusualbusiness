/* ==|====================
   Module/Slider
   ======================= */

'use strict';

import slick from 'slick-carousel';

let Slider = () => {

  let initSlider = function() {

    let featuredArticlesSlickCarouselSettings = {
      centerMode: true,
      centerPadding: '8px',
      dots: true,
      accessibility: true,
      autoplay: true,
      autoplaySpeed: 5000,
      speed: 700,
      responsive: [ {

          breakpoint: 768,
          settings: {
            arrows: false
          }

        }]
    };

    let agendaCarouselSettings = {
      infinite: false,
      slidesToShow: 4,
      slidesToScroll: 1,
      focusOnSelect: true,
      accessibility: true,
      adaptiveHeight: true,
      // the magic
      responsive: [ {

          breakpoint: 1800,
          settings: {
            slidesToShow: 3
          }

        }, {

          breakpoint: 1440,
          settings: {
            slidesToShow: 2
          }

        }, {

          breakpoint: 768,
          settings: {
            slidesToShow: 1
          }

        }]
    };

    let $featuredArticlesCarousel = $('#featured-articles-carousel');
    if($featuredArticlesCarousel.length > 0) {
      $featuredArticlesCarousel.slick(featuredArticlesSlickCarouselSettings);
    }

    let $agendaCarousel = $('#agenda-carousel');
    if($agendaCarousel.length > 0) {
      $agendaCarousel.slick(agendaCarouselSettings);
    }

  };

  let initSlideSwipteEvents = function() {
    // On swipe event
    $('#featured-articles-carousel .slider-holder').on('swipe', function (event, slick, direction) {
      console.log(direction);
      // left
    });
  };

  let init = function () {
    console.log('Slider go!');
    initSlider();
    initSlideSwipteEvents();
  };

  return {
    init: init
  };
};

export default Slider;
