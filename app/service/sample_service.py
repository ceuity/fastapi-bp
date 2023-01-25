from bson import ObjectId

from app.model.model_sample import SampleModel, SampleModelData, SampleUpdateData, SampleCreateData
from app.repository.sample_repository import SampleRepository
from app.core.exceptions import ResourceNotFound


class SampleService:
    """Sample service"""

    def __init__(self, sample_repository: SampleRepository) -> None:
        self.sample_repository = sample_repository

    async def get_sample(self, sample_id: str) -> SampleModel:
        """Find sample by id"""

        sample = await self.sample_repository.get_sample(sample_id)
        if not sample:
            ResourceNotFound("Sample not found")

        return SampleModel(**sample)

    async def get_samples(self) -> list[SampleModel]:
        """Find samples"""

        samples = await self.sample_repository.get_samples()
        if not samples:
            ResourceNotFound("Samples not found")

        return [SampleModel(**sample) for sample in samples]

    async def create_sample(self, data: SampleCreateData) -> ObjectId:
        """Create sample"""

        sample = SampleModelData(**data.dict())

        return await self.sample_repository.create_sample(sample.dict())

    async def update_sample(self, sample_id: str, data: SampleUpdateData) -> int:
        """Update sample"""

        sample = SampleModelData(**data.dict(exclude_unset=True))

        return await self.sample_repository.update_sample(sample_id, sample.dict(exclude_unset=True))

    async def delete_sample(self, sample_id: str) -> int:
        """Delete sample"""

        return await self.sample_repository.delete_sample(sample_id)
