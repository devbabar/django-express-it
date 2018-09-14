$(document).ready(function(){

	// ===========================================================
	// ---------- Navbar moves as we scroll down ------------start
	// ===========================================================

 	 $(window).on('scroll', fixHeader);
		var header = $('nav');
		var headerOffset = header.offset().top;
		function fixHeader(evt){
			var currentScroll = $(window).scrollTop()
			// console.log(headerOffset, currentScroll);
			if(headerOffset <= currentScroll){
				header.addClass('navbar-fixed-top').css({"right":"10px","left":"10px"});
			}
			else {
			 header.removeClass('navbar-fixed-top')
			}
		}



	// ===========================================================
	// ---------- Navbar moves as we scroll down ------------ends
	// ===========================================================


	// ==============================================================
	// --------Custom funtion to animate gallery section--------Start
	// ==============================================================

	function slideinFunction(div,position,speed,completed){
		div.animate({left:position}, speed,completed);
		// div.animate({right:position}, speed,completed);

	};

	// Reset the div after window size is changed
	function resizeWidth(){
		$(window).resize(function(){
			
			var $windowSize = $(window).width();
			
			if ($windowSize >= 1200){
				var lgBox = 10, mdBox = 390, smBox = 765;
			
			} else if ($windowSize >= 992 && $windowSize <= 1199){
				var lgBox = 10, mdBox = 350, smBox = 680;
			
			} else if ($windowSize >= 768 && $windowSize <= 991){
				var lgBox = 10, mdBox = 265, smBox = 525;
			}

			$(".imgbox").css('left',lgBox);
			$(".imgbox2").css('left',mdBox);
			$(".imgbox3").css('left',smBox);
		
		});
	};

	// ---------
	// Method 1:
	// ---------

	// Calling custom animate functions for different window size
	function checkWidth(){
		
		var $windowSize = $(window).width();
		
		if ($windowSize >= 1200){
			var lgBox = 10, mdBox = 390, smBox = 765;
		
		} else if ($windowSize >= 992 && $windowSize <= 1199){
			var lgBox = 10, mdBox = 350, smBox = 680;
		
		} else if ($windowSize >= 768 && $windowSize <= 991){
			var lgBox = 10, mdBox = 265, smBox = 525;
		}

		slideinFunction($('.imgbox'),lgBox,1000,function(){
			slideinFunction($('.imgbox2'),mdBox,1000, function(){
				slideinFunction($('.imgbox3'),smBox,1000);
			});
		});
	};
	// -----------------------END------------------------------------
	
	// ================
	// Execute on load
	// ================

	resizeWidth();
	checkWidth();

	var timer;
	function fading(){	
		timer = setInterval(function(){
			$("#gallery").fadeOut(1000).fadeIn(100);
		},3000);
	};
	fading();

	$("#gallery").hover(function(){
		clearInterval(timer);

	}, function(){
		fading();
	});

	// =====================================================
	// Switch between Day & Night photography tips--Start
	// =====================================================

	// -------- Calling with anonymous Function -------------
	$(function(){
		var $dayPhotography   = $("#day-photography");
		var $nightPhotography = $("#night-photography");

		 $nightPhotography.hide();
			$('#night-photography-btn').on("click",function(e){
				e.preventDefault();

				$nightPhotography.show() && $dayPhotography.hide();

				$('#day-photography-btn').on("click",function(){	
					$dayPhotography.show() && $nightPhotography.hide();		
				});
			});
	});

	
	// ==========================================
	// Article goes back to it's position --Start
	// ==========================================
	$(function(){
		$("#day-photography div, #night-photography div").mouseleave(function(){
			$(this).animate({ scrollTop:0},"fast");
		// $("#day-photography div").scrollTop(0);
		});
	});
	// ==========================================
	// Article goes back to it's position ---Ends
	// ==========================================


    // ===================================================================================
	// Div slide in and visible when scroll with arguments, Left, Right & Speed -----start
	// Method 1: Reuseable Function
	// ===================================================================================
	
	// Define variables globally so variable scope will be beyond any particular function
	var windowHeight = $(window).height();
	var windowScrollPositionTop = $(window).scrollTop();
	var windowScrollPositionBottom = windowHeight + windowScrollPositionTop;

	$.fn.revealOnScroll = function(direction, speed){
		return this.each(function(){

			var objectOffset = $(this).offset();
			var objectOffsetTop = objectOffset.top;

			// we need to run this code only once we scroll
			// Do NOT use hidden class if your are using Bootstrap, name something else like "closed"
			if (!$(this).hasClass("closed")){

				// Run the code by checking it's direction
				if (direction == "right"){
					$(this).css({
						"opacity" : 0,
						"right"	  : "700px",
						"position": "relative"
					});
				} else if (direction == "left"){
					$(this).css({
						"opacity" : 0,
						"right"	  : "-700px",
						"position": "relative"
					});
				} else {
					$(this).css({
						"opacity" : 0						
					});
				}

				$(this).addClass("closed");
			} //------checking direction ends
			
			// we don't want the code to be keep running after animation is completed
			if(!$(this).hasClass("animation-complete")){
				if(windowScrollPositionBottom > objectOffsetTop){
					$(this).animate({"opacity":1, "right":0}, speed).addClass("animation-complete");
				}
			}
		});

	} //function ends


	$(window).scroll(function(){

		windowHeight = $(window).height();
		windowScrollPositionTop = $(window).scrollTop();
		windowScrollPositionBottom = windowHeight + windowScrollPositionTop;
	
		// Calling revealOnScroll()
		$(".display-gallery").revealOnScroll("",10000);

		// Calling revealOnScroll() with arguments, Left, Right & Speed
		$(".about").revealOnScroll("left", 2000);
		$(".about2").revealOnScroll("right",2000);
		$(".about3").revealOnScroll("left",2000);

	});

	// ===============================================
	// Div slide in and visible when scroll ------ends
	// ===============================================

}); 
// ----------document. ready() ends here -----------


//=================
// EXTRA CODE -----
//=================


	// ===================================================================================
	// Div slide in and visible when scroll with arguments, Left, Right & Speed -----start
	// Method 2: None Reuseable Function
	// ===================================================================================


	// $(".about").css("opacity", 0);
	// $(window).scroll(function(){
	// 	// $(".about").css("opacity", 0);

	// 	var windowHeight = $(window).height();
	// 	var windowScrollPositionTop = $(window).scrollTop();
	// 	var windowScrollPositionBottom = windowHeight + windowScrollPositionTop;
	// 	var objectOffset = $(".about").offset();
	// 	var objectOffsetTop = objectOffset.top;

	// 	$(".status").html(objectOffsetTop);

	// 	// we don't want the code to be keep running after animation is completed
	// 	if(!$(".about").hasClass("animation-complete")){
	// 		if(windowScrollPositionBottom > objectOffsetTop){
	// 			$(".about").animate({"opacity":1}, 5000).addClass("animation-complete");
	// 		}
	// 	}

	// });
	// ===============================================
	// Div slide in and visible when scroll ------ends
	// ===============================================

		// ---------
		// Method 2:
		// Calling custom animate functions for different window size
		// ---------
		// $(window).resize(function(){
		// if ($(window).width() >= 1200){
		// 	slideinFunction($('.imgbox'),10,1000,function(){
		// 		slideinFunction($('.imgbox2'),390,1000, function(){
		// 			slideinFunction($('.imgbox3'),765,1000);
		// 		});
		// 	});
		// } else if ($(window).width() >= 992){
		// 	slideinFunction($('.imgbox'),10,1000,function(){
		// 		slideinFunction($('.imgbox2'),390,1000, function(){
		// 			slideinFunction($('.imgbox3'),665,1000);
		// 		});
		// 	});
		// } else if ($(window).width() >= 762){
		// 	slideinFunction($('.imgbox'),10,1000,function(){
		// 		slideinFunction($('.imgbox2'),390,1000, function(){
		// 			slideinFunction($('.imgbox3'),665,1000);
		// 		});
		// 	});
		// }
		// };

	// ==============================================================
	// --------Custom funtion to animate gallery section---------ends
	// ==============================================================

	

	
	
	











