from typing import List, Union, Optional
from pydantic import BaseModel


class Location(BaseModel):
    city: Union[str, List[str], None]
    country: Union[str, List[str], None]

    def get(self, key, default=None):
        return getattr(self, key, default)


class Experience(BaseModel):
    company_name: Union[str, List[str], None]
    position: Union[str, List[str], None]
    description: Union[str, List[str], None]
    skills_position: List[str]
    starts_at: Union[str, List[str], None]
    ends_at: Optional[Union[str, List[str], None]]
    location: Location

    class Config:
        extra = "allow"


class Profile(BaseModel):
    first_name: Union[str, List[str], None]
    surname: Union[str, List[str], None]
    skills: List[str]
    description: Union[str, List[str], None]
    location: Location
    experiences: List[Experience]
