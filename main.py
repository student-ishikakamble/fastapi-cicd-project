from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"CI/CD FastAPI project running 🚀"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "fastapi-cicd-project"
    }