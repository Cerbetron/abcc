from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import pandas as pd

LOG_FILE = os.path.join('logs', 'agent_usage_log.csv')
TEMPLATE_FILE = os.path.join('templates', 'report.html')

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
async def get_report():
    if os.path.exists(TEMPLATE_FILE):
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    return HTMLResponse(content="<h1>Template not found</h1>", status_code=404)


@app.get("/log.csv")
async def get_log_file():
    if os.path.exists(LOG_FILE):
        return FileResponse(LOG_FILE, media_type="text/csv", filename="agent_usage_log.csv")
    return {"error": "Log file not found."}