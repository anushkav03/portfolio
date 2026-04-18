from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

## ----------------- HTML Routes ----------------- ##
@app.get("/")
def home(request: Request):
    #return f"<h1>Hello world<h1>"
    return templates.TemplateResponse(
        request,
        "home.html"
    )

@app.get("/projects")
def projects(request: Request):
    return templates.TemplateResponse(
        request,
        "projects.html"
    )