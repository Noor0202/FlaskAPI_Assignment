from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import requests
from transformers import pipeline
import uuid

app = FastAPI()

summ_list = {}

t5_model = pipeline("summarization", model="t5-base")

class URLRequest(BaseModel):
    url: HttpUrl

@app.post("/summarize")
async def summarize_large_document(request: URLRequest):
    try:
        with requests.get(request.url, stream=True) as response:
            response.raise_for_status()
            content = ''
            for chunk in response.iter_content(chunk_size=1024):
                content += chunk.decode('utf-8')
                if len(content) > 2000:
                    content = content[:2000]
                    break

        summary = t5_model(content, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

        summary_id = str(uuid.uuid4())
        summ_list[summary_id] = summary

        return {"id": summary_id}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail="Error - " + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Errpr - " + str(e))

@app.get("/summary/{id}")
async def get_summary(id: str):
    if id in summ_list:
        return {"summary": summ_list[id]}
    else:
        raise HTTPException(status_code=404, detail="not found")