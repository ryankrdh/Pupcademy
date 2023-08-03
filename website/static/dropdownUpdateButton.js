// Function for the dog breed dropdown menu when clicked!
function updateButton(breedName, imageUrl) {
	const dropdownButton = document.getElementById('dropdownMenuButton');
	dropdownButton.innerHTML = `
        <img src="${imageUrl}" alt="${breedName}" width="30" height="30" class="mr-2">${breedName}
        <span class="caret"></span>
        `;

	// Capture the selected dog's information
	const dogNameInput = document.getElementById('dogNameInput');
	const dogImageInput = document.getElementById('dogImageInput');
	dogNameInput.value = breedName;
	dogImageInput.value = imageUrl;

	// Clear the selected dog section if the user changes the selection
	const selectedDogDiv = document.getElementById('selectedDog');
	selectedDogDiv.innerHTML = '';
}
