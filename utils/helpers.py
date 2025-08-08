import os
from datetime import datetime

def save_response(username, prompt, response):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/{username}_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(f"User: {username}\n")
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Response: {response}\n")

    print(f"📁 Saved to {filename}")
