import os
import time


import re
import socket

def is_valid_email(email):
    # Regex for validating email format
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

def verify_email_domain(email):
    try:
        domain = email.split('@')[1]
        # Attempt to resolve the domain
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        print(f"Domain {domain} does not exist or cannot be resolved.")
        return False


def authenticate_email():
    print("Welcome to TS-CLASSROOM! Please enter your email to proceed:")
    print("A email Is Like This: youremail@putdomainhere.org or youremail@putdomainhere.edu")
    email = input("Email: ")



    # Syntax validation
    if not is_valid_email(email):
        print("Invalid email format. Please try again.")
        return authenticate_email()
    
    # Domain verification
    if not verify_email_domain(email):
        print("The domain of this email doesn't seem to exist. Please try again.")
        return authenticate_email()
    
    # Basic validation for email format
    if "@" in email and "." in email:
        print(f"Thank you, {email}. Authentication process starting...")
        # Simulate authentication
        print("Authenticating...")
        import time
        time.sleep(2)
        print("Authentication successful!")
        return email
    else:
        print("Invalid email format. Please try again.")
        return authenticate_email()


def ts_classroom_student2025():
    time.sleep(2)
    print("Welcome to TS-Classroom 2025!")
    time.sleep(2)
    print("If You Are Seeing this It Means You are Testing TS-CLASSROOM For Schools Around The World!")
    time.sleep(2)
    print("This is a test version of TS-Classroom 2025.")
    time.sleep(2)
    print("Please Report Any Bugs To Tadeo A Gonzlaez")
    time.sleep(2)
    print("Type in This email To Tell Tadeo A Gonzlaez About Bugs: tadeotherocketbuilder@gmail.com or tadeotherocketbuilder@outlook.com")
    time.sleep(2)
    print("The Screen Will Now Clear")
    print("Please Wait...")
    time.sleep(2)
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The Screen Has Been Cleared")
    time.sleep(2)
    print("Let's Start")
    time.sleep(2)
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)

    
    print("\n\n********************************************************************")
    print("*              TS-CLASSROOM 2025 FOR STUDENTS  AND TEACHERS        *")
    print("*                    COPYRIGHT (C) 2025 Tadeo A Gonzlaez           *")
    print("*                       TYPE help FOR COMMANDS                     *")
    print("*                      LEARNING PURPOSES ONLY                      *")
    print("********************************************************************")
    time.sleep(2)
    while True:
        user_input = input("TS-CLASSROOM 2025 Console>> ")
        if user_input == "help":
            print("Available commands:")
            print("- essay: Open Microsoft Word")
            print("- present m : Open Microsoft PowerPoint")
            print("- exit: Exit the program")
            print("- teams: Open Microsoft Teams")
            print("- help: Show this help message")

        elif user_input == "essay":
            print("Opening Microsoft Word...")
            time.sleep(2)
            os.system('start winword.exe')

        elif user_input == "present":
            print("Opening Microsoft PowerPoint...")
            time.sleep(2)
            os.system('start powerpnt.exe')

        elif user_input == "exit":
            os.system("taskkill /F /IM cmd.exe")
            os._exit(0)

        elif user_input == "teams":
            print("Opening Microsoft Teams...")
            time.sleep(2)
            os.system('cd C:\\Program Files\\WindowsApps\\MSTeams_25060.205.3499.6849_x64__8wekyb3d8bbwe')
            os.system('ms-teams.exe')









if __name__ == "__main__":
    email_account = authenticate_email()
    print(f"Logging In With {email_account}")
    ts_classroom_student2025()