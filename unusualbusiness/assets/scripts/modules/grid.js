/* ==|====================
   Module/Grid
   ======================= */

'use strict';

// import imagesLoaded from 'imagesloaded';
// import Isotope from 'isotope-layout';

let Grid = () => {
  let initIsotope = function() {
    $('.l-grid').imagesLoaded(function() {
      $('.l-grid').isotope({
        itemSelector: '.l-grid-item',
        percentPosition: true,
        masonry: {
          // use element for option
          columnWidth: '.l-grid-sizer',
          gutter: '.l-grid-gutter-sizer'
        }
      });
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
