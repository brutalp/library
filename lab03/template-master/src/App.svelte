<main>
    <div class="row">
        {#each wines as item}
            <div class="col-lg-4 mb-5 col-md-6">
                <div class="wine_v_1 text-center pb-4">
                    <a href="shop-single.html" class="thumbnail d-block mb-4"><img src="{ item.img }" alt="Image" class="img-fluid"></a>
                    <div>
                        <h3 class="heading mb-1"><a href="#">{ item.title }</a></h3>
                        <span class="price">{ item.price }</span>
                    </div>
                    <div class="wine-actions">
                        <h3 class="heading-2"><a href="#">{ item.title }</a></h3>
                        <span class="price d-block">{ item.price }</span>
                        <div class="rating">
                            <span class="icon-star"></span>
                            <span class="icon-star"></span>
                            <span class="icon-star"></span>
                            <span class="icon-star"></span>
                            <span class="icon-star-o"></span>
                        </div>
                        <a href="cart.html" class="btn add"><span class="icon-shopping-bag mr-3"></span>Add to Cart</a>
                    </div>
                </div>
            </div>
        {/each}
        <ul class="pagination">
            {#each winePages as page}
                <li>
                    <button on:click="{() => changePage(page)}">
                        {page}
                    </button>
                </li>
            {/each}
        </ul>
    </div>
</main>

<script>
    import { onMount, onDestroy } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js'
	const CSRF_TOKEN = Cookies.get('csrftoken');
	const SHOP_URL = getRef('shop-ref');

    let wines = [];
    let totalPages = null;
    let currentPage = 1;
    let winePages = [];

    function createPagesArray(total){
        let arr = []
        for(let i = 1; i <= total; i++){
            arr.push(i)
        }
        return arr
    }

    function getTotalPages(length){
        if (length % 3 == 0){
            return length / 3
        } else {
            return length / 3 + 1
        }
    }

    function changePage(page){
        fetch(SHOP_URL + page).then(res => {
            return res.json()
        }).then(result => {
            posts = result
            currentPage = page
        })
    }

    function getRef(id) {return document.getElementById(id).href;};
    onMount(async () => {
        const response = await fetch(SHOP_URL, {
                                        headers: {
                                            'Accept': 'application/json, text-plain, */*',
                                            'X-Requested-With': 'XMLHttpRequest',
                                        }, });
        let wines_json = await response.json();
        wines = wines_json['wines'];
        totalPages = getTotalPages(wines.length)
        winePages = createPagesArray(totalPages)
    });
</script>

<style>

</style>