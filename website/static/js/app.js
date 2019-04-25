
const app = new Vue({
  el: '#omnidb-django-website',
  delimiters: ['[[', ']]'],
  data() {
    return {
      umTeste: 'só um teste'
    }
  },
  mounted: function() {
    console.warn('foi');
  },
  methods: {
    initialize () {

    }
  }
});

window.app = app;


app.initialize();
