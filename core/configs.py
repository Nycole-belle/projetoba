from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
   
    #credencias geradas pelo render colque a do banco que vocês criaram "postgresql+asyncpg://usuario do banco:senha@postgres.render.com:5432/nome da base de dados"
    DB_URL: str = "postgresql+asyncpg://api_curso_user:NUn6AQWvvuAzYlGaEYaffhH6R4cTSWs9@postgres.render.com:5432/api_curso"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
