from prometheus_client import Counter

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
