// $(function() {

// 	$('#product_dialog').modal({
	
// 	});


// });//ready

$(function() {

	// $('#shoppingCart').modal({
	// 		  	show: false,
	// });//modal

		$('#search').change(function() {
			searchTerms = document.getElementById("search").value;
			//window.location.href = '/homepage/shoppingCart.filter/'
	  		console.log(searchTerms)
	  		$.ajax({
  			url: '/homepage/product.filter/' + searchTerms,
  			success: function(data){
  				$('#DisplayProducts').find('.displaystuff').html(data)
  			},//success
  		});//ajax
	  		console.log("got here");
  	});//click

		$('.filter').on('click', function() {
			searchTerms = document.getElementById("search").value;
			//window.location.href = '/homepage/shoppingCart.filter/'
	  		console.log(searchTerms)
	  		$.ajax({
  			url: '/homepage/product.filter/' + searchTerms,
  			success: function(data){
  				$('#DisplayProducts').find('.displaystuff').html(data)
  			},//success
  		});//ajax
	  		console.log("got here");
  	});//click

		$('.add_button').on('click', function() {

			var pid = $(this).attr('data-pid');
			var qty = $(this).attr('data-qty');

	  		$('#shoppingCart').modal('show');
	  		$.ajax({
  			url: '/homepage/shoppingCart.add/' + pid + '/' + 1,
  			success: function(data){
  				$('#shoppingCart').find('.modal-body').html(data)
  			},//success
  		});//ajax
  	});//click

		// $.loadmodal({
		// 	url: "/homepage/product_detail/" + pid,
		// 	title: 'Shopping Cart'
		// 	width: '700px',
		// });

	});



