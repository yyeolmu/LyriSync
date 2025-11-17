import os, warnings

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"  # pygame 인사메시지 숨기기
warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API",
    category=UserWarning,
)

import time, sys, pygame
from song_model import load_song
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(path, new_width=50):
    img = Image.open(path).convert("L")  # 그레이스케일
    w, h = img.size
    aspect_ratio = h / w
    new_height = int(aspect_ratio * new_width * 0.5)  # 세로 보정
    img = img.resize((new_width, new_height))

    pixels = img.getdata()
    chars = "".join(ASCII_CHARS[p * (len(ASCII_CHARS)-1) // 255] for p in pixels)

    lines = [
        chars[i:i+new_width]
        for i in range(0, len(chars), new_width)
    ]
    return "\n".join(lines)

song = load_song("songinfo/사랑하게 될 거야.json")
ascii_art = image_to_ascii("cover/" + song.cover_file)

sec_per_beat = 60 / song.bpm

pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("./songs/" + song.audio_file)
pygame.mixer.music.play(start=song.start_offset - song.fadein)

if song.fadein > 0 :
    time.sleep(song.fadein)

for note in song.notes:
    print(note.ch, end = '', flush=True)
    if note.beat > 0 :
        time.sleep(note.beat * sec_per_beat)

print(ascii_art)
print(f"{song.artist} - {song.title}")
        
if song.fadeout > 0 :
    time.sleep(song.fadeout)
    
pygame.mixer.music.stop()