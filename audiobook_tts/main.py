import os
import sys
import time
import azure.cognitiveservices.speech as speechsdk

# Settings folder access karne ke liye path set kar rahe hain
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Config se settings import karo
from settings.config import AZURE_KEY, AZURE_REGION, AUDIO_OUTPUT_DIR, AUDIO_QUALITY_STRING
from ssml.ssml_generator import generate_ssml

def text_to_speech(ssml_file, output_audio_path):
    # 1. Azure Setup
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_KEY, region=AZURE_REGION)
    
    # Quality Set karo (Config se)
    if AUDIO_QUALITY_STRING == "Audio48Khz192KBitRateMonoMp3":
        speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio48Khz192KBitRateMonoMp3)
    
    # 2. Output File Setup
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_audio_path)

    # 3. Synthesizer Create karo
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # 4. SSML File Read karo
    try:
        with open(ssml_file, "r", encoding="utf-8") as f:
            ssml_string = f.read()
    except Exception as e:
        print(f"❌ File Read Error: {e}")
        return

    print(f"🎙️ Dubbing: {os.path.basename(ssml_file)} ...")
    
    # 5. Azure ko bhejo (Async Call)
    result = synthesizer.speak_ssml_async(ssml_string).get()

    # 6. Result Check
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"✅ Saved: {output_audio_path}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        details = result.cancellation_details
        print(f"❌ Azure Error: {details.reason}")
        if details.error_details:
            print(f"🔍 Error Details: {details.error_details}")

def run_project():
    print("\n🚀 Audiobook Pipeline Starting...\n")
    
    # Step 1: SSML Generate karo
    xml_files = generate_ssml()

    if not xml_files:
        print("⚠️ Koi SSML file nahi bani. Input file check kar bhai.")
        return

    # Step 2: Audio Folder Check/Create
    # Ye folder wahin banega jahan tera main.py hai
    if not os.path.exists(AUDIO_OUTPUT_DIR):
        os.makedirs(AUDIO_OUTPUT_DIR)
        print(f"📂 Created Audio Folder: {AUDIO_OUTPUT_DIR}")
    else:
        print(f"📂 Saving to: {AUDIO_OUTPUT_DIR}")

    print(f"🎯 Total {len(xml_files)} parts process karne hain.\n")

    # Step 3: Loop through all parts
    for xml_path in xml_files:
        # File name nikaalo (chapter1_part1.xml -> chapter1_part1)
        base_name = os.path.splitext(os.path.basename(xml_path))[0]
        
        # .mp3 extension lagao
        mp3_name = f"{base_name}.mp3"
        
        # Full path banao (audio/chapter1_part1.mp3)
        output_path = os.path.join(AUDIO_OUTPUT_DIR, mp3_name)
        
        # Convert karo
        text_to_speech(xml_path, output_path)
        
        # Thoda rest (Taaki Azure block na kare)
        time.sleep(1)

    print("\n🎉 Badhai ho! Saari audio files 'audio' folder mein ready hain.")

if __name__ == "__main__":
    run_project()