import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

load_dotenv()

class s1Input(BaseModel):
    pw : str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/s1")
def s1(pw:s1Input):
    if pw.pw == os.getenv("stage1Answer"):
        return {"pass" : True, "key" : os.getenv("stage1Key")}
    else:
        return {"pass" : False}

@app.get("/s1")
def s1_hint():
    return {
        "hint" : "고급 암호화 표준 - 2^8 - ECB. 2 Times. I Give an 'Ciphertext' and 'key' to You. But. Not Korean. Find 'Key' and decrypt 'Ciphertext' to get 'Plaintext'."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0",port=6974, reload=True)