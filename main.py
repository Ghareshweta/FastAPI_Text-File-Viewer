from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html") as f:
        return f.read()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Read file text
    contents = (await file.read()).decode("utf-8", errors="ignore")
    return JSONResponse({
        "filename": file.filename,
        "content": contents
    })
