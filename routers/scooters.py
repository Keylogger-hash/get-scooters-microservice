from fastapi import APIRouter



router = APIRouter(prefix="/v1")



@router.get("/scooters")
async def get_scooters():
    return "Scooters"


@router.get("/admin/scooters")
async def get_admin_scooters():
    return "Scooters admin"

