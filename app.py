from fastapi import FastAPI  # type: ignore
from dapr.ext.fastapi import DaprActor  # type: ignore
from service.proxy_actor import ProxyActor
from service.cookie_actor import CookieActor
import uvicorn


app = FastAPI(title=f'spider-actor-service')

# Add Dapr Actor Extension
actor = DaprActor(app)


@app.on_event("startup")
async def startup_event():
    # Register DemoActor
    await actor.register_actor(ProxyActor)
    await actor.register_actor(CookieActor)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
