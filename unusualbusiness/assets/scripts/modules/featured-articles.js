/* ==|====================
   Module/Featured Article
   ======================= */

'use strict';

let FeaturedArticles = () => {
  let initSlider = function() {
    $('.unslider').unslider({
      keys: false,
      arrows: true,
      nav: true
    });
  };

  let init = function () {
    console.log('Featured Articles go!');
    initSlider();
  };

  return {
    init: init
  };
};

export default FeaturedArticles;
