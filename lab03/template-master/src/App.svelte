<main>
    <div class="row">

        {#each winesCut as item}
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
                    <button on:click="{() => sliceForPagination(page, wines)}">
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
    let page = null;
    let currentPage = 1;
    let winePages = [];
    let winesCut = [];

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

    function sliceForPagination(page, wines){
        console.log(page)
        if (page == 1){
           winesCut = wines.slice(0, 3)
        } else if (page == 2){
            winesCut = wines.slice(3, 6)
        } else if (page == 3){
            winesCut = wines.slice(7, 10)
        } else {
            console.log('при инициализации я залез сюда')
            winesCut = wines.slice(0, 3)
        }
        return winesCut
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
        totalPages = getTotalPages(wines.length);
        winePages = createPagesArray(totalPages);
        sliceForPagination(page, wines);
    });

</script>

<style>

</style>