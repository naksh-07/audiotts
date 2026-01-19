# settings/casting.py

"""
CASTING DIRECTOR: THE HOBBIT
----------------------------
Region: North Central US (Hindi Neural Models)
Main Voices Used:
- Swara (Female Base)
- Madhur (Male Young/Common)
- Kunal (Male Deep/Authoritative) - Agar ye nahi chala to Madhur use karenge
- Aarav (Male Youth/Comic)
- Rehaan (Male Rough/Old)
"""

CHARACTER_VOICES = {
    # ==========================
    # 🎤 THE NARRATOR (Sutradhaar)
    # ==========================
    "NARRATOR": "hi-IN-SwaraNeural",

    # ==========================
    # 🏠 HERO & WIZARD
    # ==========================
    
    # Bilbo: Thoda ghabraya hua, middle-aged lekin soft dil. 
    # Madhur ki pitch badha ke use "chota" dikhayenge.
    "BILBO": "hi-IN-MadhurNeural", 

    # Gandalf: Budha, taakatwar aur gusse wala. 
    # Kunal best hai heavy voice ke liye.
    "GANDALF": "hi-IN-KunalNeural",

    # ==========================
    # 🛡️ THE LEADER (Thorin)
    # ==========================
    # Thorin Oakenshield: Ghamandi aur Raja.
    "THORIN": "hi-IN-KunalNeural",

    # ==========================
    # ⚒️ THE DWARVES (Company)
    # ==========================
    # Inko humne groups mein baata hai unki personality ke hisab se.

    # Group 1: The Elders (Balin, Dwalin, Oin, Gloin)
    # Thodi bhaari aur samajhdar awaaz
    "BALIN":    "hi-IN-RehaanNeural",
    "DWALIN":   "hi-IN-RehaanNeural",
    "GLOIN":    "hi-IN-RehaanNeural",
    "OIN":      "hi-IN-RehaanNeural",

    # Group 2: The Young & Fighters (Fili, Kili)
    # Joshile launde
    "FILI":     "hi-IN-MadhurNeural",
    "KILI":     "hi-IN-MadhurNeural",

    # Group 3: The Funny/Fat/Weird (Bombur, Bofur, Bifur, Ori, Nori, Dori)
    # Aarav ki awaaz thodi lighter/comic hai
    "BOMBUR":   "hi-IN-AaravNeural",
    "BOFUR":    "hi-IN-AaravNeural",
    "BIFUR":    "hi-IN-AaravNeural",
    "ORI":      "hi-IN-AaravNeural",
    "DORI":     "hi-IN-AaravNeural",
    "NORI":     "hi-IN-AaravNeural",

    # ==========================
    # 🐉 VILLAINS & MONSTERS
    # ==========================
    
    # Smaug: The Dragon. Iski awaaz sabse deep hogi (Pitch -30% in logic).
    "SMAUG":    "hi-IN-KunalNeural",

    # Gollum: Ajeeb, schizophrenic. Aarav ko high pitch karke creepy banayenge.
    "GOLLUM":   "hi-IN-AaravNeural",

    # The Goblin King: Mota aur heavy.
    "GOBLIN_KING": "hi-IN-RehaanNeural",

    # Azog/Bolg (Orcs): Rough voice.
    "ORC_LEADER": "hi-IN-RehaanNeural",
    
    # Generic Villains
    "TROLL":    "hi-IN-KunalNeural",
    "GOBLIN":   "hi-IN-AaravNeural",

    # ==========================
    # 🧝 ELVES & HUMANS
    # ==========================
    
    # Elrond: Wise, calm, ageless. Swara (Male version) ya soft Madhur.
    # Elves ke liye hum Madhur use karenge lekin soft style mein.
    "ELROND":       "hi-IN-MadhurNeural",
    "LEGOLAS":      "hi-IN-MadhurNeural",
    "THRANDUIL":    "hi-IN-MadhurNeural", # Elven King

    # Bard the Bowman: Heroic Human.
    "BARD":         "hi-IN-MadhurNeural",

    # Master of Lake-town: Lalchi politician type.
    "MASTER":       "hi-IN-RehaanNeural",

    # ==========================
    # 👥 SIDE CHARACTERS / ONE-TIMERS
    # ==========================
    
    "OLD_MAN":      "hi-IN-RehaanNeural",
    "OLD_WOMAN":    "hi-IN-SwaraNeural", # Isko slow kar denge
    "GUARD":        "hi-IN-KunalNeural",
    "SOLDIER":      "hi-IN-KunalNeural",
    "VILLAGER_M":   "hi-IN-MadhurNeural",
    "VILLAGER_F":   "hi-IN-SwaraNeural",
    "CHILD":        "hi-IN-AaravNeural"   # Pitch badha ke bachcha banayenge
}

# NOTE:
# Agar tere Azure account me 'Kunal' ya 'Rehaan' nahi chalte,
# to unko replace karke 'MadhurNeural' kar dena. Code baki sambhal lega.