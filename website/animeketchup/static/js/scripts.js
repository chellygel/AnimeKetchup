// Wait for the DOM content to be fully loaded before executing the code inside this block.
document.addEventListener("DOMContentLoaded", function () {
    // Fetch the anime list data from the URL.
    fetch("http://127.0.0.1:8000/api/anime/")
        // Parse the response as JSON.
        .then(response => response.json())
        // Handle the JSON data.
        .then(data => {
            // Obtain the container elemenr where anime information will be displayed.
            const animeContainer = document.getElementById("anime-container");

            // Loop through each item.
            data.forEach(anime => {
                // Create a 'div' element to contain each anime and it's information.
                const animeBox = document.createElement("div");
                // Add a CSS class to the div.
                animeBox.classList.add("anime-box");

                // Create a 'h2' element for the anime's name.
                const animeName = document.createElement("h2");
                animeName.classList.add("anime-name");
                // Set the text content of the h2 element to the anime's name.
                animeName.textContent = anime.name;

                // Create a 'p' element for the description.
                const animeDescription = document.createElement("p");
                animeDescription.classList.add("anime-description");
                animeDescription.textContent = anime.description;

                // Apend the name and description elements to the anime box.
                animeBox.appendChild(animeName);
                animeBox.appendChild(animeDescription);

                // Append the anime box to the container element.
                animeContainer.appendChild(animeBox);
            });
        })
        // Handles any errors that occur during the fetch operation.
        .catch(error => console.error("Error fetching anime data:", error));
});
