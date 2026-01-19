# settings/emotions.py

"""
MASTER EMOTION MAP FOR AUDIOBOOK TTS
------------------------------------
Ye dictionary 'ssml_generator.py' use karega.
Hum Azure ke 'styles' (angry, sad, etc.) ko 'prosody' (pitch, rate, volume)
ke saath mix karke naye emotions create kar rahe hain.
"""

EMOTIONS = {
    # ==========================================
    # 🟢 BASE / NARRATION (Kahaani Sunane ke liye)
    # ==========================================
    
    "NEUTRAL": {
        "style": "narration-professional",  # Agar voice support na kare, to ye ignore ho jayega
        "rate": "default", 
        "pitch": "default", 
        "volume": "default"
    },
    
    "NARRATION_SOFT": {
        "style": "calm",        # Thoda shant, rahasyamayi storytelling
        "rate": "-3%", 
        "pitch": "-1Hz", 
        "volume": "+5%"
    },

    "NARRATION_DRAMATIC": {
        "style": "serious",     # Movie trailer jaisa bhaari narration
        "rate": "-5%", 
        "pitch": "-2Hz", 
        "volume": "+10%"
    },

    # ==========================================
    # 🔴 INTENSE / ACTION (Ladai aur Gussa)
    # ==========================================

    "ANGRY": {
        "style": "angry", 
        "rate": "+10%",         # Gusse mein log tez bolte hain
        "pitch": "+2Hz", 
        "volume": "+20%"        # Thoda loud
    },

    "SHOUTING": {
        "style": "angry",       # Azure me direct 'shout' nahi h, to Angry + Volume boost
        "rate": "+15%", 
        "pitch": "+5Hz",        # Gala faad ke chillana
        "volume": "+40%"        # MAX VOLUME (Dhyaan se!)
    },

    "ACTION": {
        "style": "excited",     # Jaldi-jaldi bolna (Chalo bhaago!)
        "rate": "+20%", 
        "pitch": "+3Hz", 
        "volume": "+15%"
    },

    "INTENSE": {
        "style": "serious",     # "Main tumhe dhoond lunga..."
        "rate": "-10%",         # Slow aur scary
        "pitch": "-5Hz",        # Bhaari awaaz
        "volume": "+15%"
    },

    # ==========================================
    # 🔵 SAD / DARK (Dukh aur Dard)
    # ==========================================

    "SAD": {
        "style": "sad", 
        "rate": "-10%", 
        "pitch": "-2Hz", 
        "volume": "-5%"
    },

    "DESPAIR": {
        "style": "sad", 
        "rate": "-15%",         # Bahut slow (toot chuka insaan)
        "pitch": "-4Hz", 
        "volume": "-10%"
    },

    "CRYING": {
        "style": "sad",         # Rone jaisa effect
        "rate": "-20%", 
        "pitch": "+2Hz",        # Rote waqt awaaz thodi patli/crack hoti h
        "volume": "-5%"
    },

    "TIRED": {
        "style": "calm",        # Thaka hua, "Bas ab aur nahi..."
        "rate": "-15%", 
        "pitch": "-3Hz", 
        "volume": "-15%"
    },

    # ==========================================
    # 🟣 FEAR / SUSPENSE (Darr ka mahual)
    # ==========================================

    "FEAR": {
        "style": "fearful", 
        "rate": "+5%",          # Darr mein dhadkan aur bolna tez ho jata h
        "pitch": "+4Hz",        # Awaaz kampna
        "volume": "+5%"
    },

    "SHOCK": {
        "style": "fearful", 
        "rate": "+10%",         # "Kya?? Ye kaise hua??"
        "pitch": "+6Hz",        # Achanak high pitch
        "volume": "+10%"
    },

    "WHISPER": {
        "style": "calm",        # Azure Hindi me 'whisper' style nahi h, to 'calm' + low volume
        "rate": "-5%", 
        "pitch": "-2Hz", 
        "volume": "-30%"        # Bahut dheema (Fusfusana)
    },

    "SUSPENSE": {
        "style": "serious",     # "Kuch to gadbad hai..."
        "rate": "-10%", 
        "pitch": "-5Hz",        # Deep bass
        "volume": "-10%"
    },

    # ==========================================
    # 🟡 LIGHT / HAPPY (Mazaak aur Pyaar)
    # ==========================================

    "HAPPY": {
        "style": "cheerful", 
        "rate": "+5%", 
        "pitch": "+3Hz", 
        "volume": "+10%"
    },

    "HUMOR": {
        "style": "cheerful",    # Mazaakiya tone
        "rate": "+10%",         # Thoda bouncy
        "pitch": "+4Hz", 
        "volume": "+12%"
    },

    "CASUAL": {
        "style": "chat",        # Casual conversation (Dost se baat)
        "rate": "default", 
        "pitch": "default", 
        "volume": "default"
    },

    "ROMANTIC": {
        "style": "gentle",      # Pyar bhari baatein
        "rate": "-5%",          # Thoda slow aur soft
        "pitch": "-1Hz", 
        "volume": "-5%"
    },

    "EXCITED": {
        "style": "excited",     # "Arre wah! Jeet gaye!"
        "rate": "+15%", 
        "pitch": "+5Hz", 
        "volume": "+15%"
    }
}