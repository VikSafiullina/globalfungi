from pydantic import BaseModel, UUID4
from typing import Optional
from uuid import UUID

class CreateSampleRequest(BaseModel):
    original_id: int
    paper_id: UUID
    chemical_data_id: Optional[UUID]
    env_data_id: Optional[UUID]
    sampling_data_id: Optional[UUID]
    sequencing_data_id: Optional[UUID]
    latitude: float
    longitude: float
    sample_info: str

    class Config:
        arbitrary_types_allowed = True


class GetSampleByIdRequest(BaseModel):
    sample_id: UUID4
