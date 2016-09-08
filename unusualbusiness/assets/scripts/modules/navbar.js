/* ==|====================
   Module/Navbar
   ======================= */

import Headroom from 'headroom.js';
import debounce from 'debounce';

let Navbars = () => {
  let spinLogo = function() {
    $(this).toggleClass('is-spinned');
  };

  let shakeIcon = function() {
    $(this).toggleClass('animated shake');
    return false;
  };

  let initNavbar = function() {
    console.log('Navbar: initNavbar');
    let $ubLogoLink = $('.ub-logo-link');
    let $searchLink = $('.main-menu-search-link');

    $ubLogoLink.on('mouseenter', debounce(spinLogo));
    $ubLogoLink.on('mouseleave', debounce(spinLogo));

    $searchLink.on('click', shakeIcon);
  };

  let initHeadroomJS = function() {
    // console.log('Navbar: initHeadroomJS');

    let $extraNavbarMenuButton = $('.extra-navbar-hamburger-button');
    let $navbar = $('.navbar');
    // TODO: exclude
    // .home &,
    // .disclaimer-page &,
    // .about-page &,
    // .how-tos-page &,
    // .how-to &
    let $extraNavbar = $('.extra-navbar');
    let $upcomingEventsElement = $('.upcoming-related-events');

    let articleHeaderHeight = $('.article-header').height();
    let articleSubHeaderHeight = $('.article-subheader').height();
    let headerHeight = $navbar.height();
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

    // console.log('Navbar: initHeadroomJS - querySelector');

    $navbar.headroom({
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
    });
    if($extraNavbar.length > 0) {
        $extraNavbar.headroom({
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
        });
    }
    // console.log('Navbar: initHeadroomJS - headroomHeader = new Headroom');

    $extraNavbarMenuButton.on('click', function(e) {
        e.preventDefault();

        $extraNavbar.toggleClass('is-pined-under-navbar');
        $extraNavbar.toggleClass('slideInDown');
        $navbar.toggleClass('slideOutUp');
        $navbar.toggleClass('slideInDown');

        if($navbar.hasClass('slideInDown')) {
            $navbar.pin();
        } else {
            $extraNavbar.unpin();
        }
    });

  };

  let initHowToCircleHover = function() {
    let $howToCirclesLink = $('.how-to-circles-link');
    $howToCirclesLink.on('mouseover', function() {
      "use strict";
      $(this).find('svg').addClass('how-to-circle-hover');
    });
    $howToCirclesLink.on('mouseout', function() {
      "use strict";
      $(this).find('svg').removeClass('how-to-circle-hover');
    });
    // console.log('Navbar: initHeadroomJS - END');
  };

  let init = function () {
    console.log('Navbar go!');
    initNavbar();
    initHeadroomJS();
    initHowToCircleHover()
  };

  return {
    init: init
  };
};


export default Navbars;
