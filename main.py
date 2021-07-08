from fastapi import FastAPI

app = FastAPI()

class Token:
    def __init__(self, access_token: str, token_type: str):
         self.access_token = access_token
         self.token_type = token_type

@app.get("/")
async def root():
    return Token(access_token="access", token_type="token")
