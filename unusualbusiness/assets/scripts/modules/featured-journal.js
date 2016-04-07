/* ==|====================
   Module/Featured Article
   ======================= */

'use strict';

let FeaturedJournal = () => {
  let toggleOverlay = function() {
    let overlayElement = $(this).find('.featured-journal-overlay');
    overlayElement.toggleClass('is-hidden');
  };

  let initMouseEvents = function() {
    let calloutLink = $('.featured-journal-link');

    calloutLink.on('mouseover', toggleOverlay);
    calloutLink.on('mouseout', toggleOverlay);
  };

  let init = function() {
    console.log('Featured Journal go!');
    initMouseEvents();
  };

  return {
    init: init
  };
};

export default FeaturedJournal
