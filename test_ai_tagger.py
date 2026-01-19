from google import genai
from google.genai import types

# ==========================================
# 🔑 APNI KEY YAHAN DAAL
# ==========================================
MY_API_KEY = ""

SYSTEM_PROMPT = """
You are an expert Audiobook Script Formatter.
Convert the input Raw Hindi Story Text into a specific tagged format for TTS.

RULES:
1. Detect who is speaking.
2. Detect the emotion [NEUTRAL, SAD, ANGRY, FEAR, WHISPER, SHOUT, HAPPY, CASUAL, INTENSE, HUMOR].
3. Format Dialogue:
   DIALOGUE (CHARACTER_NAME):
   [EMOTION]
   Hindi dialogue text...
4. Format Narration:
   [NARRATOR : EMOTION]
   Hindi narration text...
5. Keep names in English (BILBO, GANDALF, THORIN).
"""

raw_text_sample = """
दरवाजे पर एक जोर की दस्तक हुई। "कौन है वहां?" बिल्बो ने डरते हुए पूछा। 
अचानक एक भारी आवाज आई, "मैं हूँ, थोरिन! दरवाजा खोलो वरना मैं तोड़ दूंगा!" 
"""

def run_test():
    print("🤖 AI Director (Gemini Stable) soch raha hai...")

    try:
        client = genai.Client(api_key=MY_API_KEY)

        # 👇 CHANGE: '2.0' hata diya, 'latest' stable wala use kar rahe hain
        model_name = "gemini-flash-latest" 

        response = client.models.generate_content(
            model=model_name,
            contents=raw_text_sample,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7
            )
        )

        print(f"\n-------- 🚀 AI OUTPUT ({model_name}) 🚀 --------")
        print(response.text)
        print("------------------------------------------")

    except Exception as e:
        print(f"\n❌ Abhi bhi error hai: {e}")
        print("\n💡 Bhai agar ye bhi na chale, to neeche wala 'Plan B (Groq)' try kar.")

if __name__ == "__main__":
    run_test()