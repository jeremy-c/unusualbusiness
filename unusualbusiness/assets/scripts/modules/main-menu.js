/* ==|====================
   Module/Main Menu
   ======================= */

'use strict';

var headerMenus = () => {
  let toggleEyebrows = function() {
    let howToEyebrow = $(this).children().first();
    let howToEye = howToEyebrow.siblings().first();

    howToEyebrow.toggleClass('is-hidden');
    howToEye.toggleClass('is-hidden');
  };

  let initMainMenu = function() {
    let howToLink = $('.how-to-link');
    howToLink.on('mouseenter', toggleEyebrows);
    howToLink.on('mouseleave', toggleEyebrows);
  };

  return {
    initMainMenu: initMainMenu
  };
};

(function() {
  $(document).ready(function() {
    let HeaderMenus = headerMenus();
    HeaderMenus.initMainMenu();
  });
})();
