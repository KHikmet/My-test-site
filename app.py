# Internal Dev App
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    email = os.getenv("EMAIL")
    db = os.getenv("DB_URL")

    print("Starting internal service...")
    print(f"Connected as: {email}")
    print(f"Database: {db}")

if __name__ == "__main__":
    main()
