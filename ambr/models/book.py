from typing import List

from pydantic import BaseModel, Field, field_validator

__all__ = (
    "BookVolume",
    "BookDetail",
    "Book",
)


class BookVolume(BaseModel):
    id: int
    name: str
    description: str
    story_id: int = Field(alias="storyId")


class BookDetail(BaseModel):
    id: int
    name: str
    rarity: int = Field(alias="rank")
    icon: str
    volumes: List[BookVolume] = Field(alias="volume")

    @field_validator("icon", mode="before")
    def _convert_icon_url(cls, v: str) -> str:
        return f"https://api.ambr.top/assets/UI/{v}.png"


class Book(BaseModel):
    """
    Represents a book.

    Attributes
    ----------
    id: :class:`int`
        The book's ID.
    name: :class:`str`
        The book's name.
    rarity: :class:`int`
        The book's rarity.
    icon: :class:`str`
        The book's icon.
    route: :class:`str`
        The book's route.
    """

    id: int
    name: str
    rarity: int = Field(alias="rank")
    icon: str
    route: str

    @field_validator("icon", mode="before")
    def _convert_icon_url(cls, v: str) -> str:
        return f"https://api.ambr.top/assets/UI/{v}.png"
