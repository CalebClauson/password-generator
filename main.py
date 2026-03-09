from generation import password_generation, generate_password
from prompt import welcome_prompt

def main():
    welcome_prompt()
    password = password_generation()
    print(f"Generated Password: {password}")
main()