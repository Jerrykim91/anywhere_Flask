/*
	Strata by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function ($) {

    var $window = $(window),
        $body = $('body'),
        $header = $('#header'),
        $footer = $('#footer'),
        $main = $('#main'),
        settings = {

            // Parallax background effect?
            parallax: true,

            // Parallax factor (lower = more intense, higher = less intense).
            parallaxFactor: 20

        };

    // Breakpoints.
    breakpoints({
        xlarge: [
            '1281px', '1800px'
        ],
        large: [
            '981px', '1280px'
        ],
        medium: [
            '737px', '980px'
        ],
        small: [
            '481px', '736px'
        ],
        xsmall: [null, '480px']
    });

    // Play initial animations on page load.
    $window.on('load', function () {
        window.setTimeout(function () {
            $body.removeClass('is-preload');
        }, 100);
    });

    // Touch?
    if (browser.mobile) {

        // Turn on touch mode.
        $body.addClass('is-touch');

        // Height fix (mostly for iOS).
        window.setTimeout(function () {
            $window.scrollTop($window.scrollTop() + 1);
        }, 0);

    }

    // Footer.
    breakpoints.on('<=medium', function () {
        $footer.insertAfter($main);
    });

    breakpoints.on('>medium', function () {
        $footer.appendTo($header);
    });

    // Header. Parallax background. Disable parallax on IE (smooth scrolling is
    // jerky), and on mobile platforms (= better performance).
    if (browser.name == 'ie' || browser.mobile) 
        settings.parallax = false;
    
    if (settings.parallax) {

        breakpoints.on('<=medium', function () {

            $window.off('scroll.strata_parallax');
            $header.css('background-position', '');

        });

        breakpoints.on('>medium', function () {

            $header.css('background-position', 'left 0px');

            $window.on('scroll.strata_parallax', function () {
                $header.css('background-position', 'left ' + (
                    -1 * (parseInt($window.scrollTop()) / settings.parallaxFactor)
                ) + 'px');
            });

        });

        $window.on('load', function () {
            $window.triggerHandler('scroll');
        });

    }

    // Main Sections: Two. Lightbox gallery.
    $window.on('load', function () {

        $('#two').poptrox({
            caption: function ($a) {
                return $a
                    .next('h3')
                    .text();
            },
            overlayColor: '#2c2c2c',
            overlayOpacity: 0.85,
            popupCloserText: '',
            popupLoaderText: '',
            selector: '.work-item a.image ',
            usePopupCaption: true,
            usePopupDefaultStyling: false,
            usePopupEasyClose: false,
            usePopupNav: true,
            windowMargin: (
                breakpoints.active('<=small')
                    ? 0
                    : 50
            )
        });

    });

    // Lightbox gallery-2.
    $window.on('load', function () {

        $('#two').poptrox({
            caption: function ($a) {
                return $a
                    .next('h3')
                    .text();
            },
            overlayColor: '#2c2c2c',
            // overlayOpacity : 백그라운드 투명도 Default : 0.85
            overlayOpacity: 0.50,
            popupCloserText: '',
            popupLoaderText: '',
            selector: '.work-test a.image ',
            usePopupCaption: true,
            usePopupDefaultStyling: false,
            usePopupEasyClose: false,
            // usePopupNav : 좌우 이동 클릭 -> 이미지 이동
            usePopupNav: false,
            windowMargin: (
                breakpoints.active('<=small')
                    ? 0
                    : 50
            )
        });

    });

    // Menu.
    var $menu = $('#menu'),
        $menu_openers = $menu
            .children('ul')
            .find('.opener');

    // Openers.
    $menu_openers.each(function () {

        var $this = $(this);

        $this.on('click', function (event) {

            // Prevent default.
            event.preventDefault();

            // Toggle.
            $menu_openers
                .not($this)
                .removeClass('active');
            $this.toggleClass('active');

            // Trigger resize (sidebar lock).
            $window.triggerHandler('resize.sidebar-lock');

        });

    });

    // toggle.
    // $('#sidebarCollapse').on('click', function () {
    //     $('#sidebar').addClass('active');
    //     $('.overlay').fadeIn();
    // });
    
    // $('.overlay').on('click', function () {
    //     $('#sidebar').removeClass('active');
    //     $('.overlay').fadeOut();
    // });
    // $(function() {
    //     // Sidebar toggle behavior
    //     $('#navCollapse').on('click', function() {
    //       $('#menu').toggleClass('active');
    //     });
    //   });
      

})(jQuery);