from dotenv import load_dotenv
import os
from gigachat import GigaChat
from google import genai
from google.genai.types import HttpOptions
from datetime import datetime

LOG_FILE = "test_task/output.log"


def log(text: str):
    """Записывает текст в лог-файл"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


def print_and_log(text: str):
    """Печать и одновременное логирование"""
    print(text)
    log(text)


if __name__ == "__main__":
    load_dotenv()

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")

    # Инициализация GigaChat
    giga = GigaChat(
        credentials=GIGACHAT_API_KEY,
        verify_ssl_certs=False,
        scope="GIGACHAT_API_PERS"
    )

    # Инициализация Gemini
    http_options = HttpOptions()
    http_options.client_args = {"proxy": os.getenv("PROXY_URL")}

    gemini = genai.Client(api_key=GEMINI_API_KEY, http_options=http_options)

    # Меню
    while True:
        print("\n=== МЕНЮ ===")
        print("1 — Задать вопрос 3 моделям")
        print("2 — Выйти")

        choice = input("Выберите пункт: ")

        if choice == "2":
            print("Выход.")
            break

        if choice == "1":
            question = input("\nВведите ваш вопрос:\n> ")

            header = f"\n=== Новый запрос ({datetime.now()}) ==="
            print_and_log(header)
            print_and_log(f"Вопрос: {question}\n")

            # --- GigaChat ---
            print_and_log("[MODEL] GigaChat:")
            try:
                answer_gc = giga.chat(question).choices[0].message.content
                print_and_log(answer_gc + "\n")
            except Exception as e:
                print_and_log(f"Ошибка GigaChat: {e}\n")

            # --- Gemini Flash ---
            print_and_log("[MODEL] Gemini 2.5 Flash:")
            try:
                answer_flash = gemini.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=question
                ).text
                print_and_log(answer_flash + "\n")
            except Exception as e:
                print_and_log(f"Ошибка Gemini Flash: {e}\n")

            # --- Gemini Pro ---
            print_and_log("[MODEL] Gemini 2.5 Pro:")
            try:
                answer_pro = gemini.models.generate_content(
                    model="gemini-2.5-pro",
                    contents=question
                ).text
                print_and_log(answer_pro + "\n")
            except Exception as e:
                print_and_log(f"Ошибка Gemini Pro: {e}\n")

            print("Все ответы сохранены в output.log")

        else:
            print("Неверный ввод. Повторите.")
