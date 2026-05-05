# app/schemas/gist.py
from pydantic import BaseModel
from typing import List, Optional

class GistResponse(BaseModel):
    id: str
    description: Optional[str]
    url: str
    files: List[str]