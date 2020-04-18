<script>
    import { onMount, onDestroy } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js'
	const CSRF_TOKEN = Cookies.get('csrftoken');
	const SHOP_URL = getRef('shop-ref');

    let wines = [
    ];

    function getRef(id) {return document.getElementById(id).href;};
    console.log(SHOP_URL);
    onMount(async () => {
        const response = await fetch(SHOP_URL, {
                                        headers: {
                                            'Accept': 'application/json, text-plain, */*',
                                            'X-Requested-Width': 'XMLHttpRequest',
                                        }, });
        wines = await response.json();
        console.log(wines);
    });
</script>

<main>
    {#each wines as item}

    {/each}
</main>

<style>

</style>