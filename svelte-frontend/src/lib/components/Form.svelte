<script>
    let place = "";
    let season = "";
    let num_birds = "";
    let loading = false;
    /**
     * @type {{ error: any; birds: any; } | null}
     */
    let results = null;
    let error = false;
    /**
     * Submit the HTML form to send the HTTP request to the backend server.
     * The returned response is parsed using a Svelte for loop to populate the
     * page.
     * 
     * Current issues include:
     * 1. Changing the text in the text box does not remove already loaded content
     */
    async function submitForm() {
        loading = true;
        try {
            // Create an object with the input data
            const data = {
                place,
                season,
                num_birds,
            };

            // Send the data to the REST API
            const response = await fetch(
                `http://127.0.0.1:8000/place/${place}/season/${season.toLowerCase()}/birds/${num_birds}`,
                {
                    method: "GET",
                }
            );
            loading = false;

            // Parse the response
            results = await response.json();

            if (results && results.error) {
                error = true;
            }

            // Display the results
            // Or update a component property to show results in the UI
        } catch (error) {
            console.error(error);
        }
    }

    function clearWindow() {
        results = null;
    }
</script>

<form on:submit|preventDefault={submitForm} on:change={clearWindow}>
    <label for="place">Place:</label>
    <input bind:value={place} type="text" id="place" />

    <label for="season">Season:</label>
    <select bind:value={season} id="season" name="season">
        <option value="Fall">Fall</option>
        <option value="Winter">Winter</option>
        <option value="Spring">Spring</option>
        <option value="Summer">Summer</option>
    </select>

    <label for="numBirds">Number of Birds:</label>
    <select bind:value={num_birds} id="numBirds" name="numBirds">
        <option value="2">2</option>
        <option value="5">5</option>
        <option value="10">10</option>
        <option value="15">15</option>
    </select>

    <button type="submit">Submit</button>
</form>

{#if loading}
    <h3>Loading. Please wait...</h3>
{/if}

{#if error}
    <h2 style="color: red;">HTTP Error Ocurred</h2>
{:else if results && !error}
    <h2>Here are the top {num_birds} birds for {place}:</h2>
    <ul>
        {#each results.birds as bird}
            <li>
                <p>
                    <strong style="color:brown">Bird:</strong>
                    {bird.common_name}
                </p>
                <p>
                    <strong style="color: brown;">Scientific Name:</strong>
                    <i>{bird.scientific_name}</i>
                </p>
            </li>
        {/each}
    </ul>
{/if}
