$(function() {

	$('#checkout_btn').on('click', function(){
	$('#shoppingCart').modal({
		show: false,
	});
    window.location.href = '/homepage/checkout/'
  	});//click

	$('#show_login_dialog').on('click', function () {
		console.log('Im here!!')
		$.loadmodal({
			url: '/homepage/login.loginform/',
			title: 'Sign In',
		});
	});
});