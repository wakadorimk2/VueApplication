<template>
  <v-card
    class="mx-auto"
    :max-width="windowSize.x"
  >
    <v-container fluid fill-height>
      <v-btn
        fab
        bottom
        right
        fixed
        color=#f99
      >
        <v-icon color=#fff>mdi-heart</v-icon>
      </v-btn>
        <scroll-loader :loader-method="getFaves" :loader-enable="loadMore">
          <v-row dense>
            <v-col
              v-for="(fav, index) in faves"
              :key="index"
              :cols="fav.sizes[display]['h']"
            >
              <v-card flat tile>
                <v-img
                  :src="fav.src"
                  :height="windowSize.y/5"
                  :width="fav.sizes[display]['w']/2"
                  aspect-ratio="1"
                >
                </v-img>
              </v-card>
            </v-col>
          </v-row>
        </scroll-loader>
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
