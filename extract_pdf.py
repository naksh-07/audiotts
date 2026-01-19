import os
import sys
from pypdf import PdfReader

# Config setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    from settings.config import BASE_DIR
except ImportError:
    BASE_DIR = os.getcwd()

# ================= SETTINGS =================
PDF_FILE = "meri_story.pdf"  # 👈 Apni PDF ka naam yahan likh
# ============================================

INPUT_PATH = os.path.join(BASE_DIR, "input", PDF_FILE)
OUTPUT_PATH = os.path.join(BASE_DIR, "input", "full_story.txt")

def extract_text():
    print(f"📄 Reading PDF: {PDF_FILE}...")
    
    if not os.path.exists(INPUT_PATH):
        print(f"❌ Error: {INPUT_PATH} nahi mili.")
        return

    reader = PdfReader(INPUT_PATH)
    full_text = ""

    # Page by page text nikalna
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            # Thodi safai (Header/Footer hatane ki koshish)
            lines = text.split('\n')
            clean_lines = [line for line in lines if len(line) > 5] # Choti lines hatao
            full_text += "\n".join(clean_lines) + "\n\n"
    
    # Save karna
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(full_text)
    
    print(f"✅ Extraction Done! Text file saved at: {OUTPUT_PATH}")

if __name__ == "__main__":
    extract_text()