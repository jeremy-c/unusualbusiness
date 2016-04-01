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
    window.setTimeout(initAnimateMenuBar, 1000);
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
