from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENCRYPTION_ALGORITHM: str = "HS256"
    STG_NAME: str = ''
    ENV: str = 'DEV'

    class Config:
        env_file = './.env'
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return (
                init_settings,
                env_settings,
                file_secret_settings,
            )

    def get(self, key, default=None):
        return self.dict().get(key, default)

    def is_dev(self):
        return self.ENV.upper() == 'DEV'

    def is_secure_deployment(self):
        return self.ENV.upper() in ('STAGE', 'PROD')


@lru_cache
def get_settings() -> Settings:
    return Settings()


@lru_cache
def get_env_name() -> str:
    return get_settings().ENV
