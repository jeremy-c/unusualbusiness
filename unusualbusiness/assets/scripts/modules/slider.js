/* ==|====================
   Module/Slider
   ======================= */

'use strict';

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
      slidesToShow: 3,
      slidesToScroll: 1,
      asNavFor: '#agenda-carousel-preview',
      focusOnSelect: true,
      accessibility: true,
      adaptiveHeight: true,
      // the magic
      responsive: [ {

          breakpoint: 1800,
          settings: {
            slidesToShow: 2
          }

        }, {

          breakpoint: 1024,
          settings: {
            slidesToShow: 1
          }

        }]
    };

    let agendaPreviewCarouselSettings = {
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '#agenda-carousel',
      infinite: false,
      accessibility: false
    };

    if($.fn.slick !== undefined) {
      $('#featured-articles-carousel').slick(featuredArticlesSlickCarouselSettings);
      $('#agenda-carousel').slick(agendaCarouselSettings);
      $('#agenda-carousel-preview').slick(agendaPreviewCarouselSettings);
    }
  };

  let init = function () {
    console.log('Featured Articles go!');
    initSlider();
  };

  return {
    init: init
  };
};

export default Slider;
