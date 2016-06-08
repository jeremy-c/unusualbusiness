/* ==|====================
   Module/Grid
   ======================= */

'use strict';

// import imagesLoaded from 'imagesloaded';
// import Isotope from 'isotope-layout';

let Grid = () => {

  let initIsotope = function() {
    let $gridPackery = $('.grid-packery');

    let packerySettings = {
        itemSelector: '.l-grid-item',
        stamp: '.l-stamp',
        layoutMode: 'packery',
        percentPosition: true,
        initLayout: false,
        packery: {
          gutter: '.l-grid-gutter-sizer'
        }
    };

    $gridPackery.isotope(packerySettings);

    // reveal all items after init
    let $packeryItems = $gridPackery.find('.l-grid-item');
    $gridPackery.addClass('is-showing-items').isotope(
        'revealItemElements',
        $packeryItems
    );

    $gridPackery.imagesLoaded(function() {
        $gridPackery.isotope();
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
