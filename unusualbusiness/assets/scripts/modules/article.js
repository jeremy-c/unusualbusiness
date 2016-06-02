/* ==|====================
   Module/Article
   ======================= */

'use strict';

// import Froffcanvas from 'fr-offcanvas';

let Article = () => {
  let initInlineAricleLinks = function() {
    let articleInlineLinks = $('.article-inline-link');

    articleInlineLinks.on('click', function() {
      let inlineElement = $(this).data('id');

      $(this).toggleClass('is-expanded');
      $('#' + inlineElement).each( function () {
        $(this).toggleClass('is-visuallyhidden');
      });
    });
  };

  let initTOC = function() {
    // var myOffcanvas = Froffcanvas();
    // myOffcanvas.init()
  };

  let initAuthorPane = function() {
    let articleInlineLinks = $('.open-author-pane-button');

    articleInlineLinks.on('click', function() {
      $(this).toggleClass('is-opened-button');
      let $authorElement = $('.author');
      let articleContentElement = $('.article-content');

      if( $authorElement.hasClass('is-visuallyhidden') ) {
        $authorElement.removeClass('is-visuallyhidden');
        $authorElement.toggleClass('slideInDown is-author-clicked');
      } else {
        $authorElement.removeClass('slideInDown');
        $authorElement.addClass('slideOutUp').one(
            'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
            function() {
          $authorElement.removeClass('is-author-clicked');
          $authorElement.removeClass('slideOutUp');
          $authorElement.addClass('is-visuallyhidden');
        });
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

  let initExternalLinks = function() {
    $('a:external')
        .attr('target', '_blank');
    $('a:external')
        .not('.facebook-link')
        .not('.twitter-link')
        .addClass('external-link');
  };

  let init = function() {
    console.log('Article go!');
    initArticleNotes();
    initInlineAricleLinks();
    initTOC();
    initAuthorPane();
    initExternalLinks();
  };

  return {
    init: init
  };
};

export default Article;
