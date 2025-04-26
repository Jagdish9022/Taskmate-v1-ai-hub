from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat
from routes import chat, eod, task_generator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat")
app.include_router(chat.router, prefix="/api/chat")
app.include_router(eod.router, prefix="/api/eod")
app.include_router(task_generator.router, prefix="/api/task-generator")
