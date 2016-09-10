/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

// Imports
import General from './modules/general';
import Grid from './modules/grid';
import Navbars from './modules/navbar';
import Article from './modules/article';
import Agenda from './modules/agenda';
import Sliders from './modules/slider';
import Navbar from './modules/navbar';
import Organization from './modules/organization';
import HowTo from './modules/how-to';
import Icons from './modules/icons';
import MobileMenu from './modules/mobile-menu';

(function() {
  console.log('Main: go!');

  $(document).ready(function() {
    console.log('Main: Document ready go!');

    let grid = Grid();
    let navbars = Navbars();
    let article = Article();
    let agenda = Agenda();
    let slider = Sliders();
    let navbar = Navbar();
    let organization = Organization();
    let mobileMenu = MobileMenu();

    grid.init();
    navbars.init();
    article.init();
    agenda.init();
    slider.init();
    navbar.init();
    organization.init();
    mobileMenu.init();
  });

  $(window).ready(function() {
    console.log('Main: Window ready go!');

    let general = General();
    let howTo = HowTo();
    let icons = Icons();

    general.init();
    icons.init();
    howTo.init();
  });
})();
