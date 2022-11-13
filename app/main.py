from fastapi import FastAPI
from .events.register import register_routers
from .config.env_manager import get_settings

EnvManager = get_settings()

app = FastAPI(title="IOET MVP Clients App",
              root_path=EnvManager.STG_NAME,
              openapi_url=f'{EnvManager.STG_NAME}/openapi.json',
              docs_url=f'{EnvManager.STG_NAME}/docs')

register_routers(app, 'app.routers')
