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

    let addListenerMulti = function (el, s, fn) {
      s.split().forEach(e => el.addEventListener(e, fn, false));
    };

    let stopAnimation = function(event){
        event.srcElement.style.webkitAnimationPlayState = "paused";
        // console.log(event.srcElement);
        // event.currentTarget.classList.remove("is-running");
    };

    let startAnimation = function(){
        let element = this;
        let svgElements = element.querySelectorAll('svg *');

        for (var j = 0; j < svgElements.length; j++) {
            let svgElement = svgElements[j];
            svgElement.style.webkitAnimationPlayState = "running";
        }
        // element.classList.add("is-running");

        element.addEventListener('webkitAnimationEnd', stopAnimation);
        element.addEventListener('mozAnimationEnd', stopAnimation);
        element.addEventListener('oAnimationEnd', stopAnimation);
        element.addEventListener('msAnimationEnd', stopAnimation);
        element.addEventListener('animationEnd', stopAnimation);
    };

    let initStartSVGAnimationsOnHover = function() {
        let animationHolders = document.getElementsByClassName("start-animation-on-hover");

        for (var i = 0; i < animationHolders.length; i++) {
            let element = animationHolders[i];
            element.addEventListener("mouseenter", startAnimation, false);
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
