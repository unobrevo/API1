import requests
import time
import urllib
import json
import hashlib
import hmac


def main():
    while True:
        print("Wybierz operacje do wykonania")
        print("1 - Api publiczne")
        print("2 - Api prywatne")
        print("9 - Zamknij program")
        print("")
        exit2=False

        wybor = int(input('Wybór: '))
        print("")
        while exit2==False:

            if wybor==1:

                print("--- API Publiczne---")
                print("Wybierz operację do wykonania")
                print("1 - Ticker")
                print("2 - Statystyka rynku")
                print("3 - Orderbook")
                print("4 - Ostatnie transakcje")
                print("5 - Wykres świecowy")
                print("9 - Wroc")
                print("")

                pub=int(input('Wybór: '))
                print("")

                if pub==1:

                    while True:
                        print('Rynek BTC-PLN')
                        print('1 - Obecny kurs')
                        print("2 - Kurs poprzedniej transakcji")
                        print("9 - Wróć")
                        print("")

                        t = int(input('Wybór: '))

                        if t==1:
                            r = requests.get("https://api.bitbay.net/rest/trading/ticker/BTC-PLN")
                            print('Obecny kurs BTC to: ' + r.json()['ticker']['rate'])
                            print("")
                            time.sleep(2)

                        elif t==2:
                            r = requests.get("https://api.bitbay.net/rest/trading/ticker/BTC-PLN")
                            print('Poprzedni kurs BTC to: ' + r.json()['ticker']['previousRate'])
                            print("")
                            time.sleep(2)

                        elif t==9:
                            break
                            time.sleep(1)

                        else:
                            print('Wybierz poprawną opcję')
                            print("")
                            time.sleep(1)


                elif pub==2:
                        r = requests.get('https://api.bitbay.net/rest/trading/stats/BTC-PLN')
                        print('Statystyka rynku BTC-PLN: ' + str(r.json()))
                        print("")
                        time.sleep(2)

                elif pub==3:
                        r = requests.get('https://api.bitbay.net/rest/trading/orderbook/BTC-PLN')
                        print('Orderbook: jedna pozycja kupna i sprzedaży: ')
                        print('Orderbook sell (BTC-PLN): ' + str(r.json()['sell'][0]))
                        print('Orderbook buy (BTC-PLN): ' + str(r.json()['buy'][0]))
                        print('Gdzie: ')
                        print('ra - Kurs pozycji')
                        print('ca - Obecna ilość kryptowaluty w pozycji')
                        print('sa - Początkowa ilość kryptowaluty w pozycji')
                        print('pa - Ilość kryptowaluty w pozycji przed ostatnią zmianą')
                        print('co - Ilość ofert na którą składa się pozycja')
                        print("")
                        time.sleep(2)

                elif pub==4:
                        r = requests.get('https://api.bitbay.net/rest/trading/transactions/BTC-PLN')
                        print('Ostatnie transakcje: ' + str(r.json()))
                        print("")
                        time.sleep(2)

                elif pub == 5:
                        r = requests.get('https://api.bitbay.net/rest/trading/candle/history/BTC-PLN/3600?from=1510394400000&to=1510401600000')
                        print('Wykres świec: ' + str(r.json()))
                        print("")
                        time.sleep(2)

                elif pub == 9:
                    break

                else:
                    print('Wybierz poprawną opcję')
                    print("")
                    time.sleep(1)


            elif wybor==2:

                print("--- API Prywatne---")
                print("Wybierz operację do wykonania")
                print("1 - Wystaw ofertę")
                print("2 - Aktywne oferty")
                print("3 - Prowizje i konfiguracja")

                prv = int(input('Wybór: '))
                print("")

                if prv == 1:

                    while True:
                        secret = "e0db05ba-4d8b-4a35-ae3f-8f8984400e4c"
                        apiKey = "03cb881f-3799-4cde-b2fe-cb84a5b6539f"

                        timestamp = int(time.time())

                        data = urllib.parse.urlencode((('method', 'info'), ('moment', timestamp)))

                        apihash = hmac.new(secret, data.encode('utf-8'), hashlib.sha512).hexdigest()

                        res = requests.post('https://bitbay.net/API/Trading/tradingApi.php',
                                            headers={
                                                'API-Key': apiKey,
                                                'API-Hash': apihash,
                                                'Content-Type': 'application/json'
                                            },
                                            data=data
                                            )

                        print(res)
                        print(res.text)



            elif wybor==9:
                exit2==True
                exit(0)

            else:
                print('Wybierz poprawną opcję')
                print("")
                time.sleep(1)
                break




if __name__==("__main__"):
    main()



