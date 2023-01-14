from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/badge",
    tags=["badge"],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def get_badge():
    """
    Ito hakana ny badge rehetra
    """
    return fake_items_db


@router.get("/{item_id}")
async def get_badge(item_id: str):
    """
    Ito hakana ny badge par id
    """
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}
