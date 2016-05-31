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

  let initNavbar = function() {
    let howToLink = $('.how-to-link');
    howToLink.on('mouseenter', toggleEyebrows);
    howToLink.on('mouseleave', toggleEyebrows);

    let ubLogoLink = $('.ub-logo-link');
    ubLogoLink.on('mouseenter', spinLogo);
    ubLogoLink.on('mouseleave', spinLogo);
  };

  let initCustomHeader = function() {
    let customHeaderMenuButton = $('.extra-navbar-hamburger-button');
    let customHeader = $('.extra-navbar');
    let header = $('.navbar');

    customHeaderMenuButton.on('click', function() {
        customHeader.addClass('l-pin-custom-header-under-header');

        header.toggleClass('slideOutUp');
        header.toggleClass('slideInDown');
        customHeader.toggleClass('slideInDown');
    });
  };

  let initHeadroomJS = function() {
    let $customHeaderMenuButton = $('.extra-navbar-hamburger-button');
    let $header = $('.navbar');
    let $extraNavbar = $('.extra-navbar');
    let $upcomingEventsElement = $('.upcoming-related-events');

    let articleHeaderHeight = $('.article-header').height();
    let articleSubHeaderHeight = $('.article-subheader').height();
    let headerHeight = $header.height();
    let gutter = 34;

    let upcomingEventsHeight = 0;
    if( $upcomingEventsElement.length )
        upcomingEventsHeight = $upcomingEventsElement.height();

    const headroomOffset =
        upcomingEventsHeight +
        articleHeaderHeight +
        headerHeight +
        articleSubHeaderHeight -
        gutter;

    // grab an element
    var navbarElement = document.querySelector(".navbar");
    var extraNavarElement = document.querySelector(".extra-navbar");

    // construct an instance of Headroom, passing the element
    let headroomCustomHeader;
    let headroomHeader  = new Headroom(
        navbarElement,
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
              $extraNavbar.addClass('is-pined-under-navbar');
          },
          onUnpin : function() {
              $extraNavbar.removeClass('is-pined-under-navbar');
          }
        }
    );

      if(extraNavarElement !== null) {
        // construct an instance of Headroom, passing the element
        headroomCustomHeader = new Headroom(
            extraNavarElement,
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
    console.log('Navbar go!');
    initNavbar();
    initHeadroomJS();
    // initCustomHeader();
  };

  return {
    init: init
  };
};


export default HeaderMenus;
