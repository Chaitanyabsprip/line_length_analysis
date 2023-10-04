from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    should_recurse: bool
    display_method: str
    file_paths: list[str]
