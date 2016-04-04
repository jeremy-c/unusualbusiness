/* ==|====================
   Module/Page List
   ======================= */

'use strict';

var pageList = () => {
  let initPageList = function() {
    $('.page-list').isotope({
      // set itemSelector so .grid-sizer is not used in layout
      itemSelector: '.page-list-item',
      percentPosition: true,
      masonry: {
        // use element for option
        columnWidth: '.grid-sizer',
        gutter: 40
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
