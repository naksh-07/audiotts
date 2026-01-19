import html

def voice_block(voice, style, rate, pitch, volume, text):
    # Text ko safe banao
    safe_text = html.escape(text)

    return (
        f'<voice name="{voice}">'
            f'<mstts:express-as style="{style}">'
                f'<prosody rate="{rate}" pitch="{pitch}" volume="{volume}">'
                    f'{safe_text}'
                f'</prosody>'
            f'</mstts:express-as>'
            # FIX: Break ko voice tag ke ANDAR le aaye hain.
            # Ab Azure khush rahega.
            f'<break time="400ms"/>' 
        f'</voice>'
    )