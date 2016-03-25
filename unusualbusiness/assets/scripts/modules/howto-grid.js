/* ==|====================
   Module/Featured Article
   ======================= */

'use strict';

var howtoGrid = () => {
  let initGrid = function() {
  };

  return {
    initGrid: initGrid
  };
};

(function() {
  $(document).ready(function() {
    console.log('Howto Grid go!');
    let HowtoGrid = howtoGrid();
    HowtoGrid.initGrid();
  });
})();
