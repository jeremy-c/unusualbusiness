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
    let $customHeaderMenuButton = $('.custom-header-hamburger-button');
    let $header = $('.header');
    let $customHeader = $('.custom-header');
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
    let headroomCustomHeader;
    let headroomHeader  = new Headroom(
        headerElement,
        {
          offset : headroomOffset,
          tolerance : {
            down : 10,
            up : 1000
          },
          "classes": {
            "initial": "animated",
            "pinned": "slideInDown",
            "unpinned": "slideOutUp"
          },
          onPin : function() {
              $customHeader.addClass('pin-custom-header-under-header');
          },
          onUnpin : function() {
              $customHeader.removeClass('pin-custom-header-under-header');
          }
        }
    );

      if(customHeaderElement !== null) {
        // construct an instance of Headroom, passing the element
        headroomCustomHeader = new Headroom(
            customHeaderElement,
            {
              offset : headroomOffset,
              tolerance : {
                down : 0,
                up : 5000
              },
              "classes": {
                "initial": "animated",
                "pinned": "slideOutUp",
                "unpinned": "slideInDown"
              }
            }
        );
        headroomCustomHeader.init();
      }
    // initialise
    headroomHeader.init();

    $customHeaderMenuButton.on('click', function() {
        if($header.hasClass('slideOutUp')) {
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
