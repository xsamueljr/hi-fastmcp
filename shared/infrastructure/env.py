from enum import Enum
import os

from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict

load_dotenv()


class AppEnvType(Enum):
    PRODUCTION = "production"
    TEST = "test"


class EnvSchema(BaseModel):
    APP_ENV: AppEnvType = AppEnvType.TEST

    model_config = ConfigDict(frozen=True)


ENV = EnvSchema(**os.environ) # type: ignore (pydantic will handle parsing)
