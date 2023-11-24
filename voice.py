from gtts import gTTS
import os

def dosyayi_sese_cevir(dosya_adi, dil='tr'):
    try:
        # Dosyayı oku
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            metin = dosya.read()

        # Metni ses dosyasına dönüştür
        sesli_metin = gTTS(text=metin, lang=dil, slow=False)

        # Ses dosyasını kaydet
        ses_dosya_adi = dosya_adi.replace('.txt', '_ses.mp3')
        sesli_metin.save(ses_dosya_adi)

        # Ses dosyasını oynat
        os.system(f"start {ses_dosya_adi}")

    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    dosya_adi = input("Dosya Yolunu girin: ")
    dosyayi_sese_cevir(dosya_adi)
