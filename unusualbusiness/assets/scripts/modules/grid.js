/* ==|====================
   Module/Grid
   ======================= */

'use strict';

// import imagesLoaded from 'imagesloaded';
// import Isotope from 'isotope-layout';

let Grid = () => {

  let initIsotope = function() {
    let $gridPackery = $('.grid-packery');
    let $gridMasonry = $('.grid-masonry');

    let packerySettings = {
        itemSelector: '.l-grid-item',
        stamp: '.l-stamp',
        percentPosition: true,
        initLayout: false,
        packery: {
          gutter: '.l-grid-gutter-sizer'
        }
    };

    let masonrySettings = {
        itemSelector: '.l-grid-item',
        initLayout: false,
        masonry: {
            columnWidth: 459,
            fitWidth: true
        }
    };

    $gridPackery.isotope(packerySettings);
    $gridMasonry.isotope(masonrySettings);

    // reveal all items after init
    let $items = $gridPackery.find('.l-grid-item');
    $gridPackery.addClass('is-showing-items').isotope('revealItemElements', $items);
    $gridMasonry.addClass('is-showing-items').isotope('revealItemElements', $items);

    $gridPackery.imagesLoaded(function() {
        $gridPackery.isotope();
    });

    $gridMasonry.imagesLoaded(function() {
        $gridMasonry.isotope();
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
