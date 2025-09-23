from fastapi import FastAPI
import uvicorn
import sys 
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline

text:str = "What is text summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response(content="Training successful!!", media_type="text/plain")
    except Exception as e:
        return Response(content=f"Error Occurred! {e}", media_type="text/plain")
    
@app.get("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e 
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)