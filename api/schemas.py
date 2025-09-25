from pydantic import BaseModel

class PersonCreate(BaseModel):
    name: str
    title: str | None = None
    company: str | None = None
    location: str | None = None
    linkedin_url: str | None = None
    tags: str | None = None
    hotness: int | None = 2
    fit: int | None = 2

class TouchCreate(BaseModel):
    person_id: int
    channel: str | None = None
    time: str | None = None
    note: str | None = None
    outcome: str | None = None
    next_time: str | None = None
