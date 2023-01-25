from datetime import datetime

from pydantic import Field

from app.model.common import Model, OID


class SampleModel(Model):
    """Sample Model"""

    id: OID = Field(..., description="Sample id", alias="_id")
    name: str = Field(..., description="Sample name", example="example name")
    age: int = Field(..., description="Sample age")
    created_at: datetime = Field(..., description="created at")


class SampleCreateData(Model):
    """Sample Update form"""

    name: str = Field(None, example="hyulee", description="Sample name")
    age: int = Field(None, description="Sample age")


class SampleUpdateData(Model):
    """Sample Update form"""

    name: str = Field(None, example="hyulee", description="Sample name")
    age: int = Field(None, description="Sample age")


class SampleModelData(Model):
    """Sample Model Data"""

    name: str = Field(None, description="Sample name", example="example name")
    age: int = Field(None, description="Sample age")
    created_at: datetime = Field(None, description="created at")


class SampleSuccessResponse(Model):
    """Sample uid response"""

    id: OID = Field(..., description="Sample id", alias="_id")


class SampleUIDResponse(Model):
    """Sample uid response"""

    id: OID = Field(..., description="Sample id", alias="_id")
