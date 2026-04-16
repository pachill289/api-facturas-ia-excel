from fastapi import FastAPI, UploadFile, File
import fitz  # PyMuPDF

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API PDF Tigo funcionando"}

@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    content = await file.read()

    doc = fitz.open(stream=content, filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    return {
        "text": text
    }