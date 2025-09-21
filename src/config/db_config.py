from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_DRIVER: str
    DB_HOST: str
    DB_PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def connection_string(self):
        return (f"{self.DB_DRIVER}+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}")
    @property
    def connection_string_sync(self):
        return (f"{self.DB_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}")

db_config = DBConfig()  # type: ignore
