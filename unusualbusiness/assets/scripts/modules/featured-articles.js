/* ==|====================
   Module/Featured Article
   ======================= */

'use strict';

let FeaturedArticles = () => {
  let initSlider = function() {
    $('.unslider').unslider({
      keys: {
          prev: 37,
          next: 39,
          stop: 27 //  Example: pause when the Esc key is hit
      },
      arrows: {
        //  Unslider default behaviour
        prev: '<a class="unslider-arrow prev" aria-controls="Previous slide"></a>',
        next: '<a class="unslider-arrow next" aria-controls="Next slide"></a>'
      },
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
