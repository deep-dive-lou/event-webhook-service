from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def recieve_webhook(request: Request):
    body = await request.json()
    print("Recevied Webhook:", body)
    return {'received': True}