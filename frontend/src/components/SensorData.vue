<template>
  <div class="data-block">
    <h4>Sensor Data</h4>

    <!-- Форма добавления данных -->
    <form @submit.prevent="addData" class="data-form">
      <input
        v-if="sensor.data_type === 'temperature'"
        v-model.number="value"
        type="number"
        step="0.1"
        placeholder="Temperature"
        required
      />

      <input
        v-if="sensor.data_type === 'humidity'"
        v-model.number="value"
        type="number"
        placeholder="Humidity"
        required
      />

      <input
        v-if="sensor.data_type === 'pressure'"
        v-model.number="value"
        type="number"
        placeholder="Pressure"
        required
      />

      <input
        v-if="sensor.data_type === 'light'"
        v-model.number="value"
        type="number"
        placeholder="Light"
        required
      />

      <button type="submit">Add</button>
    </form>

    <!-- Список данных -->
    <div v-if="dataList.length === 0">
      No data yet
    </div>

    <SensorDataItem
      v-for="d in dataList"
      :key="d.id"
      :sensor="sensor"
      :data="d"
      @reload="loadData"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {
  getSensorData,
  createSensorData
} from "../api/api";

import SensorDataItem from "./SensorDataItem.vue";

const props = defineProps({
  sensor: {
    type: Object,
    required: true
  }
});

const dataList = ref([]);
const value = ref(null);

/* ===== Загрузка данных ===== */

const loadData = async () => {
  try {
    const response = await getSensorData(props.sensor.id);
    dataList.value = response.data;
  } catch (error) {
    console.error("Error loading data:", error);
  }
};

/* ===== Добавление данных ===== */

const addData = async () => {
  if (value.value === null) return;

  const payload = {};
  payload[props.sensor.data_type] = value.value;

  try {
    await createSensorData(props.sensor.id, payload);
    value.value = null;
    await loadData();
  } catch (error) {
    console.error("Error adding data:", error);
  }
};

onMounted(loadData);
</script>

<style scoped>
.data-block {
  margin-top: 15px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: #fafafa;
}

.data-form {
  margin-bottom: 10px;
}

.data-form input {
  margin-right: 8px;
  padding: 4px;
}

.data-form button {
  padding: 4px 10px;
}
</style>
