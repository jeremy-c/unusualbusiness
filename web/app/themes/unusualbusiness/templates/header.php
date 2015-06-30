<header class="banner" role="banner">
    <div class="container">
        <a class="brand" href="<?= esc_url(home_url('/')); ?>">
            <picture>
                <img srcset="<?= get_bloginfo('template_directory');?>/dist/images/unusualbusiness-logo.png, <?= get_bloginfo('template_directory');?>/dist/images/unusualbusiness-logo-retina.png 2x"
                     alt="Linksmith - Web development" class="logo" />
            </picture>
        </a>
        <?php
        /*
          <nav role="navigation">
            <?php
            if (has_nav_menu('primary_navigation')) :
              wp_nav_menu(['theme_location' => 'primary_navigation', 'menu_class' => 'nav']);
            endif;
            ?>
          </nav>
          */
        ?>
    </div>
</header>
