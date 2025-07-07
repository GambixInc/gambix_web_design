from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI(title="Gambix Website", description="Gambix IT Services Website")

# Mount static files
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.get("/services")
async def read_services():
    return FileResponse("services.html")

@app.get("/tai")
async def read_tai():
    return FileResponse("tai.html")

@app.get("/team")
async def read_team():
    return FileResponse("team.html")

@app.get("/contact")
async def read_contact():
    return FileResponse("contact.html")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 