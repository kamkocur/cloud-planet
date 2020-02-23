# cloud-planet
#### Testy automatyczne do zadania rekrutacyjnego

##### Treść Zadania:

Kroki:
1. Wejście na stronę https://ingksiegowosc.pl/
2. Przejście do wersji demonstracyjnej aplikacji INGKsięgowość i zalogowanie do demo
3. Przy użyciu menu-nawigacji przejście na formularz wystawiania faktury
4. Ustawienie typu dokumentu "Paragon sprzedaży"
5. Wprowadzenie w polu "Nazwa produktu" tekstu "abc"
6. Wystawienie paragonu.

Oczekiwany wynik testu - przejście do podglądu dokumentu typu paragon sprzedaży o wartości 0,00 PLN, bez danych kontrahenta.

### README:
Rozwiązanie zadania zostało wykonane w środowisku PyCharm. Kod został napisany w języku Python wersji 3.6. Narzędziem obsługującym testy jest selenium.

#### Jak uruchomić?

1. Utwórz projekt z interpreterem Pythona wersji 3.6 (lub wyższej) wybierając folder "cloud-planet" jako źródłowy katalog projektu
2. Zainstaluj wymagane biblioteki przy pomocy komendy "pip install -r requirements.txt"
3. Uruchom testy komendą pytest tests/test_feature.py

##### Struktura projektu:

'tests' zawiera testy w pliku test_feature.py

'pages' zawiera selektory i page objecty w pliku invoice.py

'conftest.py' to plik z konfiguracją testową projektu tzw. setup

'requirements.txt' zawiera informacje jakie biblioteki są niezbędne do prawidłowego działania kodu


