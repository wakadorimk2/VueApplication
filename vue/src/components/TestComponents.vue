<template>
    <v-container>
        <v-row>
            <v-col cols="12" sm="12" md="6">
                <v-card>
                    <v-parallax
                        :height="windowSize.y"
                        :width="windowSize.x"
                        src="https://pbs.twimg.com/media/EJ4dZGZU4AEq_by?format=jpg&name=900x900"
                    >
                    </v-parallax>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
  data: () => ({
    windowSize: {
      x: 0,
      y: 0,
    },

  }),

  mounted() {
    this.onResize();
  },

  methods: {
    onResize() {
      this.windowSize = { x: window.innerWidth, y: window.innerHeight };
    },
  },
};
</script>
