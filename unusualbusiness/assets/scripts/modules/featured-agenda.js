/* ==|====================
   Module/Featured Agenda
   ======================= */

'use strict';

var featuredAgenda = () => {
  let initMouseEvents = function() {
    let agendaItemLink = $('.featured-agenda-item-link');

    agendaItemLink.on('mouseover', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.addClass('is-hover');
    });
    agendaItemLink.on('mouseout', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.removeClass('is-hover');
    });
  };

  return {
    initGrid: initMouseEvents
  };
};

(function() {
  $(document).ready(function() {
    let FeaturedAgenda = featuredAgenda();
    FeaturedAgenda.initGrid();
  });
})();
