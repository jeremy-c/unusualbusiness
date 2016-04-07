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

  let init = function() {
    console.log('Article go!');
    initInlineAricleLinks();
  };

  return {
    init: init
  };
};

export default Article;
