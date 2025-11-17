from dataclasses import dataclass
from typing import List
import json

@dataclass
class Note:
    ch: str
    beat: float
    
@dataclass
class Song:
    title: str
    artist: str
    audio_file: str
    cover_file: str
    bpm: float
    fadein: float
    fadeout: float
    start_offset : float
    notes: List[Note]
    
def load_song(path: str) -> Song:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    notes = [Note(**n) for n in data["notes"]]
    
    return Song(
        title=data["title"],
        artist=data["artist"],
        audio_file=data["audio_file"],
        cover_file=data["cover_file"],
        bpm=data["bpm"],
        fadein=data["fadein"],
        fadeout=data["fadeout"],
        start_offset=data["start_offset"],
        notes=notes
    )
    