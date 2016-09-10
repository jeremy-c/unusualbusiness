/* ==|====================
   Module/Featured Agenda
   ======================= */

'use strict';

var Agenda = () => {
  let initMouseEvents = function() {
    let $agendaItemLink = $('.featured-agenda-item-link,.latest-agenda-item-link');

    if($agendaItemLink.length > 0) {
      $agendaItemLink.on('mouseover', function() {
        let timeElement = $(this).parent().siblings().first();
        timeElement.addClass('is-hover');
      });
      $agendaItemLink.on('mouseout', function() {
        let timeElement = $(this).parent().siblings().first();
        timeElement.removeClass('is-hover');
      });
    }
  };

  let init = function () {
    console.log('Agenda go!');
    initMouseEvents()
  };

  return {
    init: init
  };
};


export default Agenda;
