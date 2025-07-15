from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, post

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(post.router)

@app.get("/health")
async def health_check():
    return {"status" : "healty"}
