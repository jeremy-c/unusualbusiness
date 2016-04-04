/* ==|====================
   Module/Page List
   ======================= */

'use strict';

var pageList = () => {
  let initPageList = function() {
    $('.l-grid').isotope({
      // set itemSelector so .grid-sizer is not used in layout
      itemSelector: '.l-grid-item',
      percentPosition: true,
      masonry: {
        // use element for option
        columnWidth: '.l-grid-sizer',
        gutter: '.l-grid-gutter-sizer'
      }
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
