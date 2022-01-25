from pydantic import BaseSettings


class Config(BaseSettings):
    # Your Config Here
    def __init__(self, **value: dict):
        super().__init__(**value)
        pass

    class Config:
        extra = "ignore"