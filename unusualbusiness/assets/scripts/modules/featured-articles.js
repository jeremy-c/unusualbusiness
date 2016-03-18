/* ==|====================
   Module/Featured Article
   ======================= */

'use strict';

var featuredArticles = () => {
  let initSlider = function() {
    $('.unslider').unslider({
      keys: false,
      arrows: false,
      nav: true
    });
  };

  return {
    initSlider: initSlider
  };
};

(function() {
  $(document).ready(function() {
    let FeaturedArticles = featuredArticles();
    FeaturedArticles.initSlider();
  });
})();
