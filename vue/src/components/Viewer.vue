<template>
  <v-card
    class="mx-auto"
    :max-width="windowSize.x"
    :max-height="windowSize.y"
  >
    <v-container fluid fill-height class="grey lighten-5">
      <v-btn
        fab
        bottom
        right
        fixed
        color=#f99
      >
        <v-icon color=#fff>mdi-heart</v-icon>
      </v-btn>
      <v-carousel
        hide-delimiters
        :show-arrows="showArrows"
        :height="windowSize.y"
        :progress="true"
        :show-arrows-on-hover="true"
        :vertical="true"
        >
        <v-carousel-item
          v-for="(fav, index) in faves"
          :key="index"
          :src="fav.src"
        >
        </v-carousel-item>
      </v-carousel>
    </v-container>
  </v-card>
</template>


<script>
import axios from 'axios';

export default {
  name: 'Viewer',
  data: () => ({
    faves: {},
    windowSize: {
      x: 0,
      y: 0,
    },
    display: 'small',
    loadMore: true,
  }),
  /*
  created() {
    this.getFaves();
  }, */
  mounted() {
    this.onResize();
    this.getFaves();
  },

  methods: {
    onResize() {
      this.windowSize = { x: window.innerWidth, y: window.innerHeight };
    },
    getFaves() {
      const path = 'http://localhost:5000/faves';
      axios.get(path, {
        params: {
          page: this.page + 1,
          per_page: this.pageSize,
        },
      })
        .then((res) => {
          this.faves = res.data.faves;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
