<template>
    <div>
        <myheader></myheader>
        <h1 v-if='msg.length > 0'>{{ msg }}</h1>
        <h1 v-else>no text</h1>
        <input type='text' v-model='msg'>
        <button @click='clear()'>clear</button>
        <button @click='set()'>set</button>
        <br>
        <img :src="image_src">
    </div>
</template>

<script>
import myheader from './components/myheader'

export default {
    components : {
        myheader
    },
    data () {
        return {
            msg : 'vue tutorial',
            image_src : 'https://pbs.twimg.com/media/EJaKTwcUcAA-kuk?format=jpg&name=900x900'
        }
    },
    methods : {
        clear () {
            this.msg = ''
            this.image_src = ''
        },
        set() {
            this.image_src = 'https://pbs.twimg.com/media/EJaKTwcUcAA-kuk?format=jpg&name=900x900'
        }
    },
}
</script>