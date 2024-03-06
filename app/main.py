from fastapi import FastAPI

from app.routers import integrator_router

app = FastAPI(
    title='Request Integrator API',
    description='API to integrate requests from different sources.',
    version='0.1.0',
)


@app.get('/')
async def home():
    return {
        'message': 'Welcome to the request-integrator server!'
    }


# Routers
app.include_router(integrator_router)
