from fastapi import FastAPI

app = FastAPI(
    title="OpenVision API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "application": "OpenVision",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }