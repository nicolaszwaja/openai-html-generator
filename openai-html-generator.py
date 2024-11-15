import openai
import tiktoken

def load_text_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Nie udało się wczytać pliku: {e}")
        exit()

def generate_html(api_key, article_path="artykul.txt", output_file="artykul.html", prompt_path="prompt.txt"):
    openai.api_key = api_key
    
    article_from_file = load_text_from_file(article_path)
    print("\nPlik artykułu został wczytany pomyślnie.")
    
    prompt_from_file = load_text_from_file(prompt_path)
    print("\nPlik z promptem został wczytany pomyślnie.")
    
    prompt = f"{prompt_from_file}\n {article_from_file}"

    encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
    article_tokens = encoder.encode(article_from_file)
    article_length_tokens = len(article_tokens)
    
    max_tokens = int(article_length_tokens * 1.2)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )

    generated_html = response['choices'][0]['message']['content'].strip()

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(generated_html)

    print(f"Odpowiedź zapisana do pliku: {output_file}")

def main():
    api_key = input("Proszę podać swój klucz API: ")
    
    article_path = input("Podaj ścieżkę do pliku z artykułem (domyślnie 'artykul.txt'): ")
    if not article_path:
        article_path = "artykul.txt"
        
    output_file = input("Podaj nazwę pliku, w którym chcesz zapisać kod html (domyślnie 'artykul.html'): ")
    if not output_file:
        output_file = "artykul.html"
        
    generate_html(api_key, article_path, output_file)

if __name__ == "__main__":
    main()
