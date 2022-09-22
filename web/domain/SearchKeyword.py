from typing import Optional

from pydantic import BaseModel


class SearchKeyword(BaseModel):
    transaction_id: Optional[str] = None
    client_id: Optional[str] = None
    ip: Optional[str] = None