<template>
  <div class="lesson">
    <div>
      <button @click="getStepInstruction">Provide Start and End Coordinates:</button>
    </div>
    <div>
      <input 
        v-model="start"
        type="text"
      />
    </div>
    <div>
      <input 
        v-model="end"
        type="text"
      />
    </div>
    <textarea v-model="result"> </textarea>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Lesson",
  data() {
    return {
      start: "",
      end: "",
      result: "Did not change"
    }
  },
  methods: {
    async getStepInstruction() {
     const path = 'http://0.0.0.0:5000/api/v1/instructions';
      axios.get(path, {params: {start: this.start, end: this.end}})
        .then((res) => {
          this.result = JSON.stringify(res.data)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

