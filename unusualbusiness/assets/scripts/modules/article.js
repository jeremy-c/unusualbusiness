/* ==|====================
   Module/Article
   ======================= */

'use strict';

var article = () => {
  let initInlineAricleLinks = function() {
    let articleInlineLinks = $('.article-inline-link');

    articleInlineLinks.on('click', function() {
      let inlineElement = $(this).attr('href');

      $(this).toggleClass('is-open');
      $(inlineElement).toggleClass('is-hidden');
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
