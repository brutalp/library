import App from './App.svelte';

const app = new App({
	target: document.getElementById('wine-list'),
	props: {
		name: 'world'
	}
});

export default app;