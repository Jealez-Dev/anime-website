from . import appAnime2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

program = FastAPI()

class Anime(BaseModel):
    nombre_anime: str
    selectEP: Optional[str] = None

program.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@program.post("/BuscarAnime")
async def anime(anime: Anime):
    animeAPP = appAnime2.Anime()
    return {"listado": animeAPP.listado_anime(anime.nombre_anime)}

@program.post("/SeleccionAnime")
async def anime(anime: Anime):
    animeAPP = appAnime2.Anime()
    return {"Informacion": animeAPP.select_anime(anime.nombre_anime)}

@program.post("/SeleccionCap")
async def anime(anime: Anime):
    animeAPP = appAnime2.Anime()
    return {"Url": animeAPP.select_cap(anime.nombre_anime, anime.selectEP)}

app = program

