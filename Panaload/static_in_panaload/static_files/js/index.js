// for the datepicker i used zebraDatepicker and animate.css
//http://daneden.github.io/animate.css/
// http://stefangabos.ro/jquery/zebra-datepicker/
$(document).ready(function(){
      $('.datepicker').Zebra_DatePicker({direction: 1,always_visible: 							$('#zebracontainer1')});
      	$('#datepickbox1').bind('click',function(){
      	$('.searchslide').addClass('active');
      	$('#zebracontainer1').addClass('active');	
      });
      $('.dp_daypicker, .dp_footer').bind('click',function(){
      $('.searchslide').removeClass('active');
      $('.zbc').removeClass('active');
});
});