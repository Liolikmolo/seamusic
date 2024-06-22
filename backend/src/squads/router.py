from src.beats.services import BeatsRepository, BeatPacksRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatPackBase, SBeatPack, SBeatPackCreate
from src.auth.schemas import SUser
from src.beats.utils import save_audio, save_image
from src.config import settings
from src.auth.dependencies import get_current_user
from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse

beats = APIRouter(
    prefix = "/beats",
    tags = ["Squads"]
)

@beats.get("/my", summary="Beats by current user")
async def get_user_squads(user: SUser = Depends(get_current_user)):
    response = await BeatsRepository.find_all(user=user)
    return response

@beats.post("/add", summary="Add a file for new beat")
async def add_beats(file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    file_info = await save_audio(settings.media., file) if file else None

    data = {
        "title": file_info['title'],
        "file_path": file_info['file_path'],
        "user_id": user.id
    }
    
    response = await BeatsRepository.add_one(data)
    return response

@beats.post("/picture/{beats_id}", summary="Update a picture for ur beats")
async def update_pic_beats(beats_id: int, picture_file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    picture_path = await save_image(settings.media.BEATS_PICTURES, picture_file) if picture_file else None
    data = {
        "picture": picture_path
    }
    print(data)
    response = await BeatsRepository.edit_one(beats_id, data)
    return response

@beats.post("/release/{id}", summary="Realise a beat")
async def release_beats(id: int, beats_data: SBeatBase):    
    data = {
        "title": beats_data["title"],
        "description": beats_data["description"],
        "co_prod": beats_data["co_prod"],
        "prod_by": beats_data["prod_by"],
    }

    await BeatsRepository.edit_one(id, data)
    return data

@beats.put("/update/{id}", summary="Create new beats")
async def update_beats(id: int, beats_data: SBeatBase):
    data = {
        "title": beats_data.title,
        "description": beats_data.description,
    }
    
    await BeatsRepository.edit_one(id, data)
    return data

@beats.delete("/delete/{id}", summary="Create new beats")
async def delete_beats(id: int):
    return await BeatsRepository.delete(id=id)

@beats.get("/all", summary="Create new beats")
async def all_beats():
    return await BeatsRepository.find_all()

@beats.get("/get_one/{id}", summary="Create new beats")
async def get_one(id: int):
    return await BeatsRepository.find_one_by_id(id)
