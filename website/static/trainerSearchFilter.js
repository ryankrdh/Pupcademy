// jQuery(document).ready(function ($) {
// 	// Attach an event listener to the filter form submission
// 	$('#filterForm').on('submit', function (event) {
// 		event.preventDefault(); // Prevent the default form submission

// 		// Serialize the form data
// 		var formData = $(this).serialize();

// 		// Make an AJAX request to the search-trainer endpoint with the form data
// 		$.ajax({
// 			url: '/search-trainer',
// 			type: 'GET',
// 			data: formData,
// 			success: function (response) {
// 				// Replace the search results container with the updated search results
// 				$('#searchResultsContainer').html(response);
// 			},
// 			error: function (error) {
// 				console.error('Error:', error);
// 			},
// 		});
// 	});
// });
