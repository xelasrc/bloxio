from fastapi import FastAPI

app = FastAPI(title="Bloxio API")

@app.get("/health")
def health():
    return {"status": "ok"}
