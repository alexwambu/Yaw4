from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import video_pipeline
import uvicorn
import os

app = FastAPI()

# Enable CORS for frontend later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict to your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Video Creator API is running!"}

@app.post("/generate")
async def generate(script: str = Form(...), file: UploadFile = None):
    input_path = None
    if file:
        input_path = f"temp_{file.filename}"
        with open(input_path, "wb") as f:
            f.write(await file.read())

    output_path = video_pipeline.generate_movie(script, input_path)

    # Cleanup uploaded file
    if input_path and os.path.exists(input_path):
        os.remove(input_path)

    return {"output_file": output_path}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
