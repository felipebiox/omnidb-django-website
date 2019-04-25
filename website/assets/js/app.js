const app = new Vue({
  el: '#omnidb-django-website',
  delimiters: ['[[', ']]'],
  components: {
    omnidbSidebar
  },
  data() {
    return {
      widgets: new Bag(WIDGETS),
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
