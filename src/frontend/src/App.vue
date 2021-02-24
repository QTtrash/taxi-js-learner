<template>
  <!-- <Lesson /> -->
  <Exam />
</template>

<script>
//import Lesson from './components/Lesson.vue';
import Exam from './components/Exam.vue'

export default {
  name: "App",
  components: {
    //Lesson,
    Exam
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
