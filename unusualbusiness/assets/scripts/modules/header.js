/* ==|====================
   Module/Header
   ======================= */

import Headroom from 'headroom.js';

let HeaderMenus = () => {
  let toggleEyebrows = function() {
    let howToEyebrow = $(this).children().first();
    let howToEye = howToEyebrow.siblings().first();

    howToEyebrow.toggleClass('is-hidden');
    howToEye.toggleClass('is-hidden');
  };

  let spinLogo = function() {
    $(this).toggleClass('is-spinned');
  };

  let initHeader = function() {
    let howToLink = $('.how-to-link');
    howToLink.on('mouseenter', toggleEyebrows);
    howToLink.on('mouseleave', toggleEyebrows);

    let ubLogoLink = $('.ub-logo-link');
    ubLogoLink.on('mouseenter', spinLogo);
    ubLogoLink.on('mouseleave', spinLogo);
  };

  let initCustomHeader = function() {
    let customHeaderMenuButton = $('.custom-header-hamburger-button');
    let customHeader = $('.custom-header');
    let header = $('.header');

    customHeaderMenuButton.on('click', function() {
        customHeader.addClass('l-pin-custom-header-under-header');

        header.toggleClass('slideOutUp');
        header.toggleClass('slideInDown');
        customHeader.toggleClass('slideInDown');
    });
  };

  let initHeadroomJS = function() {
    let customHeaderMenuButton = $('.custom-header-hamburger-button');
    let header = $('.header');
    let upcomingEventsHeight = $('.upcoming-related-events').height();
    let articleHeaderHeight = $('.article-header').height();
    let headerHeight = 85;
    const headroomOffset =
        upcomingEventsHeight +
        articleHeaderHeight +
        headerHeight -
        15;

    // grab an element
    var headerElement = document.querySelector(".header");
    var customHeaderElement = document.querySelector(".custom-header");

    // construct an instance of Headroom, passing the element
    var headroomHeader  = new Headroom(
        headerElement,
        {
          // vertical offset in px before element is first unpinned
          offset : headroomOffset,
          // or scroll tolerance per direction
          tolerance : {
            down : 10,
            up : 1000
          },
          // element which is source of scroll events. Defaults to window
          //scroller : element,
          // css classes to apply
          "classes": {
            "initial": "animated",
            "pinned": "slideInDown",
            "unpinned": "slideOutUp"
          },
          // callback when pinned, `this` is headroom object
          onPin : function() {
              $('.custom-header').addClass('pin-custom-header-under-header');
          },
          // callback when unpinned, `this` is headroom object
          onUnpin : function() {
              $('.custom-header').removeClass('pin-custom-header-under-header');
          },
          // callback when above offset, `this` is headroom object
          onTop : function() {},
          // callback when below offset, `this` is headroom object
          onNotTop : function() {},
          // callback at bottom of page, `this` is headroom object
          onBottom : function() {},
          // callback when moving away from bottom of page, `this` is headroom object
          onNotBottom : function() {}
        }
    );

    // construct an instance of Headroom, passing the element
    var headroomCustomHeader  = new Headroom(
        customHeaderElement,
        {
          // vertical offset in px before element is first unpinned
          offset : headroomOffset,
          // or scroll tolerance per direction
          tolerance : {
            down : 0,
            up : 5000
          },
          // element which is source of scroll events. Defaults to window
          //scroller : element,
          // css classes to apply
          "classes": {
            "initial": "animated",
            "pinned": "slideOutUp",
            "unpinned": "slideInDown"
          },
          // callback when pinned, `this` is headroom object
          onPin : function() {},
          // callback when unpinned, `this` is headroom object
          onUnpin : function() {},
          // callback when above offset, `this` is headroom object
          onTop : function() {},
          // callback when below offset, `this` is headroom object
          onNotTop : function() {},
          // callback at bottom of page, `this` is headroom object
          onBottom : function() {},
          // callback when moving away from bottom of page, `this` is headroom object
          onNotBottom : function() {}
      }
    );

    // initialise
    headroomHeader.init();
    headroomCustomHeader.init();

    customHeaderMenuButton.on('click', function() {
        if(header.hasClass('slideOutUp')) {
            headroomCustomHeader.unpin();
            headroomHeader.pin();
        } else {
            headroomHeader.unpin();
        }
    });
  };

  let init = function () {
    console.log('Header go!');
    initHeader();
    initHeadroomJS();
    // initCustomHeader();
  };

  return {
    init: init
  };
};


export default HeaderMenus;
