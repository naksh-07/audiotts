import os
import sys

# Settings folder access
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from settings.config import INPUT_CLEAN_TEXT, SSML_OUTPUT_DIR, IGNORE_PREFIXES
from settings.emotions import EMOTIONS
from settings.casting import CHARACTER_VOICES
from templates.templates import voice_block

MAX_VOICES_PER_CHUNK = 30 

def generate_ssml(input_path=INPUT_CLEAN_TEXT, chapter_name="chapter_audio"):
    
    if not os.path.exists(input_path):
        print(f"❌ Error: File nahi mili -> {input_path}")
        return []

    print(f"🎭 Loading Cast... ({len(CHARACTER_VOICES)} Characters loaded)")
    
    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()

    blocks = []
    
    # Defaults
    current_emotion = "NEUTRAL"
    current_voice = CHARACTER_VOICES["NARRATOR"]

    for raw in lines:
        line = raw.strip()

        # 1. Empty lines skip karo
        if not line:
            continue

        # 2. Headings ignore karo
        if line.startswith(IGNORE_PREFIXES):
            continue

        # ====================================================
        # 🛑 TAG PARSING LOGIC (STRICT)
        # ====================================================

        # CASE A: Agar line '[' se shuru hoti hai (Emotion ya Narrator change)
        if line.startswith("[") and "]" in line:
            tag_content = line.split("]")[0].replace("[", "").strip() # [FEAR] -> FEAR
            
            # Check 1: Kya ye [CHAR : EMOTION] format hai? (e.g. [NARRATOR : SAD])
            if ":" in tag_content:
                parts = tag_content.split(":")
                char_key = parts[0].strip().upper()
                emo_key = parts[1].strip().upper()
                
                # Voice aur Emotion dono update karo
                if char_key in CHARACTER_VOICES:
                    current_voice = CHARACTER_VOICES[char_key]
                if emo_key in EMOTIONS:
                    current_emotion = emo_key
            
            # Check 2: Kya ye bas Emotion hai? (e.g. [FEAR])
            elif tag_content in EMOTIONS:
                current_emotion = tag_content
            
            # 🛑 IMPORTANT: Continue kar do taaki ye line audio mein na jaye
            continue 

        # CASE B: Agar line 'DIALOGUE' se shuru hoti hai
        if line.startswith("DIALOGUE"):
            try:
                # Character name nikaalo -> DIALOGUE (BILBO): -> BILBO
                if "(" in line and ")" in line:
                    char_name = line.split("(")[1].split(")")[0].strip().upper()
                    current_voice = CHARACTER_VOICES.get(char_name, CHARACTER_VOICES["NARRATOR"])
                
                # Agar usi line mein text bhi hai (e.g. DIALOGUE (BILBO): Hello)
                # To text ko alag karo
                if ":" in line:
                    possible_text = line.split(":", 1)[1].strip()
                    # Agar colon ke baad text hai, tabhi add karo.
                    # Agar text khali hai (jaise user input mein tha), to skip karo.
                    if possible_text:
                        e = EMOTIONS.get(current_emotion, EMOTIONS["NEUTRAL"])
                        blocks.append(voice_block(
                            current_voice, e["style"], e["rate"], e["pitch"], e["volume"], possible_text
                        ))
            except:
                pass
            
            # 🛑 IMPORTANT: Continue taaki 'DIALOGUE (..)' audio me na bole
            continue

        # ====================================================
        # 🗣️ NORMAL TEXT (Jo bach gaya, wo dialogue hai)
        # ====================================================
        
        # Bas wahi lines lo jo tags nahi hain
        e = EMOTIONS.get(current_emotion, EMOTIONS["NEUTRAL"])
        blocks.append(voice_block(
            current_voice, e["style"], e["rate"], e["pitch"], e["volume"], line
        ))

    # --- XML File Writing (Same as before) ---
    chunks = [blocks[i:i+MAX_VOICES_PER_CHUNK] for i in range(0, len(blocks), MAX_VOICES_PER_CHUNK)]
    os.makedirs(SSML_OUTPUT_DIR, exist_ok=True)
    generated_files = []

    for idx, chunk in enumerate(chunks, 1):
        full_xml = (
            '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="hi-IN">\n'
            + "\n".join(chunk) + 
            '\n</speak>'
        )
        outfile = os.path.join(SSML_OUTPUT_DIR, f"{chapter_name}_part{idx}.xml")
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(full_xml)
        generated_files.append(outfile)
    
    print(f"✅ SSML Generated: {len(generated_files)} parts ready.")
    return generated_files