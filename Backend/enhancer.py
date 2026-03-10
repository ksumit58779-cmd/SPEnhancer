from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


SYSTEM_PROMPTS = {
    "normal": """You are a prompt enhancement expert. 
Take the user's basic prompt and make it clearer, more specific, and better structured.
Keep it simple and natural. Just improve the wording and add clarity.
Return ONLY the enhanced prompt, nothing else. No explanations, no labels.""",

    "pro": """You are an expert prompt engineer.
Transform the user's prompt into a highly optimized, detailed, and structured prompt.
Add context, specify tone, format, and expected output style.
Use clear sections if needed. Make it significantly more powerful than the original.
Return ONLY the enhanced prompt, nothing else. No explanations, no labels.""",

    "extremely_pro": """You are a world-class prompt engineering specialist.
Transform the user's prompt into an extremely powerful, professional-grade prompt.
Include: clear role/persona, detailed context, specific constraints, output format instructions,
tone guidance, examples if helpful, and chain-of-thought instructions.
Make it dramatically better than the original — something a professional would use.
Return ONLY the enhanced prompt, nothing else. No explanations, no labels."""
}


def enhance_prompt(user_prompt: str, mode: str = "normal") -> dict:
    """
    Enhance a user prompt using Gemini AI.

    Args:
        user_prompt: The original prompt from the user
        mode: Enhancement level — 'normal', 'pro', or 'extremely_pro'

    Returns:
        dict with 'success', 'enhanced_prompt', and 'error' keys
    """

    # Validate mode
    if mode not in SYSTEM_PROMPTS:
        mode = "normal"

    # Guard: empty prompt
    if not user_prompt or not user_prompt.strip():
        return {
            "success": False,
            "enhanced_prompt": None,
            "error": "Prompt cannot be empty."
        }

    try:
        system = SYSTEM_PROMPTS[mode]
        full_prompt = f"{system}\n\nUser Prompt to enhance:\n{user_prompt.strip()}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        enhanced = response.text.strip()

        return {
            "success": True,
            "enhanced_prompt": enhanced,
            "error": None
        }

    except Exception as e:
        return {
            "success": False,
            "enhanced_prompt": None,
            "error": str(e)
        }