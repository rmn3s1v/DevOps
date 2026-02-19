<template>
  <div class="data-item">
    <div v-if="!isEditing">
      {{ displayValue }}
      <small>{{ data.timestamp }}</small>

      <button @click="startEdit">Edit</button>
      <button @click="remove">Delete</button>
    </div>

    <div v-else>
      <input v-model.number="editValue" />

      <button @click="save">Save</button>
      <button @click="cancel">Cancel</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { updateSensorData, deleteSensorData } from "../api/api";

const props = defineProps(["sensor", "data"]);
const emit = defineEmits(["reload"]);

const isEditing = ref(false);
const editValue = ref(null);

const displayValue = computed(() => {
  return (
    props.data.temperature ??
    props.data.humidity ??
    props.data.pressure ??
    props.data.light
  );
});

const startEdit = () => {
  isEditing.value = true;
  editValue.value = displayValue.value;
};

const cancel = () => {
  isEditing.value = false;
};

const save = async () => {
  const payload = {};
  payload[props.sensor.data_type] = editValue.value;

  await updateSensorData(
    props.sensor.id,
    props.data.id,
    payload
  );

  isEditing.value = false;
  emit("reload");
};

const remove = async () => {
  await deleteSensorData(
    props.sensor.id,
    props.data.id
  );

  emit("reload");
};
</script>
