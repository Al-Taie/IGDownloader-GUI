from dataclasses import dataclass
from typing import List

from data.models.media import Media


@dataclass
class Post:
    username: str
    caption: str
    short_code: str
    is_video: bool
    is_slide: bool
    item: Media
    items: List[Media]

    @property
    def count(self) -> int:
        return len(self.items)
