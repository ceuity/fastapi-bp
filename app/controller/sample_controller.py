from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path

from app.core.containers import Container
from app.model.common import SuccessResponse
from app.model.model_sample import SampleModel, SampleUIDResponse, SampleUpdateData, SampleCreateData
from app.service.sample_service import SampleService

router = APIRouter(prefix="/api/v1/samples", tags=["Sample 관련 API"])


@router.get("/{sample_id}", response_model=SampleModel)
@inject
async def get_sample(
    sample_id: str = Path(..., min_length=24, max_length=24),
    sample_service: SampleService = Depends(Provide[Container.sample_service]),
):
    try:
        sample = await sample_service.get_sample(sample_id)

        return sample
    except Exception as e:
        raise e


@router.get("", response_model=list[SampleModel])
@inject
async def get_samples(
    sample_service: SampleService = Depends(Provide[Container.sample_service]),
):
    try:
        samples = await sample_service.get_samples()

        return samples
    except Exception as e:
        raise e


@router.post("", response_model=SampleUIDResponse)
@inject
async def create_sample(
    sample: SampleCreateData,
    sample_service: SampleService = Depends(Provide[Container.sample_service]),
):
    try:
        id = await sample_service.create_sample(sample)

        return SampleUIDResponse(id=id)
    except Exception as e:
        raise e


@router.put("/{sample_id}", response_model=SuccessResponse)
@inject
async def update_sample(
    sample_id: str = Path(..., min_length=24, max_length=24),
    data: SampleUpdateData = None,
    sample_service: SampleService = Depends(Provide[Container.sample_service]),
):
    try:
        await sample_service.update_sample(sample_id, data)

        return SuccessResponse()
    except Exception as e:
        raise e


@router.delete("/{sample_id}", response_model=SuccessResponse)
@inject
async def delete_sample(
    sample_id: str = Path(..., min_length=24, max_length=24),
    sample_service: SampleService = Depends(Provide[Container.sample_service]),
):
    try:
        await sample_service.delete_sample(sample_id)

        return SuccessResponse()
    except Exception as e:
        raise e
