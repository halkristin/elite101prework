print("Welcome to your Chatbot!")
name = input("Tell us your name:")
print("Hello ",name)
age = input("What is your grade?")
print("Perfect! How can I help you today?")

def display_menu():
  print("\n Options:")  
  print("1. x ")
  print("2. x ")
  print("3. x ")
  print("4. Exit ")

def user_selection():
    user_pick = int(input("Enter a number between 1-4: "))
    if user_pick == 1:
        print("1.")
    elif user_pick == 2:
        print("2.")
    elif user_pick == 3:
        print("3.")
    elif user_pick == 4:
        print("Goodbye!")
    else:
        print("Invalid")
      
display_menu()

