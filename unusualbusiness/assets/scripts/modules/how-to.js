/* ==|====================
   Module/Article
   ======================= */

'use strict';

import smoothScroll from 'smooth-scroll';

let HowTo = () => {

  let repaceZero = function() {
    let zeroElement = $('.count-0.number');
    zeroElement.text('-');
  };

  let toggleContentMetaInfo = function (event) {
    let $satellite = $('.how-to-satellites .' + this.classList[1]);
    $satellite.toggleClass('is-hidden');
  };

  let goToColor = function (event) {
     var color = this.classList[1];
    window.location.href = "#" + color;
    // if ($.fn.smoothScroll !== undefined) {
    //   $("#" + color).smoothScroll();
    // } else {
    //   console.log('$.fn.smoothScroll === undefined');
    // }
  };

  let howToCirclesEvents = function (event) {
    let $theoryCircle = $('.how-to-planet .theory');
    let $storiesCircle = $('.how-to-planet .stories');
    let $activitiesCircle = $('.how-to-planet .activities');
    let $practitionersCircle = $('.how-to-planet .practitioners');

    $theoryCircle.on('mouseout', toggleContentMetaInfo);
    $theoryCircle.on('mouseover', toggleContentMetaInfo);
    $storiesCircle.on('mouseout', toggleContentMetaInfo);
    $storiesCircle.on('mouseover', toggleContentMetaInfo);
    $practitionersCircle.on('mouseout', toggleContentMetaInfo);
    $practitionersCircle.on('mouseover', toggleContentMetaInfo);
    $activitiesCircle.on('mouseout', toggleContentMetaInfo);
    $activitiesCircle.on('mouseover', toggleContentMetaInfo);

    $theoryCircle.on('click', goToColor);
    $storiesCircle.on('click', goToColor);
    $activitiesCircle.on('click', goToColor);
    $practitionersCircle.on('click', goToColor);
  };

  let howToLinkHover = function () {
    let howToLink = $('.how-to-link');
    howToLink.on('mouseover', function(){
      $(this).find('svg').toggleClass('circle-hover');
    });
    howToLink.on('mouseout', function(){
      $(this).find('svg').toggleClass('circle-hover');
    });
  };


  let init = function() {
    console.log('Howto go!');
    repaceZero();
    howToCirclesEvents();
    howToLinkHover();
  };

  return {
    init: init
  };
};

export default HowTo;
