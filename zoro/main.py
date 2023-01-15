from fastapi import FastAPI
from starlette.responses import RedirectResponse
from .api.endpoints import badge

app = FastAPI()

app.include_router(badge.router)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")
