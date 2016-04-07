/* ==|====================
   Module/Header
   ======================= */

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

  let init = function () {
    console.log('Header go!');
    initHeader();
  };

  return {
    init: init
  };
};


export default HeaderMenus;
