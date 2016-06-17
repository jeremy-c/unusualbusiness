/* ==|====================
   Module/Article
   ======================= */

'use strict';

import gumshoe from 'gumshoe';
import Clipboard from 'clipboard';

let Article = () => {
  let initInlineArticleLinks = function() {
    let articleInlineLinks = $('.article-inline-link');

    articleInlineLinks.on('click', function() {
      let inlineElement = $(this).data('id');

      $(this).toggleClass('is-expanded');
      $('#' + inlineElement).each( function () {
        $(this).toggleClass('is-visuallyhidden animated fadeIn');
      });
    });
  };

  let initTOC = function() {
    let $tocWrapper = $('.toc-wrapper');
    let $tocToggleLink = $('.toggle-toc-link');
    let $toc = $('.article-table-of-contents');
    let $tocList = $('.toc-list');
    let $articleIntroduction = $('.article-introduction');
    let $blockImage = $('.block-image');

    $tocToggleLink.on('click', function() {
      $tocList.toggleClass('is-hidden');
      $tocToggleLink.toggleClass('is-panel-open');
      $toc.toggleClass('is-closed');
      $articleIntroduction.toggleClass('l-pull-right');
      $blockImage.toggleClass('l-pull-right');

      return false;
    });

    gumshoe.init();
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

  let initSocialLinks = function() {
    let $moreSocialLink = $('.more-social-link');
    let $socialListItem = $('.social-list-item');


    $moreSocialLink.on('click', function() {
      $socialListItem.removeClass('is-hidden');
      return false;
    });
  };

  let initSocialLinksModal = function() {
    let $articleHeader = $('.article-header');
    let $articleSubheader = $('.article-subheader');
    let $openSocialModal = $('.open-social-modal');
    let $openAuthorPaneButton = $('.open-author-pane-button');

    $openSocialModal.on('click', function() {
      let status = $(this).attr('data-closed');
      console.log(status);
      if( status === 'true' ) { // Opening
        console.log('Opening');

        $openSocialModal.parent().toggleClass('is-open-social');

        $articleHeader.toggleClass('is-no-position');
        if( $articleSubheader.hasClass('slideOutDown')) {
          $articleSubheader.removeClass('slideOutDown');
        }

        $articleSubheader.addClass('animated slideInUp is-show-article-subheader');
        $openAuthorPaneButton.toggleClass('is-hidden');
        $(this).attr('data-closed', 'false');

      } else { // Closing
        console.log('Closing');

        $openSocialModal.parent().toggleClass('is-open-social');

        $articleSubheader.removeClass('slideInUp');
        $articleSubheader.addClass('slideOutDown ');
        $articleSubheader.removeClass('is-show-article-subheader');
        $openAuthorPaneButton.toggleClass('is-hidden');
        $articleHeader.toggleClass('is-no-position');
        $(this).attr('data-closed', 'true');
      }
    });
  };


  let initCopyUrlToClipboard = function() {
    new Clipboard('.copy-url-link');
  };

  let init = function() {
    console.log('Article go!');
    initArticleNotes();
    initInlineArticleLinks();
    initTOC();
    initAuthorPane();
    initExternalLinks();
    initSocialLinks();
    initSocialLinksModal();
    initCopyUrlToClipboard();
  };

  return {
    init: init
  };
};

export default Article;
