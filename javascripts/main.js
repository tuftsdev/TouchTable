$(document).ready(function(){
  $(".menu-wrapper").click(function(){
    $(".header-nav").slideToggle();
  })
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 500);
        return false;
      }
    }
  });
  $(window).resize(function(){
    resizeSidebar();
  })
  resizeSidebar();
  function resizeSidebar(){
    height = $(window).height();
    newHeight = height-65;
    $('.sidebar-wrapper').css('height', newHeight+'px');
  }
  if(!window.webkitURL && window.location.href.indexOf("about") == -1){
    $(".content").addClass('scroll');
  }
});
