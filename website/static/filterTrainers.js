// // /static/js/filterTrainers.js
// document.addEventListener('DOMContentLoaded', () => {
// 	const trainingTypeDropdown = document.getElementById('trainingType');
// 	const sizeDropdown = document.getElementById('size');
// 	const experienceDropdown = document.getElementById('experience');
// 	const cityDropdown = document.getElementById('city');
// 	const filteredTrainersContainer =
// 		document.querySelector('.filtered-trainers');

// 	const fetchFilteredTrainers = () => {
// 		const trainingType = trainingTypeDropdown.value;
// 		const size = sizeDropdown.value;
// 		const experience = experienceDropdown.value;
// 		const city = cityDropdown.value;

// 		const url = `/search-trainer?training_type=${trainingType}&size=${size}&experience=${experience}&city=${city}`;

// 		fetch(url)
// 			.then((response) => response.json())
// 			.then((data) => {
// 				// Clear existing filtered trainers
// 				filteredTrainersContainer.innerHTML = '';
// 				console.log(data.filtered_trainers);
// 				// Populate the container with the filtered trainers
// 				data.filtered_trainers.forEach((trainer) => {
// 					const trainerCard = document.createElement('div');
// 					trainerCard.classList.add('trainer-card');
// 					trainerCard.innerHTML = `
//             <h2>${trainer.name}</h2>
//             <p>Training Type: ${trainer.training_type}</p>
//             <p>Size: ${trainer.size}</p>
//             <p>Experience: ${trainer.experience}</p>
//             <p>City: ${trainer.city}</p>
//           `;
// 					filteredTrainersContainer.appendChild(trainerCard);
// 				});
// 			})
// 			.catch((error) => {
// 				console.error('Error fetching filtered trainers:', error);
// 			});
// 	};

// 	// Add event listeners for filter dropdowns
// 	trainingTypeDropdown.addEventListener('change', fetchFilteredTrainers);
// 	sizeDropdown.addEventListener('change', fetchFilteredTrainers);
// 	experienceDropdown.addEventListener('change', fetchFilteredTrainers);
// 	cityDropdown.addEventListener('change', fetchFilteredTrainers);

// 	// Fetch initial filtered trainers on page load
// 	fetchFilteredTrainers();
// });
