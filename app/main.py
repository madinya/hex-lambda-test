from fastapi import FastAPI
from .events.register import register_routers
from .config.env_manager import get_settings

EnvManager = get_settings()

app = FastAPI(title="Clients App",
              root_path=EnvManager.STG_NAME)

register_routers(app, 'app.routers')
