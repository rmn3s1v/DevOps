from datetime import datetime
from app.db.database import db
from app.models.data_models import SensorDataCreate


class DataService:

    @staticmethod
    def create_data(sensor_id: int, data:SensorDataCreate):
        count = db.sensor_data.count_documents({"sensor_id": sensor_id})
        new_id = count + 1

        data_dict = data.model_dump()
        data_dict = data.model_dump()
        data_dict["id"] = new_id
        data_dict["sensor_id"] = sensor_id
        data_dict["timestamp"] = datetime.now()

        db.sensor_data.insert_one(data_dict)
        return data_dict

    @staticmethod
    def get_sensor_data(sensor_id: int, limit: int = 100):
        cursor = (
            db.sensor_data
            .find({"sensor_id":sensor_id}, {"_id": 0})
            .sort("timestamp", -1)
            .limit(limit)
        )

        return list(cursor)

    @staticmethod
    def update_data(sensor_id: int, data_id: int, data):
        existing = db.sensor_data.find(
            {"sensor_id":sensor_id}, {"_id": 0}
        )

        if not existing:
            return None

        update_fields = {
            k: v for k, v in data.model_dump().items()
            if v is not None
        }

        db.sensor_data.update_one(
            {"sensor_id": sensor_id, "id": data_id},
            {"$set": update_fields}
        )

        return db.sensor_data.find_one(
            {"sensor_id": sensor_id, "id": data_id},
            {"_id": 0}
        )


    @staticmethod
    def delete_sensor_data(sensor_id: int, id : int):
        db.sensor_data.delete_one({"sensor_id": sensor_id, "id": id})
        return True
