/* ==|====================
   Module/Page List
   ======================= */

'use strict';

var pageList = () => {
  let initPageList = function() {
    let $grid = $('.l-grid');
    $grid.imagesLoaded(function() {
      $grid.isotope({
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
    initPageList: initPageList
  };
};

(function() {
  $(document).ready(function() {
    console.log('Page List go!');
    let PageList = pageList();
    PageList.initPageList();
  });
})();
