/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

let mobileMenu = () => {
  let toggleHamburgerMenu = function() {
    $('#hamburger-menu-button').toggleClass('active');
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
