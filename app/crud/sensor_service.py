from datetime import datetime
from app.db.database import db
from app.models.sensor_models import SensorCreate, SensorUpdate


class SensorService:

    @staticmethod
    def create_sensor(sensor: SensorCreate):
        count = db.sensors.count_documents({})
        new_id = count + 1

        sensor_dict = sensor.model_dump()
        sensor_dict["ip"] = str(sensor_dict["ip"])
        sensor_dict.update({
            "id": new_id,
            "created_at": datetime.now()
        })

        db.sensors.insert_one(sensor_dict)
        return sensor_dict

    @staticmethod
    def get_all_sensors():
        return list(db.sensors.find({}, {"_id":0}))

    @staticmethod
    def get_sensor(sensor_id: int):
        return db.sensors.find_one({"id": sensor_id}, {"_id": 0})

    @staticmethod
    def update_sensor(sensor_id: int, sensor: SensorUpdate):

        update_data = {
            k: v for k, v in sensor.model_dump().items()
            if v is not None
        }

        if "ip" in update_data:
            update_data["ip"] = str(update_data["ip"])

        db.sensors.update_one(
            {"id": sensor_id},
            {"$set": update_data}
        )

        return db.sensors.find_one({"id": sensor_id}, {"_id": 0})

    @staticmethod
    def delete_sensor(sensor_id: int):
        db.sensors.delete_one({"id": sensor_id})
        db.sensor_data.delete_many({"sensor_id": sensor_id})
        return True
