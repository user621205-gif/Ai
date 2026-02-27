from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Replace with actual Claude AI integration
class ClaudeAI:
    @staticmethod
    def analyze(text: str) -> dict:
        # Dummy implementation for analysis
        return {"scam_detected": "no", "confidence": 0.0}

@app.post("/analyze")
async def analyze_text(text: str):
    result = ClaudeAI.analyze(text)
    return JSONResponse(content=result)