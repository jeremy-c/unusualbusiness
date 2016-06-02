/* ==|====================
   Module/Article
   ======================= */

'use strict';

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
     location.hash = "#" + color;
  };

  let howToCirclesEvents = function (event) {
    let $greenCircle = $('.how-to-planet .green');
    let $blueCircle = $('.how-to-planet .blue');
    let $blackCircle = $('.how-to-planet .black');
    let $yellowCircle = $('.how-to-planet .yellow');

    $greenCircle.on('mouseout', toggleContentMetaInfo);
    $greenCircle.on('mouseover', toggleContentMetaInfo);
    $blackCircle.on('mouseout', toggleContentMetaInfo);
    $blackCircle.on('mouseover', toggleContentMetaInfo);
    $blueCircle.on('mouseout', toggleContentMetaInfo);
    $blueCircle.on('mouseover', toggleContentMetaInfo);
    $yellowCircle.on('mouseout', toggleContentMetaInfo);
    $yellowCircle.on('mouseover', toggleContentMetaInfo);

    $greenCircle.on('click', goToColor);
    $blueCircle.on('click', goToColor);
    $blackCircle.on('click', goToColor);
    $yellowCircle.on('click', goToColor);
  };

  let init = function() {
    console.log('Howto go!');
    repaceZero();
    howToCirclesEvents();
  };

  return {
    init: init
  };
};

export default HowTo;
