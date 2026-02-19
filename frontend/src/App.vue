<template>
  <div>
    <h1>IoT Agriculture Dashboard</h1>

    <SensorForm @created="reload" />
    <SensorList ref="listRef" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import SensorList from "./components/SensorList.vue";
import SensorForm from "./components/SensorForm.vue";

const listRef = ref(null);

const reload = () => {
  window.location.reload();
};
</script>
