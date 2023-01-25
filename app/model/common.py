from datetime import datetime
from typing import TypeVar

from bson.errors import InvalidId
from bson.objectid import ObjectId
from pydantic import BaseModel, Field

T = TypeVar("T")


class SuccessResponse(BaseModel):
    """공통 응답 값"""

    message: str = "success"


class PagingResult(BaseModel):
    """페이징 객체"""

    data: list[T]
    metadata: dict


class OID(str):
    """Mongo db object id 커스텀 클래스"""

    @classmethod
    def __get_validators__(cls):
        """Validator"""

        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Validate class method"""

        try:
            return ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")

    @classmethod
    def generation_time(cls) -> datetime:
        """OID to datetime"""

        return cls.generation_time()


class Model(BaseModel):
    """Mongo db base model"""

    def dict(self, **kwargs):
        if "by_alias" not in kwargs:
            kwargs["by_alias"] = True

        return super().dict(**kwargs)

    class Config:

        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        use_enum_values = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: lambda oid: str(oid),
        }


class ObjectIdResponse(Model):
    """객체 생성 공통 응답 값"""

    id: OID = Field(..., alias="_id")

    class Config:
        schema_extra = {"example": {"_id": "60a1b2c3d4e5f6a7b8c9d0e1"}}
