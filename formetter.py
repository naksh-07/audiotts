import os
import sys
from google import genai
from google.genai import types

# ==========================================
# 🔑 APNI KEY YAHAN DAAL (DIRECT)
# ==========================================
GEMINI_API_KEY = ""  # 👈 Yahan apni asli key paste kar

# ==========================================
# ⚙️ PATH SETTINGS
# ==========================================
# Script jahan hai, wahin file dhundega
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(CURRENT_DIR, "full_story.txt")
OUTPUT_TEX = os.path.join(CURRENT_DIR, "final_book.tex")

# Output folder ensure karo
os.makedirs(os.path.dirname(OUTPUT_TEX), exist_ok=True)

# ==========================================
# 🧠 AI INSTRUCTIONS (LOCKED TEMPLATE)
# ==========================================
# Hum raw string (r""") use kar rahe hain taaki backslashes (\) kharab na ho
SYSTEM_PROMPT = r"""
You are a Professional Book Typesetter & LaTeX Expert.
I will give you the raw text of a book (which may be in Hindi or English).

YOUR TASK:
1. Convert this text into a high-quality LaTeX Book code.
2. **STRICTLY USE THE PREAMBLE BELOW.** Do not change fonts, packages, or page size.
3. Structure the content using \chapter{}, \section{}, etc.
4. For Tables: Use `tabularx` environment as shown in the template example.
5. For Chemistry: Use `\ce{...}` (e.g., \ce{H2O}).
6. Output ONLY raw LaTeX code.

REUSE THIS EXACT TEMPLATE STRUCTURE:
--------------------------------------------------
\documentclass[11pt, a4paper, twoside]{book} 

% --- PACKAGES ---
\usepackage{fontspec}
\usepackage{polyglossia}       % Hindi ke liye best
\usepackage[margin=2.5cm]{geometry} % A4 Margin
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tabularx}          % Smart Tables
\usepackage{booktabs}          % Sundar lines
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{parskip}
\usepackage[version=4]{mhchem} % Chemistry Package
\usepackage[table]{xcolor}     % Table Colors

% --- FONT SETTINGS (The Fix) ---
\setmainfont[Script=Devanagari]{FreeSerif}
\setsansfont[Script=Devanagari]{FreeSans}
\setmonofont{FreeMono}

% Language Setup
\setdefaultlanguage{hindi}
\setotherlanguage{english}

% --- HEADER & FOOTER ---
\pagestyle{fancy}
\fancyhead{}
\fancyfoot{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\rightmark}
\fancyhead[RE]{\leftmark}
\renewcommand{\headrulewidth}{0.4pt}

\title{My Book Title}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\mainmatter

% ... AI WILL INSERT CONTENT HERE ...
% Example Table Usage (If needed):
% \begin{table}[h]
%   \centering
%   \rowcolors{2}{gray!10}{white}
%   \begin{tabularx}{\textwidth}{ | l | X | }
%      \hline
%      Title & Long Description \\
%      \hline
%   \end{tabularx}
% \end{table}

\end{document}
--------------------------------------------------
"""

def generate_latex():
    print("🚀 Gemini ko text bhej raha hu... (Template: A4 + FreeSerif)")

    # Key Check
    if "TERI_ASLI_KEY" in GEMINI_API_KEY:
        print("❌ Error: Script mein Line 10 par API Key daal!")
        return

    # File Check
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: Input file nahi mili: {INPUT_FILE}")
        print("👉 Pehle 'full_story.txt' ko isi folder mein daal.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw_text = f.read()

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        # Gemini 2.5 Flash ko call karo
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=f"Here is the story text. Convert it to the specified A4 LaTeX format:\n\n{raw_text}",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7
            )
        )

        latex_code = response.text
        # Markdown cleanup (Agar AI ne ```latex likh diya to)
        latex_code = latex_code.replace("```latex", "").replace("```", "")

        with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
            f.write(latex_code)

        print("\n🎉 MUBARAK HO! Final Book Code Ready Hai.")
        print(f"📂 Saved to: {OUTPUT_TEX}")
        print("-------------------------------------------------")
        print("👇 Final Steps:")
        print("1. Copy code from 'final_book.tex'")
        print("2. Paste in Overleaf")
        print("3. **Menu > Compiler > XeLaTeX** select kar")
        print("4. Download PDF!")

    except Exception as e:
        print(f"❌ Error aaya: {e}")

if __name__ == "__main__":
    generate_latex()