from dataclasses import dataclass
from datetime import datetime

from infrastructure.database.models.base import BaseModel


@dataclass
class UsersModel(BaseModel):
    id: int
    user_id: int
    created: datetime
    tz_region: str | None
    tz_offset: str | None
    longitude: float | None
    latitude: float | None
    language: str
    is_alive: bool
    is_blocked: bool
    is_admin: bool
