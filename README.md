# OpenAI HTML Generator

## Opis
Aplikacja, która łączy się z API OpenAI w celu automatycznego przekształcania artykułów tekstowych na pliki HTML. Program odczytuje artykuł z pliku tekstowego, przesyła go do modelu OpenAI, a następnie generuje strukturalny plik HTML z odpowiednimi tagami oraz miejscami na obrazy.

## Główne funkcje
- Integracja z API OpenAI do przetwarzania artykułów.
- Odczyt artykułu z pliku tekstowego.
- Generowanie strukturalnego kodu HTML z odpowiednimi tagami.
- Wstawianie placeholderów dla obrazów za pomocą tagu `<img>`.
- Tworzenie pliku `artykul.html` z wygenerowanym kodem HTML.

## Wymagania
- Python 3.6 lub wyższy.
- Klucz API OpenAI (możliwość uzyskania klucza po kontakcie z zespołem Oxido).
- Biblioteki Python:
  - `openai==0.28.0`
  - `tiktoken`

## Struktura projektu
Projekt składa się z kilku głównych komponentów:

1. **Odczyt pliku**: Program odczytuje artykuł z pliku tekstowego i przesyła go do API OpenAI.
2. **Integracja z OpenAI**: Artykuł jest wysyłany do modelu GPT-3.5, który generuje kod HTML zgodnie z określonymi wytycznymi.
3. **Generowanie HTML**: Program generuje strukturę HTML, w tym placeholdery dla obrazów oraz odpowiednie podpisy.
4. **Zapis pliku HTML**: Wygenerowany kod HTML jest zapisywany w pliku `artykul.html`.

## Instrukcja użycia

### 1. Zainstaluj wymagane biblioteki
Przed uruchomieniem aplikacji, zainstaluj wymagane biblioteki Python:

```bash
pip install openai==0.28.0 tiktoken
```
### 2. Skonfiguruj aplikację
Ustaw swój klucz API OpenAI, który musisz podać podczas uruchamiania programu.
Przygotuj plik z artykułem (domyślnie oczekiwany plik to artykul.txt).
Przygotuj plik z promptem (domyślnie prompt.txt), który będzie zawierał instrukcje dla modelu OpenAI.
### 3. Uruchom program
W terminalu uruchom program:
```
python openai_html_generator.py
```

### 4. Podaj klucz API
Podczas uruchamiania aplikacja poprosi Cię o podanie klucza API OpenAI. Możesz uzyskać go kontaktując się z zespołem Oxido.

### 5. Wskaż plik artykułu
Program automatycznie wczyta artykuł z pliku artykul.txt, ale możesz wskazać inną ścieżkę do pliku tekstowego z artykułem.

### 6. Generowanie pliku HTML
Po przetworzeniu artykułu przez model OpenAI, wygenerowany plik HTML zostanie zapisany w artykul.html. Wygenerowany plik będzie zawierał:

Strukturalny kod HTML (nagłówki, paragrafy, listy).
Placeholdery dla obrazów z tagami `<img>` i atrybutami alt, wskazującymi prompt do generowania grafik.
Podpisy dla obrazów, umieszczone w tagach `<figcaption>`.
