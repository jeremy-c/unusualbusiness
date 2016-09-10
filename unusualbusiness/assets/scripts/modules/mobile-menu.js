/* ==|====================
   Module/Mobile Menu
   ======================= */

'use strict';

let MobileMenu = () => {
  let toggleMenu = function() {
    let $body = $('body');
    $body.toggleClass('is-menu-open');

    let hamburgerMenuButtonLink = $('#hamburger-menu-button');

    let isExpanded = hamburgerMenuButtonLink.attr('aria-expanded') === 'true';
    hamburgerMenuButtonLink.attr(
        'aria-expanded',
        (!isExpanded).toString()
    );
    hamburgerMenuButtonLink.toggleClass('is-expanded');
  };

  let initSidrMenu = function() {
    $('#hamburger-menu-button').sidr({
      name: 'mobile-menu',
      side: 'right',
      source: '.l-main-nav',
      body: '.l-wrapper',
      renaming: false,
      displace: false,
      onOpen: toggleMenu,
      onClose: toggleMenu
    });

    $('.extra-navbar-hamburger-menu-button').sidr({
      name: 'mobile-menu',
      side: 'right',
      source: '.l-main-nav',
      body: '.l-wrapper',
      renaming: false,
      displace: false,
      onOpen: toggleMenu,
      onClose: toggleMenu
    });
  };

  let init = function() {
    // wait for SVG's to be copied
    window.setTimeout(initSidrMenu, 1000);
  };

  return {
    init: init
  };
};

export default MobileMenu;
