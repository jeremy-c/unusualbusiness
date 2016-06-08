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

  let shakeIcon = function() {
    $(this).togggleClass('shake');

    return false;
  };

  let initNavbar = function() {
    let ubLogoLink = $('.ub-logo-link');
    let $searchLink = $('.main-menu-search-link');

    ubLogoLink.on('mouseenter', spinLogo);
    ubLogoLink.on('mouseleave', spinLogo);

    $searchLink.on('click', shakeIcon);
  };

  let initExtraNavbar = function() {
    let $extraNavbarMenuButton = $('.extra-navbar-hamburger-button');
    let $extraNavbar = $('.extra-navbar');
    let $navbar = $('.navbar');

    $extraNavbarMenuButton.on('click', function() {
        $extraNavbar.addClass('is-pined-under-navbar');
        $navbar.toggleClass('slideOutUp');
        $navbar.toggleClass('slideInDown');
        $extraNavbar.toggleClass('slideInDown');
    });
  };

  let initHeadroomJS = function() {
    let $extraNavbarMenuButton = $('.extra-navbar-hamburger-button');
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
    var extraNavbarElement = document.querySelector(".extra-navbar");

    // construct an instance of Headroom, passing the element
    let headroomExtraNavbar;
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

      if(extraNavbarElement !== null) {
        // construct an instance of Headroom, passing the element
        headroomExtraNavbar = new Headroom(
            extraNavbarElement,
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
        headroomExtraNavbar.init();
      }
    // initialise
    headroomHeader.init();

    $extraNavbarMenuButton.on('click', function() {
        var sdf = headroomHeader;
        if($header.hasClass('slideInDown')) {
            headroomExtraNavbar.unpin();
            headroomHeader.pin();
        } else {
            headroomHeader.unpin();
            $extraNavbar.removeClass('is-pined-under-navbar');
        }
    });
  };

  let init = function () {
    console.log('Navbar go!');
    initNavbar();
    initExtraNavbar();
    initHeadroomJS();
  };

  return {
    init: init
  };
};


export default HeaderMenus;
