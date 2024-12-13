from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    AWS_NAME: str
    AWS_SECRET: str
    AWS_REGION: str

    @computed_field
    @property
    def AWS_CREDENTIALS(self) -> dict:
        return {'name0': self.AWS_NAME, 'secret': self.AWS_SECRET, 'region': self.AWS_REGION}

settings = Settings()