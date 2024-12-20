from typing import Dict, Any
import json
import requests


class BaseAgent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        self.ollama_base_url = "http://localhost:11434/v1"

    async def run(self, messages: list) -> Dict[str, Any]:
        """Default run method to be overridden by child classes"""
        raise NotImplementedError("Subclasses must implement run()")

    def _query_ollama(self, prompt: str) -> str:
        """Query Ollama model with the given prompt"""
        try:
            # Prepare the payload
            payload = {
                "model": "llama3.2",
                "messages": [
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.7,
                "max_tokens": 2000,
            }
            # Send POST request to the Ollama API
            response = requests.post(
                f"{self.ollama_base_url}/chat/completions",
                json=payload,
            )
            response.raise_for_status()  # Raise an error for bad HTTP responses
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception as e:
            print(f"Error querying Ollama: {str(e)}")
            raise

    def _parse_json_safely(self, text: str) -> Dict[str, Any]:
        """Safely parse JSON from text, handling potential errors"""
        try:
            # Try to find JSON-like content between curly braces
            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1:
                json_str = text[start : end + 1]
                return json.loads(json_str)
            return {"error": "No JSON content found"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON content"}