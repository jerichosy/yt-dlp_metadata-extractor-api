import yt_dlp
from fastapi import FastAPI

app = FastAPI()


@app.get("/extract")
def extract(url: str):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return ydl.sanitize_info(info_dict)
