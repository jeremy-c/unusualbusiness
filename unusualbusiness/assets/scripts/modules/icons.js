/* ==|====================
   Module/Icons
   ======================= */

'use strict';

let Icons = () => {

  let initSvg4Everybody = function() {
    // SVG Polyfill
    svg4everybody({
      polyfill: true
    });
  };

  let initStartSVGAnimationsOnHover = function() {
     let $animationHolder = $(".start-animation-on-hover");

     $animationHolder.on("mouseenter", function() {
        $(this).toggleClass("is-running");
     });

     $animationHolder.on("mouseleave", function() {
        $(this).toggleClass("is-running");
     });
  };

  let init = function() {
    console.log('Animate Icons go!');
    initSvg4Everybody();
    initStartSVGAnimationsOnHover();
  };

  return {
    init: init
  };
};

export default Icons;
