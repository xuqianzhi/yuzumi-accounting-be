from fastapi import FastAPI
import httpx
from api.core.config import settings

app = FastAPI(title="Yuzumi Accounting Backend")

@app.get("/health")
def health_check():
    return {"status": "online", "service": "yuzumi-be"}

@app.get("/api/test-teller")
async def test_teller():
    async with httpx.AsyncClient(cert=settings.mtls_tuple) as client:
        response = await client.get(
            "https://api.teller.io/accounts",
            auth=(settings.TELLER_TOKEN, "")
        )
        return response.json()