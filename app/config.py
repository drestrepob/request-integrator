from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Bamboo

    # Zendesk

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
