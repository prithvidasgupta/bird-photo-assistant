<script>
  import Form from "$lib/components/Form.svelte";
  function handleOnSubmit() {
    console.log("I'm the handleOnSubmit() in App.svelte");
  }
</script>

<div class="centered-div">
  <h1>Bird Photo Assistant</h1>
  <p>Check out the birds you can photograph in a place during one of the four seasons</p>
  <Form on:submit={handleOnSubmit} />
</div>

<style>
  .centered-div {
    margin: auto;
    width: 50%;
    padding: 50px;
    font-family: 'Tangerine', serif;
		font-size: 24px;
  }
</style>
