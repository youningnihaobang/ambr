from __future__ import annotations

from pydantic import BaseModel, Field, field_validator

__all__ = ("Quest","QuestDetail")


class Quest(BaseModel):
    """
    Represents a quest.

    Attributes
    ----------
    id: :class:`int`
        The quest's ID.
    type: :class:`str`
        The quest's type.
    chapter_num: Optional[:class:`str`]
        The quest's chapter number.
    chapter_title: :class:`str`
        The quest's chapter title.
    chapter_icon: Optional[:class:`str`]
        The quest's chapter icon.
    chapter_image_title: :class:`str`
        The quest's chapter image title.
    route: :class:`str`
        The quest's route.
    chapter_count: :class:`int`
        The quest's chapter count.
    """

    id: int
    type: str | None
    chapter_num: str | None = Field(alias="chapterNum")
    chapter_title: str = Field(alias="chapterTitle")
    chapter_icon: str | None = Field(alias="chapterIcon")
    chapter_image_title: str | None = Field(alias="chapterImageTitle")
    route: str
    chapter_count: int = Field(alias="chapterCount")

    @field_validator("chapter_icon", mode="before")
    def _convert_icon_url(cls, v: str) -> str:
        return f"https://gi.yatta.moe/assets/UI/{v}.png"
class StoryInfo(BaseModel):
    """
    Represents a Story info.

    description: :class:`str`
    title: :class:`str`
    """
    title: str
    description: str
class StoryReward(BaseModel):
    """
    Represents a Story reward.

    count: :class:`int`
    icon: :class:`str`
    id: :class:`int`
    rank: :class:`int`
    type: :class:`str`

    """
    count:int
    icon:str
    id:int
    rank:int
    type:str

class StoryStory(BaseModel):
    """
    Represents a quest Story.

    id: :class:`int`
    isHidden: :class:`bool`
    stepDescription: :class:`str`
    taskData: :class:`str`
    title: :class:`str`
    """

    id:int
    isHidden:bool
    stepDescription:str
    taskData:str
    title:str
class QuestDetail(BaseModel):
    """
    Represents a quest Detail.
    info: :class:`Quest`
    storyList: :class:`list:QuestStory`
    """
    info:Quest
    storyList:dict[str,QuestStory]
class QuestStory(BaseModel):
    """
    Represents a quest Story.

    Attributes
    ----------
    id: :class:`int`
        The quest's ID.
    type: :class:`str`
        The quest's type.
    chapter_num: Optional[:class:`str`]
        The quest's chapter number.
    chapter_title: :class:`str`
        The quest's chapter title.
    chapter_icon: Optional[:class:`str`]
        The quest's chapter icon.
    chapter_image_title: :class:`str`
        The quest's chapter image title.
    route: :class:`str`
        The quest's route.
    chapter_count: :class:`int`
        The quest's chapter count.
    """

    id: int
    info:StoryInfo
    npcList:dict
    reward:StoryReward
    story:dict[str,StoryStory]
    suggestTrackMainQuestList:dict
