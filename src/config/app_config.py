from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    pass

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app_config = AppConfig()  # type: ignore
