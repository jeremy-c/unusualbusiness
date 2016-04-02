/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

let mobileMenu = () => {
  let toggleHamburgerMenu = function() {
    let hamburgerMenuButtonLink = $('#hamburger-menu-button');
    let isExpanded = hamburgerMenuButtonLink.attr('aria-expanded') === 'true';
    hamburgerMenuButtonLink.attr(
        'aria-expanded',
        (!isExpanded).toString()
    );
    hamburgerMenuButtonLink.toggleClass('is-expanded');
  };

  let initAnimateMenuBar = function() {
    let menuItemHowTo = $('.main-menu-how-to');
    menuItemHowTo.addClass('is-in-position');
    menuItemHowTo.on('click', function() {
      menuItemHowTo.addClass('is-fading-out');
    });
    // let menuItemHowTo1 = $('.main-menu-how-to:nth-last-of-type(1)');
    // let menuItemHowTo2 = $('.main-menu-how-to:nth-last-of-type(2)');
    // let menuItemHowTo3 = $('.main-menu-how-to:nth-last-of-type(3)');
    // let menuItemHowTo4 = $('.main-menu-how-to:nth-last-of-type(4)');
    // menuItemHowTo.on('click', function() {
    //   menuItemHowTo1.velocity({
    //     left: '100%'
    //   }, {
    //     easing: 'easeInOutExpo',
    //     duration: 200
    //   });
    //   menuItemHowTo2.velocity({
    //     left: '100%'
    //   }, {
    //     easing: 'easeInOutExpo',
    //     duration: 200
    //   });
    //   menuItemHowTo3.velocity({
    //     left: '100%'
    //   }, {
    //     easing: 'easeInOutExpo',
    //     duration: 200
    //   });
    //   menuItemHowTo4.velocity({
    //     left: '100%'
    //   }, {
    //     easing: 'easeInOutExpo',
    //     duration: 200
    //   });
    // });
  };

  let initSidrMenu = function() {
    $('#hamburger-menu-button').sidr({
      name: 'mobile-menu',
      side: 'right',
      source: '.main-nav',
      body: '.l-wrapper',
      renaming: false,
      dispace: false,
      onOpen: toggleHamburgerMenu,
      onClose: toggleHamburgerMenu
    });
  };

  let initMenu = function() {
    initAnimateMenuBar();
    // wait for SVG's to be copied
    window.setTimeout(initSidrMenu, 1000);
  };

  return {
    initMenu: initMenu
  };
};

(function() {
  $(window).ready(function() {
    console.log('Main go!');
    /* global svg4everybody*/
    /* eslint no-undef: 2*/

    svg4everybody({
      polyfill: true
    });

    let MobileMenu = mobileMenu();
    MobileMenu.initMenu();
  });
})();
