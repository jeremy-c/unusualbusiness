/* ==|====================
   Module/Page List
   ======================= */

'use strict';

let gridModule = () => {
  let grid = $('.l-grid');

  let initGrid = function() {
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
    initGrid: initGrid,
    grid: grid
  };
};

(function() {
  $(document).ready(function() {
    console.log('Page List go!');
    let GridModule = gridModule();
    GridModule.initGrid();
  });
})();
