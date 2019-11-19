<template>
  <span>Message: {{faves[0] }}</span>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Viewer',
  data() {
    return {
      faves: {},
    };
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
