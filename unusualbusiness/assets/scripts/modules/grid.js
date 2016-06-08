/* ==|====================
   Module/Grid
   ======================= */

'use strict';

// import imagesLoaded from 'imagesloaded';
// import Isotope from 'isotope-layout';

let Grid = () => {

    let delayMe = function() {
        $('.grid-masonry').isotope();
        console.log('isotoped');
    };
  let initIsotope = function() {
    let masonrySettings = {
        itemSelector: '.l-grid-item',
        stamp: '.l-stamp',
        percentPosition: true,
        masonry: {
          columnWidth: '.l-grid-sizer',
          gutter: '.l-grid-gutter-sizer'
        }
      };

    let packerySettings = {
        itemSelector: '.l-grid-item',
        stamp: '.l-stamp',
        layoutMode: 'packery',
        percentPosition: true,
        packery: {
          gutter: '.l-grid-gutter-sizer'
        }
      };

    $('.grid-masonry').imagesLoaded(function() {
      $('.grid-masonry').isotope(masonrySettings);
    });

    $('.grid-packery').imagesLoaded(function() {
      $('.grid-packery').isotope(packerySettings);
    });
  };

  let toggleHoverClass = function() {
    let overlayElement = $(this).parent().toggleClass('is-hovered');
  };

  let initHoverStates = function() {
    let gridLink = $('.l-grid-item a');

    gridLink.on('mouseover', toggleHoverClass);
    gridLink.on('mouseout', toggleHoverClass);
  };

  function init() {
    console.log('Grid go!');
    initIsotope();
    initHoverStates();
  }

  return {
    init: init
  }
};

export default Grid;
