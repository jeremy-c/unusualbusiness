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

  function init() {
    console.log('Grid go!');
    initIsotope();
  }

  return {
    init: init
  }
};

export default Grid;
