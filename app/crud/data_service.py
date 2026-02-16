from datetime import datetime
from app.db.database import db
from app.models.data_models import SensorDataCreate


class DataService:

    @staticmethod
    def create_data(sensor_id: int, data:SensorDataCreate):
        count = db.sensor_data.count_documents({})
        new_id = count + 1

        data_dict = data.model_dump()
        data_dict.update({
            "id":new_id,
            "sensor_id": sensor_id,
            "timestamp": datetime.now()
        })

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
    def delete_sensor_data(sensor_id: int):
        db.sensor_data.delete_many({"sensor_id": sensor_id})
        return True

    @staticmethod
    def get_data_by_type(limit: int = 100):
        cursor = (
            db.sensor_data
            .find({}, {"_id": 0})
            .limit(limit)
        )
        return list(cursor)
