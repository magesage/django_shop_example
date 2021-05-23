var mainMenu = (function() {

	var $listItems = $( '#mainmenu > ul > li' ),
		$menuItems = $listItems.children( 'a' ),
		$body = $( 'body' ),
		current = -1;

	function init() {
		$menuItems.on( 'click', open );
		$listItems.on( 'click', function( event ) { event.stopPropagation(); } );
	}

	function open( event ) {

		var $item = $( event.currentTarget ).parent( 'li.has-submenu' ),
			idx = $item.index();
		if($item.length != 0){
			if( current !== -1 ) {
				$listItems.eq( current ).removeClass( 'mainmenu-open' );
			}

			if( current === idx ) {
				$item.removeClass( 'mainmenu-open' );
				current = -1;
			}
			else {
				$item.addClass( 'mainmenu-open' );
				current = idx;
				$body.off( 'click' ).on( 'click', close );
			}
			return false;
		}
		else window.location = $item.find('a').attr('href');
	}

	function close( event ) {
		$listItems.eq( current ).removeClass( 'mainmenu-open' );
		current = -1;
	}

	return { init : init };

})();

//hide_it Скрытие некоторых элементов меню при прокрутке страницы вниз (hide_mob для мобильных устройств меню скрывается полностью)
//Меняется класс default на класс fixed у элемента #menu при прокрутке страницы вниз. Обратно меняется только в самом верху страницы. Этот костыль нужен чтобы исправить баг с заползанием контента под панель меню.
var lastScrollTop = 0;
	$(window).scroll(function(event){
		var $menu = $("#menu");
		var st = $(this).scrollTop();
		if (st > lastScrollTop){
			$(".hide_it").hide();
			$menu.removeClass("default").addClass("fixed");
			if ($(window).width() <= '999'){
				$(".hide_mob").hide(10);
			} else {
				$(".hide_mob").show(10);
			}
		} else {
			$(".hide_it").show();
			$(".hide_mob").show(10);
			if($(this).scrollTop() <= 10 && $menu.hasClass("fixed")) {
			$menu.removeClass("fixed").addClass("default");
			}
		}
		lastScrollTop = st;
	});

//hide_mob2 скрытие пунктов меню в мобильной версии, потому что не помещается в экран.
function windowSize(){
	if ($(window).width() <= '480'){
			$(".hide_mob2").hide(10);
	} else {
		$(".hide_mob2").show(10);
	}
}
$(window).on('load resize',windowSize);