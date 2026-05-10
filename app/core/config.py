from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    APP_NAME: str
    DEBUG: bool
    DATABASE_URL: str
    
settings = Settings()