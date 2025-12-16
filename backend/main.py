from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.training import router as train_router
from .api.inference import router as infer_router

app = FastAPI(title="LIULIAN Backend")

# Enable CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(train_router, prefix="/api")
app.include_router(infer_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "LIULIAN Backend API",
        "docs": "/docs",
        "endpoints": {
            "training": "/api/train/{plugin_name}",
            "prediction": "/api/predict/{plugin_name}",
            "visualization": "/api/visualize/{plugin_name}"
        }
    }
