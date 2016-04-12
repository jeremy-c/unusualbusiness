/* ==|====================
   Module/Article
   ======================= */

'use strict';

let Article = () => {
  let initInlineAricleLinks = function() {
    let articleInlineLinks = $('.article-inline-link');

    articleInlineLinks.on('click', function() {
      let inlineElement = $(this).data('id');

      $(this).toggleClass('is-expanded');
      $('#' + inlineElement).toggleClass('is-visuallyhidden');
    });
  };

  let initTOC = function() {
    $(".article-table-of-contents").sticky({
      topSpacing: 112,
      getWidthFrom: '.article-table-of-contents'
    });

    $('.toggle-toc-link').on('click', function () {
      $('.toc-list').toggleClass('is-visuallyhidden');
      return false;
    });
  };

  let init = function() {
    console.log('Article go!');
    initInlineAricleLinks();
    initTOC();
  };

  return {
    init: init
  };
};

export default Article;
