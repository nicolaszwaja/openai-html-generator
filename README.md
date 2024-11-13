# OpenAI HTML Generator

## Opis

Projekt ma na celu stworzenie aplikacji, która integruje się z API OpenAI, aby automatycznie przekształcać artykuły tekstowe na dobrze sformatowane pliki HTML. Aplikacja odczytuje artykuł z pliku tekstowego, przesyła jego treść wraz z odpowiednim promptem do OpenAI, a następnie zapisuje otrzymany wynik w formie pliku HTML, który spełnia określone wytyczne strukturalne.

## Funkcje projektu:

1. **Integracja z OpenAI**: Aplikacja łączy się z API OpenAI, umożliwiając przekazywanie tekstu do analizy i przetwarzania.
2. **Odczyt artykułu**: Aplikacja odczytuje zawartość artykułu z pliku tekstowego.
3. **Przesyłanie do OpenAI**: Tekst artykułu oraz odpowiedni prompt są przekazywane do modelu OpenAI w celu przetworzenia na kod HTML.
4. **Generowanie HTML**: Otrzymany wynik jest zapisany w pliku `artykul.html` zawierającym odpowiednią strukturę HTML.
5. **Generowanie tagów HTML**: Wygenerowany plik HTML zawiera odpowiednie tagi semantyczne, a także oznaczenia dla miejsc, w których mogą pojawić się obrazy (tagi `<img>` z odpowiednimi atrybutami `alt`).
6. **Wstawianie obrazów**: Obrazki są oznaczane jako placeholdery w kodzie HTML z możliwością łatwej wymiany na rzeczywiste grafiki.

## Wymagania

- Python 3.x lub JavaScript (Node.js).
- Dostęp do API OpenAI (konieczność posiadania klucza API).
- Zainstalowane biblioteki:
  - **Python**: `openai`, `requests`, `os`, `json`
  - **JavaScript**: `axios`, `fs`

## Struktura projektu

Projekt jest podzielony na dwie główne części:

- **Odczyt pliku i komunikacja z API OpenAI**: Aplikacja odczytuje plik tekstowy zawierający artykuł, przetwarza tekst, a następnie przesyła go do OpenAI.
- **Generowanie kodu HTML**: OpenAI przekształca otrzymany tekst na HTML, który jest następnie zapisywany w pliku `artykul.html`.

## Wytyczne HTML:

1. Użycie odpowiednich tagów HTML (np. `<h1>`, `<p>`, `<section>`) do strukturyzacji artykułu.
2. Wstawianie tagów `<img>` w odpowiednich miejscach, gdzie mogą pojawić się grafiki, z atrybutem `alt` zawierającym dokładny prompt do wygenerowania grafiki.
3. Każdy obrazek powinien mieć podpis umieszczony za pomocą tagu `<figcaption>`.
4. Kod HTML nie zawiera CSS ani JavaScript, tylko czysty kod strukturalny, gotowy do wstawienia pomiędzy tagi `<body>`.

## Instrukcja użycia

1. Skopiuj projekt na swoje urządzenie.
2. Upewnij się, że masz zainstalowanego Pythona lub Node.js.
3. Pobierz odpowiedni plik z artykułem, który chcesz przekształcić do HTML.
4. Zarejestruj się w OpenAI i zdobądź swój klucz API.
5. Skonfiguruj aplikację, wpisując swój klucz API w kodzie.
6. Uruchom aplikację, aby przetworzyć artykuł do formatu HTML.
7. Plik `artykul.html` zostanie zapisany w katalogu projektu, gotowy do użycia.
