from fastapi import APIRouter

todo_router = APIRouter()

@todo_router.get("/test")
async def test_todo():
    return {"message": "Todo test endpoint is working!"}