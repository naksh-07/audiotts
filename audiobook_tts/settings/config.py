import os

# ==========================================
# 🔐 1. AZURE CREDENTIALS (SECRET)
# ==========================================
# Bhai, apni key yahan paste kar dena. 
# Kisi GitHub repo pe upload mat karna ye file!

AZURE_KEY = "" 
AZURE_REGION = "northcentralus"  # Ya 'centralindia' jo tera region ho


# ==========================================
# 📂 2. SMART PATH SYSTEM (AUTO-DETECT)
# ==========================================
# Ye logic automatically dhoond lega ki tera project computer me kahan rakha hai.
# 'settings' folder se ek step peeche (..) jaake 'root' folder milega.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input File (Yahan apni book ka naam change kar sakta hai)
INPUT_FILENAME = "book_final.txt"
INPUT_CLEAN_TEXT = os.path.join(BASE_DIR, "input", INPUT_FILENAME)

# Output Folders (Agar nahi bane honge, to code khud bana dega)
SSML_OUTPUT_DIR = os.path.join(BASE_DIR, "ssml_output")
AUDIO_OUTPUT_DIR = os.path.join(BASE_DIR, "audio")


# ==========================================
# 🎧 3. AUDIO QUALITY
# ==========================================
# Options: 
# - Audio48Khz192KBitRateMonoMp3 (Best Balance)
# - Audio24Khz160KBitRateMonoMp3 (Faster)

AUDIO_QUALITY_STRING = "Audio48Khz192KBitRateMonoMp3"
OUTPUT_FORMAT = "mp3"


# ==========================================
# 🧹 4. CLEANING RULES
# ==========================================
# In prefixes wali lines ko hum ignore karenge.
# Text file me notes likhne ke kaam aayega.

IGNORE_PREFIXES = (
    "#", "##", "###",       # Markdown Headings
    "===", "---", "***",    # Separators
    "📜", "🎭", "🎧",       # Emojis (Decoration)
    "//", "Note:",          # Comments
    "END_OF_CHAPTER"
)


# ==========================================
# ⚙️ 5. SYSTEM SETTINGS
# ==========================================

# Ek baar mein kitne dialogues Azure ko bhejne hain?
# Jyada bada number = Azure Timeout ka darr.
# 30 is safe sweet spot.
MAX_VOICES_PER_CHUNK = 30 

# Debug Mode: Agar script fat rahi ho to ise True kar dena
DEBUG_MODE = True