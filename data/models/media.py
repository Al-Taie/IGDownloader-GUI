from dataclasses import dataclass


@dataclass
class Media:
    url: str
    is_video: bool
