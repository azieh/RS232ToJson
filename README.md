# Wersja z Socket.IO

Jest to gotowa wersja dostosowana do komunikacji z Socket.io.

W pliku helper.py znajduje się konfiguracja programu. W sumie interesuje was tylko 
-SocketIoAuthLocation, 
-SocketIoAuthQueryString,
-SocketIoServerAddress.

W katalogu authorization znajduje się certyfikat privateKey.pem. W razie potrzeby to trzeba go zaktualizować.
W kluczu JWT przesyłam payload np "{ 'location': 'NowySacz' }". Można ustawić to z poziomu helper.py. Wy po JWT możecie rozpoznać kto się do was loguje.

# Jak włączyć

Trzeba odpalić plik main.py jako serwis który działa na stałe w tle urządzenia. Tak jak wcześniej.

Ogólnie starego programu nie ruszałem. W razie potrzeby on jest kompatybilny ze starą wersją sesja.pl

### Prerequisites
Project is working on linux, but can be simple changed to work on windows.

Project required:

```
python 3.10
#~: python -m pip install pyserial
#~: python -m pip install asyncio
#~: python -m pip install python-socketio
#~: python -m pip install PyJWT
#~: python -m pip install cryptography
#~: python -m pip install aiohttp
```