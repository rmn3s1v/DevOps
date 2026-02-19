<template>
  <div>
    <SensorItem
      v-for="sensor in sensors"
      :key="sensor.id"
      :sensor="sensor"
      @reload="loadSensors"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getSensors } from "../api/api";
import SensorItem from "./SensorItem.vue";

const sensors = ref([]);

const loadSensors = async () => {
  const response = await getSensors();
  sensors.value = response.data;
};

onMounted(loadSensors);
</script>
