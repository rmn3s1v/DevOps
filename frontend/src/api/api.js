import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api",
});

/* ===== SENSORS ===== */

export const getSensors = () => api.get("/sensors");

export const createSensor = (data) =>
  api.post("/sensors", data);

export const updateSensor = (id, data) =>
  api.put(`/sensors/${id}`, data);

export const deleteSensor = (id) =>
  api.delete(`/sensors/${id}`);


/* ===== SENSOR DATA ===== */

export const getSensorData = (sensorId) =>
  api.get(`/sensors/${sensorId}/data`);

export const createSensorData = (sensorId, data) =>
  api.post(`/sensors/${sensorId}/data`, data);

export const updateSensorData = (sensorId, dataId, data) =>
  api.put(`/sensors/${sensorId}/data/${dataId}`, data);

export const deleteSensorData = (sensorId, dataId) =>
  api.delete(`/sensors/${sensorId}/data/${dataId}`);

export default api;
