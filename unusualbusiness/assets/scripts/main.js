/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

console.log('(Un)usual Business go!');

(function() {
  $(document).ready(function() {
    /* global svg4everybody*/
    /* eslint no-undef: 2*/

    svg4everybody({
      polyfill: true
    });
  });
})();
