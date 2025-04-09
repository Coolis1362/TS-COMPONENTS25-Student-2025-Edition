import os
import sys
import time

def ts_note_student2025():
    print("Hello, this is a test script for the TS-NOTES project.")
    time.sleep(2)
    print("This script is designed to demonstrate the functionality of the project.")   
    time.sleep(2)
    print("This is also a test for TS-COMPONENTS25 Student 2025 Edition")
    time.sleep(2)
    print("Let's start")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)

    print("\n\n******************************************************************")
    time.sleep(1)
    print("*       TS-NOTES Student 2025 Edition FOR EDUCATION ONLY         *")
    time.sleep(1)
    print("*       This is The Test for TS-NOTES Student 2025 Edition       *")
    time.sleep(1)
    print("*              You may start Taking Notes                        *")
    time.sleep(1)
    print("*                      Let's Start                               *")
    time.sleep(1)
    print("*               Press help for select commands                   *")
    time.sleep(1)
    print("*                 COPYRIGHT (C) 2025 TADEO A GONZALEZ            *")
    print("******************************************************************")
    time.sleep(1)
    print("Title:")
    while True:
        user_input = input()
        if user_input == "exit":
            print("Exiting...")
            sys.exit(0)
            
        elif user_input == "exit cmd.exe":
                os.system("taskkill /F /IM cmd.exe")
                os._exit(0)

        elif user_input == "clear":
                os.system("cls" if os.name == "nt" else "clear")
                print("Cleared the screen.")
                continue
            
        elif user_input == "feedback":
                print("Feedback:")
                feedback_input = input()
                if feedback_input == "done feedback":
                    print("Feedback submitted.")
                    print("Thank you for your feedback.")
                    continue    

        elif user_input == "help":
                print("Available commands:")
                print("exit - Exit the program")
                print("clear - Clear the screen")
                print("feedback - Provide feedback")
                print("help - Show this help message")
                continue
        



if __name__ == "__main__":
    ts_note_student2025()