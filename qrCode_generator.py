import qrcode

arabic_verses:str = "اِنَّ رَبِّیْ رَحِیْمٌ وَّدُوْدٌ" 
urdu_transition:str = "یقین مانو کہ میرا ربّ بڑی مہربانی والا اور بہت محبت کرنے والا ہے"
combined_text = f"{arabic_verses}\n{urdu_transition}"

qr = qrcode.make(combined_text)
qr.save("qr.png")
