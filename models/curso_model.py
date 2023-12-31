from core.configs import settings

from sqlalchemy import Column, Integer, String

#tabela e modelo do banco 
class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
    descricao: str = Column(String(140))
