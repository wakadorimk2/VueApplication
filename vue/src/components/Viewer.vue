<template>
  <section class="section">
    <div class="container">
      <MagicGrid>
        <card
          v-for="(fav, i) in faves"
          :key="i"
          :title="fav.title"
          :body="fav.body"
        />
      </MagicGrid>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
import MagicGrid from 'vue-magic-grid';
import card from './Card.vue';

export default {
  name: 'Viewer',
  data() {
    return {
      faves: {},
    };
  },
  components: {
    MagicGrid,
    card,
  },
  methods: {
    getFaves() {
      const path = 'http://localhost:5000/faves';
      axios.get(path)
        .then((res) => {
          this.faves = res.data.faves;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getFaves();
  },
};
</script>
