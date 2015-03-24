$(function(){
	$('#id_username').on('change', function(){
		var username = $(this).val();
		console.log(username);
		console.log('world');
		$.ajax({
			url: '/homepage/index.check_username/',
			data: {
				'u': username,
			},
			success: function(resp){
				if (resp == '1') {
					$('#id_username_message').text("This is a good username");

				}
				else {
					$('#id_username_message').text("This username is already taken");
				}
				console.log(resp);
			},//success
		});//ajax
	}); //on change
	
	//alert('hi');
	console.log('world');

});