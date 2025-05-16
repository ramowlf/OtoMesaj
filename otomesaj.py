import os
import asyncio
import random
from telethon import TelegramClient

os.system("clear")

class ModulDenetleme:
    def indir(self, modul):
        os.system(f"pip install {modul}")
        os.system("clear")

    def kontrol(self, modul):
        try:
            __import__(modul)
        except ImportError:
            self.indir(modul)

    def __init__(self):
        gerekli_moduller = ["telethon"]
        for gerekli_modul in gerekli_moduller:
            self.kontrol(gerekli_modul)

ModulDenetleme()

print("\nOTO MESAJ ARACI\n")
print("------------------------------------")
print("Oto Mesaj Tool")
print("@ramowlf @TurkUserBotKanali")
print("------------------------------------\n")

accounts = [
    {
        "session": "ramo",
        "api_id": 28063083,
        "api_hash": "17885ee1ab21bf91bf1339d980490b00",
        "tel_no": "+905376299821", # buraya tel no gir
        "messages": [
            """⭐️ MERHABA BEBEĞİM ⭐️

😜 22 YAŞINDA AZGIN VE ÇITIRIM

✅ ONAYLI SHOWCUYUM ✅

💸ÜCRETLİYİM💸

💋SEXTİNG, GÖRÜNTÜLÜ SHOW 💋

🔵ANAL, DİLDOLU ISLAK SHOW🔵

🔞 ÜCRETLİ OYUNCAKLI, TEKLİ, PARTNERLİ VE ÖZEL VİDEOLARIM 🔞
 
REAL YOK YAZMAYIN 🚫
 
@nurs3ma 
@nurs3ma
@nurs3ma""",
            
            """Genel olarak 22 yaşında çıtır🔥
Üniversite öğrencisiyim 💋
uyguna boşaltıyorum 👅
Reel✅
Sexting✅
Görüntülü Show✅
Arşiv✅
Özel video✅
Kendime ait ibanım ✅
Ücretli görüntülü teyit ✅
Beyler hızlı dm💋
Teyit sapığı yazmasın👎"""
        ]
    }
]

async def mesaji_gonder(client, messages):
    message = random.choice(messages)  
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            try:
                await client.send_message(
                    dialog.entity,
                    message,
                    parse_mode='markdown',
                    link_preview=False
                )
                print(f"Mesaj gönderildi: {dialog.name}")
            except Exception as e:
                print(f"Hata ({dialog.name}): {e}")
                continue

async def run_account(account):
    client = TelegramClient(account["session"], account["api_id"], account["api_hash"])
    print(f"{account['session']} - Telegram Hesabınıza Giriş Yapılıyor... ({account['tel_no']})")

    async def code_callback():
        print(f"{account['tel_no']} numaralı hesaba kod gönderildi. Lütfen gelen kodu girin:")
        return await asyncio.to_thread(input, f"{account['tel_no']} kodunu girin: ")

    await client.start(phone=account["tel_no"], code_callback=code_callback)
    print(f"{account['session']} - Oturum açıldı. Mesaj gönderme işlemi başlatılıyor...")

    async with client:
        while True:
            await mesaji_gonder(client, account["messages"])
            print(f"{account['session']} - Grup sohbetlerine mesaj iletildi. 30 saniye bekleniyor...")
            await asyncio.sleep(30)

async def main():
    tasks = [asyncio.create_task(run_account(account)) for account in accounts]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    