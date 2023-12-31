from typing import Optional

from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int
    descricao: str

    class Config:
        orm_mode = True
