/* ==|====================
   Module/Article
   ======================= */

'use strict';

import Velocity from 'velocity-animate';

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

  let initAuthorPane = function() {
    let articleInlineLinks = $('.open-author-pane-button');

    articleInlineLinks.on('click', function() {
      let buttonElement = $(this).toggleClass('is-opened-button');
      let authorElement = $('.author');
      let articleContentElement = $('.article-content');

      if( authorElement.hasClass('is-visuallyhidden') ) {
        authorElement.toggleClass('is-visuallyhidden');
        Velocity.animate(authorElement, {
          'min-height': "272px",
          top: "0"
        });
      } else {
        Velocity.animate(authorElement, {
          'min-height': "0",
          top: "-272px"
        }).then(
            function(elements) {
              authorElement.toggleClass('is-visuallyhidden');
            }
        );
      }

      return false;
    });
  };


  let initArticleNotes = function() {
    let articleFootnotes = $('.article-inline-footnote');

    articleFootnotes.each(function() {
      let footnoteIndex = $(this).attr('id').split('-')[2];
      let articleFootnoteLink = $('#article-footnote-link-' + footnoteIndex);
      articleFootnoteLink.after($(this).detach());
    });
  };

  let init = function() {
    console.log('Article go!');
    initArticleNotes();
    initInlineAricleLinks();
    initTOC();
    initAuthorPane();
  };

  return {
    init: init
  };
};

export default Article;
