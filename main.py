import os
from models.tinyllama import ask_tinyllama
from utils.helpers import save_response

def main():
    print("🚀 Welcome to Offline AI CLI with TinyLlama!")
    username = input("👤 Enter your name: ")

    while True:
        print("\n📜 MENU")
        print("1. Ask TinyLlama")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            prompt = input("💬 What would you like to ask TinyLlama?\n> ")
            response = ask_tinyllama(prompt)
            print(f"\n🤖 Response from TinyLlama:\n{response}")
            save_response(username, prompt, response)

        elif choice == '2':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
