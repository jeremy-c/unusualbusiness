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
    initGrid: initMouseEvents
  };
};

(function() {
  $(document).ready(function() {
    let FeaturedJournal = featuredJournal();
    FeaturedJournal.initGrid();
  });
})();
