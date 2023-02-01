from fastapi import APIRouter

from datetime import datetime

from typing import Union

router = APIRouter()

@router.get("/scrap/",tags=["scrap"])
async def collect_absitem(
    start_date:Union[datetime,None]=None,
    end_date:Union[datetime,None]=None,
) -> None:

    print("import function position")

    start = datetime.now()
    print(f'start=========={start}')

    print("function position")
    
    end = datetime.now()
    print(f'end============{end}')
    return {"ok":"ok"}