from dataclasses import dataclass
from typing import List

@dataclass
class Team:
    name: str
    description: str
    members: List[str]
