from fastapi import FASTAPI
from routers.webhook import router as webhook_router
app.include_router(webhook_router)

app = FASTAPI()

@app.get("/")
def root():
    return {"status": "ok"}