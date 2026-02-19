<template>
  <div class="sensor-card">
    <div v-if="!isEditing">
      <strong>{{ sensor.name }}</strong>
      ({{ sensor.ip }}) - {{ sensor.data_type }}

      <button @click="startEdit">Edit</button>
      <button @click="remove">Delete</button>
      <button @click="showData = !showData">Data</button>
    </div>

    <div v-else>
      <input v-model="editName" />
      <input v-model="editIp" />

      <select v-model="editType">
        <option value="temperature">Temperature</option>
        <option value="humidity">Humidity</option>
        <option value="pressure">Pressure</option>
        <option value="light">Light</option>
      </select>

      <button @click="save">Save</button>
      <button @click="cancel">Cancel</button>
    </div>

    <SensorData
      v-if="showData"
      :sensor="sensor"
    />
  </div>
</template>

<script setup>
import { ref } from "vue";
import { updateSensor, deleteSensor } from "../api/api";
import SensorData from "./SensorData.vue";

const props = defineProps(["sensor"]);
const emit = defineEmits(["reload"]);

const isEditing = ref(false);
const showData = ref(false);

const editName = ref("");
const editIp = ref("");
const editType = ref("");

const startEdit = () => {
  isEditing.value = true;
  editName.value = props.sensor.name;
  editIp.value = props.sensor.ip;
  editType.value = props.sensor.data_type;
};

const cancel = () => {
  isEditing.value = false;
};

const save = async () => {
  await updateSensor(props.sensor.id, {
    name: editName.value,
    ip: editIp.value,
    data_type: editType.value
  });

  isEditing.value = false;
  emit("reload");
};

const remove = async () => {
  await deleteSensor(props.sensor.id);
  emit("reload");
};
</script>
