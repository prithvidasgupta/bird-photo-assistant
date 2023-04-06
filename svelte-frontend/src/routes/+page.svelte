<!-- The base page for the components displayed on the webpage-->
<script>
  /** The Form component is responsible for most of the functionality 
  on the webpage. This file only controls the style. */
  import Form from "$lib/components/Form.svelte";
</script>

<div class="centered-div">
  <h1>Bird Photo Assistant</h1>
  <p>
    Check out the birds you can photograph in a place during one of the four
    seasons
  </p>
  <Form />
</div>

<style>
  .centered-div {
    margin: auto;
    width: 50%;
    padding: 50px;
    font-family: "Tangerine", serif;
    font-size: 24px;
  }
</style>
