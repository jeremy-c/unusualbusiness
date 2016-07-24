/* ==|====================
   Module/Icons
   ======================= */

'use strict';
import debounce from 'debounce';


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

    let whichAnimationEvent = function() {
      var t,
          el = document.createElement("fakeelement");

      var animations = {
        "animation"      : "animationend",
        "OAnimation"     : "oAnimationEnd",
        "MozAnimation"   : "animationend",
        "WebkitAnimation": "webkitAnimationEnd"
      };

      for (t in animations){
        if (el.style[t] !== undefined){
          return animations[t];
        }
      }
    };

    let initStartSVGAnimationsOnHover = function() {

        $(".start-animation-on-hover").on('mouseover', debounce(iterateAnimation));
    };

    let iterateAnimation = function() {
        let iteration = 1;
        let $this = $(this);
        let animationEvent = whichAnimationEvent();

        $this.addClass("is-running");

        if ( $this.attr('data-iteration') ) {
            iteration = parseInt( $this.attr('data-iteration') );
            $this.attr('data-iteration', (iteration + 1).toString());
        } else {
            $this.attr('data-iteration', (iteration).toString());
        }

        switch ( iteration ) {
            case 1:
                $this.removeClass('is-iteration-1');
                $this.addClass('is-iteration-2');
                break;
            case 2 :
                $this.removeClass('is-iteration-2');
                $this.addClass('is-iteration-3');
                break;
            case 3 :
                $this.removeClass('is-iteration-3');
                $this.addClass('is-iteration-4');
                break;
            case 4 :
                $this.removeClass('is-iteration-4');
                $this.addClass('is-iteration-5');
                break;
            case 5 :
                $this.removeClass('is-iteration-5');
                $this.addClass('is-iteration-6');
                break;
            case 6 :
                $this.removeClass('is-iteration-6');
                $this.addClass('is-iteration-7');
                break;
            case 7 :
                $this.removeClass('is-iteration-7');
                $this.addClass('is-iteration-8');
                break;
            case 8 :
                $this.removeClass('is-iteration-8');
                $this.addClass('is-iteration-9');
                break;
            case 9 :
                $this.removeClass('is-iteration-9');
                break;
        }

        $(this).one(animationEvent, endAnimation);
    };

    let endAnimation = function(event) {
        console.log('ended');
        $(this).removeClass("is-running");
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
