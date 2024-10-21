import random
from captcha.audio import AudioCaptcha

def generate_random_captcha(lenght=6):
    characters='1234567890'
    captcha_txt=''.join(random.choices(characters,k=lenght))
    return captcha_txt

audio=AudioCaptcha()
captcha_txt=generate_random_captcha()
print("Generated Captcha txt :",captcha_txt)
audio_captcha=audio.generate(captcha_txt)
audio.write(captcha_txt,"Audio_Captcha.wav")
print("Audio captcha generated : Audio_Captcha.wav")