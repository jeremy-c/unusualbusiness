/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

import Grid from './modules/grid';
import MobileMenu from './modules/mobile-menu';
import Article from './modules/article';
import FeaturedAgenda from './modules/featured-agenda';
import FeaturedArticles from './modules/featured-articles';
import FeaturedJournal from './modules/featured-journal';
import HeaderMenus from './modules/header';

(function() {
  console.log('Main: go!');

  $(document).ready(function() {
    console.log('Main: Document ready go!');

    let grid = Grid();
    let mobileMenu = MobileMenu();
    let article = Article();
    let featuredAgenda = FeaturedAgenda();
    let featuredArticles = FeaturedArticles();
    let featuredJournal = FeaturedJournal();
    let headerMenus = HeaderMenus();

    grid.init();
    mobileMenu.init();
    article.init();
    featuredAgenda.init();
    featuredArticles.init();
    featuredJournal.init();
    headerMenus.init();
  });

  $(window).ready(function() {
    console.log('Main: Window ready go!');

    // SVG Polyfill
    svg4everybody({
      polyfill: true
    });
  });
})();
