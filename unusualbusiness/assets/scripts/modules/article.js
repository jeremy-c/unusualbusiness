/* ==|====================
   Module/Article
   ======================= */

'use strict';

var article = () => {
  let initInlineAricleLinks = function() {
    let articleInlineLinks = $('.article-inline-link');

    articleInlineLinks.on('click', function() {
      let inlineElement = $(this).data('id');

      $(this).toggleClass('is-expanded');
      $('#' + inlineElement).toggleClass('is-visuallyhidden');
    });
  };

  let initArticle = function() {
    initInlineAricleLinks();
  };

  return {
    initArticle: initArticle
  };
};

(function() {
  $(document).ready(function() {
    console.log('Article go!');
    let Article = article();
    Article.initArticle();
  });
})();
