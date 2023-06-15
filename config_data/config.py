from dataclasses import dataclass
from environs import Env


@dataclass
class Tg_bot:
    token: str


@dataclass
class Config:
    tg_bot: Tg_bot


def get_config_data(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)
    config: Config = Config(tg_bot=Tg_bot(token=env("TOKEN")))
    return config

