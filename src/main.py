import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import config
from api import urls

app = FastAPI(
    title="Stock Searcher API",
    description="This is api for stock searcher",
    version=config.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(urls.router)


@app.get("/", tags=["root"])
async def root():
    return {"name": "stocker_api", "redis": True, "version": config.VERSION}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, debug=True, reload=True)
