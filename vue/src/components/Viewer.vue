<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <table class="table table-hover">
          <tbody>
            <tr v-for="(fav, index) in faves" :key="index">
              <td><img :src=fav.url width=100></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
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
