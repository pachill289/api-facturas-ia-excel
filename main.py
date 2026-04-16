from fastapi import FastAPI, Request
import fitz  # PyMuPDF

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API PDF Tigo funcionando"}

@app.post("/extract-text")
async def extract_text(request: Request):
    # Leer el body crudo como bytes
    pdf_bytes = await request.body()
    
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    text = ""
    for page in doc:
        text += page.get_text()
    
    return {"text": text}