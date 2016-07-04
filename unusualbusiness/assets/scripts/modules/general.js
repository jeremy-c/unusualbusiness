/* ==|====================
   Module/General
   ======================= */

'use strict';

import smoothScroll from 'smooth-scroll';


let General = () => {

    let initExternalLinks = function () {    
      $.expr[':'].external = function(obj){
          return !obj.href.match(/^mailto\:/)
                 && (obj.hostname != location.hostname)
                 && !obj.href.match(/^javascript\:/)
                 && !obj.href.match(/^$/)
      };        
    };
    
    let initSmoothScroll = function () {     
        smoothScroll.init({
          selector: '[data-scroll]', // Selector for links (must be a valid CSS selector)
          selectorHeader: '[data-scroll-header]', // Selector for fixed headers (must be a valid CSS selector)
          speed: 500, // Integer. How fast to complete the scroll in milliseconds
          easing: 'easeInOutCubic', // Easing pattern to use
          offset: 28, // Integer. How far to offset the scrolling anchor location in pixels
          updateURL: true, // Boolean. If true, update the URL hash on scroll
          callback: function ( anchor, toggle ) {} // Function to run after scrolling
        });
    };
    
  let init = function() {
    console.log('General go!');
    initSmoothScroll();
    initExternalLinks();
  };

  return {
    init: init
  };
};

export default General;
