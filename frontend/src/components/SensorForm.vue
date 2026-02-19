<template>
  <form @submit.prevent="submit">
    <input v-model="name" placeholder="Sensor name" />
    <input v-model="ip" placeholder="IP address" />

    <select v-model="type">
      <option value="temperature">Temperature</option>
      <option value="humidity">Humidity</option>
      <option value="pressure">Pressure</option>
      <option value="light">Light</option>
    </select>

    <button type="submit">Add Sensor</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import { createSensor } from "../api/api";

const emit = defineEmits(["created"]);

const name = ref("");
const ip = ref("");
const type = ref("temperature");

const submit = async () => {
  await createSensor({
    name: name.value,
    ip: ip.value,
    data_type: type.value,
  });

  name.value = "";
  ip.value = "";
  type.value = "temperature";

  emit("created");
};
</script>
