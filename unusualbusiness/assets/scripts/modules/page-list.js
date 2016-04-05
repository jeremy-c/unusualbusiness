/* ==|====================
   Module/Page List
   ======================= */

'use strict';

var pageList = () => {
  let grid = $('.l-grid');

  let initPageList = function() {
    grid.imagesLoaded(function() {
      grid.isotope({
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

  return {
    initPageList: initPageList,
    grid: grid
  };
};

(function() {
  $(document).ready(function() {
    console.log('Page List go!');
    let PageList = pageList();
    PageList.initPageList();
  });
})();
