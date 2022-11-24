from fastapi.routing import APIRouter

# from api.system.views import router as system_router
from api.auth.views import router as auth_router
from api.communication.views import router as communication_router
from api.contact.views import router as contact_router
from api.emotions.views import router as emotions_router
from api.example.views import router as example_router
from api.progress.views import router as progress_router


from api.note.routers import router as note_router


api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(
    communication_router, prefix="/communication", tags=["Communication"]
)
api_router.include_router(progress_router, prefix="/progress", tags=["Progress"])
api_router.include_router(emotions_router, prefix="/emotion", tags=["Emotion"])
api_router.include_router(contact_router, prefix="/contact", tags=["Contact"])
<<<<<<< HEAD

api_router.include_router(note_router)
=======
api_router.include_router(emergency_router, prefix="/emergency", tags=["Emergency"])
api_router.include_router(call_socket_router, prefix="/callwait", tags=["CallWait"])
api_router.include_router(call_router, prefix="/call", tags=["Call"])
>>>>>>> 47d8e4dddfe524e7168b7239e9dd3cb8a95bda37
