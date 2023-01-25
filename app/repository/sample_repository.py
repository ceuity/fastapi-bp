import abc
from datetime import datetime

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.collection import Collection


class SampleRepository(metaclass=abc.ABCMeta):
    """sample repository interface"""

    @abc.abstractmethod
    async def get_sample(self, sample_id: str) -> dict:
        """Get sample by id"""

        pass

    @abc.abstractmethod
    async def get_samples(self) -> list[dict]:
        """Get samples"""

        pass

    @abc.abstractmethod
    async def create_sample(self, sample: dict) -> ObjectId:
        """Create sample"""

        pass

    @abc.abstractmethod
    async def update_sample(self, sample: dict) -> int:
        """Update sample"""

        pass

    @abc.abstractmethod
    async def delete_sample(self, sample_id: ObjectId) -> int:
        """Delete sample"""

        pass


class MongoSampleRepo(SampleRepository):
    """Mongo sample repository"""

    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        """MongoDB Collection Object Injection"""

        self.sample: Collection = db.get_collection("sample")

    async def get_sample(self, sample_id: str) -> dict:
        """Find sample by id"""

        sample = await self.sample.find_one({"_id": ObjectId(sample_id)})

        return sample

    async def get_samples(self) -> list[dict]:
        """Find samples"""

        samples = self.sample.find()

        return [sample async for sample in samples]

    async def create_sample(self, data: dict) -> ObjectId:
        """Create sample"""

        data["created_at"] = datetime.now()
        result = await self.sample.insert_one(data)

        return result.inserted_id

    async def update_sample(self, sample_id: str, data: dict) -> int:
        """Update sample"""

        result = await self.sample.update_one({"_id": ObjectId(sample_id)}, {"$set": data})

        return result.modified_count

    async def delete_sample(self, sample_id: str) -> int:
        """Delete sample"""

        result = await self.sample.delete_one({"_id": ObjectId(sample_id)})

        return result.deleted_count
