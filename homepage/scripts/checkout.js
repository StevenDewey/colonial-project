$(function(){
  $(document).ready (function(){
    $('#checkout_login').modal('show');
     $.ajax({
       url: '/homepage/login.loginform/',
       success: function(data){
         $('#checkout_login').find('.modal-body').html(data)
       },//success
     });//ajax
    });//load
   $('#login_submit').on('click', function() {
    console.log('hellow')
  	$('#checkout_login').modal('hide');
	 });
});//ready