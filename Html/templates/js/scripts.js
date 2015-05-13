/***************************************************
		SLIDESHOW
***************************************************/
$(document).ready(function() {
    $('.slideshow').cycle({
		fx: 'fade', // choose your transition type, ex: fade, scrollUp, shuffle, etc...
		pager: '#nav',
		speed: 1000,  // speed of the transition (any valid fx speed value)
		pause: true,     // true to enable "pause on hover" 
		timeoutFn: calculateTimeout,  // milliseconds between slide transitions (0 to disable auto advance)
		cleartype: true,  // true if clearType corrections should be applied (for IE) 
		cleartypeNoBg: true // set to true to disable extra cleartype fixing (leave false to force background color setting on slides)	
	});
});

// timeouts per slide (in seconds) 
var timeouts = [3,3,30,3]; 
function calculateTimeout(currElement, nextElement, opts, isForward) { 
    var index = opts.currSlide; 
    return timeouts[index] * 1000; 	}


/***************************************************
		CAROUSEL
***************************************************/
function mycarousel_initCallback(carousel) {
    jQuery('.carousel-next').bind('click', function() {
        carousel.next();
        return false;
    });

    jQuery('.carousel-prev').bind('click', function() {
        carousel.prev();
        return false;
    });
};

jQuery(document).ready(function() {
    jQuery(".carousel").jcarousel({
        scroll: 1,
        initCallback: mycarousel_initCallback,
        // This tells jCarousel NOT to autobuild prev/next buttons
        buttonNextHTML: null,
        buttonPrevHTML: null
    });
});

/***************************************************
		TESTIMONIALS
***************************************************/

// testimonials on layout1...
$(document).ready(function() {
    $('.testimonials').cycle({
		fx: 'fade', // choose your transition type, ex: fade, scrollUp, shuffle, etc...
		speed: 1000,  // speed of the transition (any valid fx speed value)
		pause: true,     // true to enable "pause on hover" 
		timeout: 4000,  // milliseconds between slide transitions (0 to disable auto advance)
		cleartype: true,  // true if clearType corrections should be applied (for IE) 
		cleartypeNoBg: true // set to true to disable extra cleartype fixing (leave false to force background color setting on slides)	
	});
});

// testimonials on layout2...
$(document).ready(function() {
    $('.testimonials2').cycle({
		fx: 'fade', // choose your transition type, ex: fade, scrollUp, shuffle, etc...
		speed: 1000,  // speed of the transition (any valid fx speed value)
		pause: true,     // true to enable "pause on hover" 
		timeout: 4000,  // milliseconds between slide transitions (0 to disable auto advance)
		cleartype: true,  // true if clearType corrections should be applied (for IE) 
		cleartypeNoBg: true // set to true to disable extra cleartype fixing (leave false to force background color setting on slides)	
	});
});

/***************************************************
		IMAGE ZOOM
***************************************************/
$(document).ready(function() {
	$("a.zoom img").mouseover(function(){
		$(this).stop(true,true);
		$(this).fadeTo(300, 0.6);
	});
	
	$("a.zoom img").mouseout(function(){
		$(this).fadeTo(400, 1.0);
	});

});

/***************************************************
		PRETTYPHOTO
***************************************************/

$(document).ready(function(){
	$("a[rel^='prettyPhoto']").prettyPhoto({animationSpeed:'slow',theme:'light_square',autoplay_slideshow: false});
});
