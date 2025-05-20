import httpx
from config import Config

async def generate_ai_response(prompt: str, model: str = "deepseek/deepseek-chat-v3-0324:free") -> str:
    headers = {
        "Authorization": f"Bearer {Config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Ты дружелюбный AI-ассистент..."},
            {"role": "user", "content": prompt}
        ]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
    
    return response.json()["choices"][0]["message"]["content"]