from fastapi import FastAPI

app = FastAPI(title="Agentic Stack API")

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Agentic Stack Template"}
