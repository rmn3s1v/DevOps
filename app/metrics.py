from prometheus_client import Counter, Gauge

sensors_created_total = Counter(
    "iot_sensors_created_total",
    "Total number of created sensors",
    ["data_type"]
)

sensor_create_errors_total = Counter(
    "iot_sensor_create_errors_total",
    "Total number of failed sensor create operations",
    ["reason"]
)

sensor_data_created_total = Counter(
    "iot_sensor_data_created_total",
    "Total number of created sensor data records",
    ["data_type"]
)

sensor_data_create_errors_total = Counter(
    "iot_sensor_data_create_errors_total",
    "Total number of failed sensor data create operations",
    ["reason"]
)

sensor_data_value = Gauge(
    "iot_sensor_data_value",
    "Last value received from sensor by data type",
    ["data_type"]
)

sensor_temperature_value = Gauge(
    "iot_sensor_temperature_value",
    "Last temperature value received from sensors"
)

sensor_humidity_value = Gauge(
    "iot_sensor_humidity_value",
    "Last humidity value received from sensors"
)

sensor_pressure_value = Gauge(
    "iot_sensor_pressure_value",
    "Last pressure value received from sensors"
)

sensor_light_value = Gauge(
    "iot_sensor_light_value",
    "Last light value received from sensors"
)
