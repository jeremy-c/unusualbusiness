/* ==|====================
   Module/Icons
   ======================= */

'use strict';

let Icons = () => {

    let initSvg4Everybody = function() {
        // SVG  Polyfill
        svg4everybody({
          polyfill: true
        });
    };

    let arg = function(link) {
        link.toggleClass("is-pausing");
        link.toggleClass("is-running");
    };

    let stopAnimation = function(event){
        // event.currentTarget.classList.remove("is-running");
        // console.log(event.currentTarget.classList);
        // console.log(event.target.nearestViewportElement.clientHeight);
    };

    let addListenerMulti = function (el, s, fn) {
      s.split().forEach(e => el.addEventListener(e, fn, false));
    };

    let initStartSVGAnimationsOnHover = function() {
        let animationHolders = document.getElementsByClassName("start-animation-on-hover");

        for (var i = 0; i < animationHolders.length; i++) {
            let element = animationHolders[i];
            element.addEventListener("mouseover", function(e) {
                element.classList.add("is-running");

                element.addEventListener('webkitAnimationEnd', stopAnimation);
                element.addEventListener('mozAnimationEnd', stopAnimation);
                element.addEventListener('animationEnd', stopAnimation);

                // addListenerMulti(
                //     element,
                //     "webkitAnimationEnd mozAnimationEnd animationEnd",
                //     function(){
                //         event.currentTarget.classList.remove("is-running");
                //         console.log(event.currentTarget.offsetWidth);
                //     });
            }, false);

        }
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
