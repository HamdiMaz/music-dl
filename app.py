import uvicorn
from downloader import download_audio
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def process_url(request: Request):
    """
    Accept a URL and pass it to a function for processing.
    
    Parameters:
    request (Request): FastAPI request object containing the URL.
    
    Returns:
    dict: A JSON response with the processing result.
    """
    data = await request.json()
    url = data.get("url")
    download_audio(url)
    
    # return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
