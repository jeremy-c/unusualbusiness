/* ==|====================
   Module/Featured Article
   ======================= */

'use strict';

var featuredJournal = () => {
  let toggleOverlay = function() {
    let overlayElement = $(this).find('.featured-journal-overlay');
    overlayElement.toggleClass('is-hidden');
  };

  let initMouseEvents = function() {
    let calloutLink = $('.featured-journal-link');

    calloutLink.on('mouseover', toggleOverlay);
    calloutLink.on('mouseout', toggleOverlay);
  };

  return {
    initMouseEvents: initMouseEvents
  };
};

(function() {
  $(document).ready(function() {
    console.log('Featured Journal go!');
    let FeaturedJournal = featuredJournal();
    FeaturedJournal.initMouseEvents();
  });
})();