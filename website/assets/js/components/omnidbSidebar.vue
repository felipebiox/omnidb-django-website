<template>

    <div class="omnidb-sidebar">

        <ul>
            <li v-for="item in items">[[ item.title ]]</li>
        </ul>

    </div>

</template>


<script>

  export default {
    name: 'omnidb-sidebar',
    props: {
      items: {
        type: Array,
        required: true
      }
    }
    methods: {
    }
  }

</script>
