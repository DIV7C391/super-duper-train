from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
import tempfile

app = FastAPI()

@app.post("/extract")
async def extract_text(
    file: UploadFile = File(...)
):

    content = await file.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(content)

        temp_path = temp_file.name

    reader = PdfReader(temp_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return {
        "text": text
    }

try:

    reader = PdfReader(temp_path)

except Exception:

    raise HTTPException(
        status_code=400,
        detail="Invalid PDF"
    )
