/***************************************************************************************************************
||||||||||||||||||||||||||||           CUSTOM SCRIPT FOR FAUNA              ||||||||||||||||||||||||||||||||||||
****************************************************************************************************************
||||||||||||||||||||||||||||              TABLE OF CONTENT                  ||||||||||||||||||||||||||||||||||||
****************************************************************************************************************
****************************************************************************************************************
1. RevolutionSliderActiver
2. CounterNumberChanger
3. Single gallery slider
4. Accordion Box
5. testimonialCarosule
6. Jquery Tabs Box
7. Main menu
8. zebraDatePickerInit 
9. Update Scroll to Top
10. Scroll to a Specific 
11. Update Scroll to Top
12. Contact Form Validation   

****************************************************************************************************************
||||||||||||||||||||||||||||            End TABLE OF CONTENT                ||||||||||||||||||||||||||||||||||||
****************************************************************************************************************/
"use strict";
// 1. revolutionSliderActiver
function revolutionSliderActiver() {
    if ($('.rev_slider_wrapper #slider1').length) {
        $("#slider1").revolution({
            sliderType: "standard",
            sliderLayout: "auto",
            delay: 5000,
            hideTimerBar: "off",
            onHoverStop: "off",
            navigation: {
                arrows: {
                    enable: true
                }
            },
            gridwidth: [1900, 1320, 1170, 975, 750, 480, 450],
            gridheight: [840, 800, 650, 500, 500, 500]
        });
    };
}

// 2. CounterNumberChanger
function CounterNumberChanger() {
    var sFcounter = $('.sF-counter');
    if (sFcounter.length) {
        sFcounter.appear(function () {
            sFcounter.countTo();

        });
    };

}
//3. Single gallery slider
function singleGalleryCarousel() {
    if ($('.single-gallery-carousel-content-box').length && $('.single-gallery-carousel-thumbnail-box').length) {

        var $sync1 = $(".single-gallery-carousel-content-box"),
            $sync2 = $(".single-gallery-carousel-thumbnail-box"),
            flag = false,
            duration = 500;

        $sync1
            .owlCarousel({
                items: 1,
                margin: 0,
                nav: false,
                dots: false
            })
            .on('changed.owl.carousel', function (e) {
                if (!flag) {
                    flag = true;
                    $sync2.trigger('to.owl.carousel', [e.item.index, duration, true]);
                    flag = false;
                }
            });

        $sync2
            .owlCarousel({
                margin: 1,
                items: 3,
                nav: true,
                dots: false,
                nav: true,
                navText: [
                        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
                    ],
                center: false,
                responsive: {
                    0: {
                        items: 1,
                        autoWidth: false
                    },
                    400: {
                        items: 1,
                        autoWidth: false
                    },
                    500: {
                        items: 2,
                        center: false,
                        autoWidth: false
                    },
                    600: {
                        items: 3,
                        autoWidth: false
                    },
                    1200: {
                        items: 3,
                        autoWidth: false
                    }
                },
            })
            .on('click', '.owl-item', function () {
                $sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);

            })
            .on('changed.owl.carousel', function (e) {
                if (!flag) {
                    flag = true;
                    $sync1.trigger('to.owl.carousel', [e.item.index, duration, true]);
                    flag = false;
                }
            });

    };
}


// 4. Accordion Box
if ($('.accordion-box').length) {
    $('.accordion-box .acc-btn').click(function () {
        if ($(this).hasClass('active') !== true) {
            $('.accordion-box .acc-btn').removeClass('active');
        }

        if ($(this).next('.acc-content').is(':visible')) {
            $(this).removeClass('active');
            $(this).next('.acc-content').slideUp(500);
        } else {
            $(this).addClass('active');
            $('.accordion-box .acc-content').slideUp(500);
            $(this).next('.acc-content').slideDown(500);
        }
    });
}

//4. testimonialCarosule
function testimonial() {
    if ($('.testimonies').length) {
        $('.testimonies').owlCarousel({
            loop: true,
            margin: 29,
            nav: false,

            dots: true,
            items: 2,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 2
                }
            }
        });
    }
}
//4. serviceCarosule
function serviceCarosule() {
    if ($('.service-item').length) {
        $('.service-item').owlCarousel({
            loop: true,
            margin: 0,
            nav: true,
            navText: [
                    '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                    '<i class="fa fa-angle-right" aria-hidden="true"></i>'
                    ],
            dots: false,
            items: 4,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                600: {
                    items: 2
                },
                800: {
                    items: 3
                },
                1000: {
                    items: 3
                },
                1200: {
                    items: 4
                }
            }
        });
    }
}
// 5. testimonialCarosule
function testimonialitem() {
    if ($('.testimonies-item').length) {
        $('.testimonies-item').owlCarousel({
            loop: true,
            margin: 0,
            nav: false,

            dots: true,
            items: 1,
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1000: {
                    items: 1
                }
            }
        });
    }
}

//6. Jquery Tabs Box
if ($('.tabs-box').length) {
    //Tabs
    $('.tabs-box .tab-buttons .tab-btn').click(function (e) {

        e.preventDefault();
        var target = $($(this).attr('href'));

        target.parents('.tabs-box').children('.tab-buttons').children('.tab-btn').removeClass('active-btn');
        $(this).addClass('active-btn');
        target.parents('.tabs-box').children('.tab-content').children('.tab').fadeOut(0);
        target.parents('.tabs-box').children('.tab-content').children('.tab').removeClass('active-tab');
        $(target).fadeIn(300);
        $(target).addClass('active-tab');
    });

}
//7.  Main menu
function mainmenu() {
    //Submenu Dropdown Toggle
    if ($('.main-menu li.dropdown ul').length) {
        $('.main-menu li.dropdown').append('<div class="dropdown-btn"></div>');

        //Dropdown Button
        $('.main-menu li.dropdown .dropdown-btn').click(function () {
            $(this).prev('ul').slideToggle(500);
        });
    }

}

// 8. zebraDatePickerInit 
function zebraDatePickerInit() {
    if ($('input.datepicker').length) {
        $('input.datepicker').Zebra_DatePicker({
            default_position: 'below'
        });
    };
}



//9. Hide Loading Box (Preloader)
function handlePreloader() {
    if ($('.preloader').length) {
        $('.preloader').delay(200).fadeOut(500);
    }
}
//10. Scroll to a Specific Div
if ($('.scroll-to-target').length) {
    $(".scroll-to-target").click(function () {
        var target = $(this).attr('data-target');
        // animate
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 1000);

    });
}


//11. Update Scroll to Top
function headerStyle() {
    if ($('.main-header').length) {
        var windowpos = $(window).scrollTop();
        if (windowpos >= 200) {
            $('.main-header').addClass('fixed-header');
            $('.scroll-to-top').fadeIn(300);
        } else {
            $('.main-header').removeClass('fixed-header');
            $('.scroll-to-top').fadeOut(300);
        }
    }
}

headerStyle();

//12. Contact Form Validation
if ($('#contact-form').length) {
    $('#contact-form').validate({
        rules: {
            username: {
                required: true
            },
            lastname: {
                required: true
            },
            email: {
                required: true,
                email: true
            },
            phone: {
                required: true
            },
            message: {
                required: true
            },
            date: {
                required: true
            },
            category: {
                required: true
            },
            website: {
                required: true
            }
        }
    });
}
//Contact Form Validation
if ($(".contact-form").length) {
    $(".contact-form").validate({
        submitHandler: function (form) {
            var form_btn = $(form).find('button[type="submit"]');
            var form_result_div = '#form-result';
            $(form_result_div).remove();
            form_btn.before('<div id="form-result" class="alert alert-success" role="alert" style="display: none;"></div>');
            var form_btn_old_msg = form_btn.html();
            form_btn.html(form_btn.prop('disabled', true).data("loading-text"));
            $(form).ajaxSubmit({
                dataType: 'json',
                success: function (data) {
                    if (data.status == 'true') {
                        $(form).find('.form-control').val('');
                    }
                    form_btn.prop('disabled', false).html(form_btn_old_msg);
                    $(form_result_div).html(data.message).fadeIn('slow');
                    setTimeout(function () {
                        $(form_result_div).fadeOut('slow')
                    }, 6000);
                }
            });
        }
    });
}
//13. Elements Animation
if ($('.wow').length) {
    var wow = new WOW({
        boxClass: 'wow', // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset: 0, // distance to the element when triggering the animation (default is 0)
        mobile: false, // trigger animations on mobile devices (default is true)
        live: true // act on asynchronously loaded content (default is true)
    });
    wow.init();
}
// Dom Ready Function
jQuery(document).ready(function () {
    (function ($) {
        // add your functions
        revolutionSliderActiver();
        CounterNumberChanger();
        testimonial();
        testimonialitem();
        serviceCarosule()
        mainmenu();
        zebraDatePickerInit();
        singleGalleryCarousel();
    })(jQuery);
});
// instance of fuction while Window Load event
jQuery(window).load(function () {
    (function ($) {
        handlePreloader()

    })(jQuery);
});

(function ($) {

    /* ==========================================================================
       When document is Scrollig, do
       ========================================================================== */
    $(window).scroll(function () {
        headerStyle();


    });


})(window.jQuery);