def addTask():
    print("\nTask added") #Function to display the first option in the menu
def view():
    print("\nViewing my to-do list") #Function to display the second option
def doneTask():
    print("\nTask marked as done") #Fucntion to display the third option
def removeTask():
    print("\nTask removed") #Function to display the fourth option
def quit():
    print("\nGoodbye, Lightning McQueen!") #Function to display the final option
def main():
        print("Hello, Lightning McQueen! Here's your to-do list:") #Initial greeting
        Options={"1":addTask, "2":view, "3":doneTask, "4":removeTask, "5":quit}
        while True: #Displaying the menu
            print("\nLIGHTNING MCQUEEN'S TO-DO LIST") 
            print("1. Add a task")
            print("2. View my to-do list")
            print("3. Mark a task as done")
            print("4. Remove a task")
            print("5. Quit") 

            choice= input("/nChoose an option: ").strip() #Taking input from the user
            if choice =="5":
                print("What's the move, champ?")
                break #Exit menu when the user chooses to quit
            #Using the functions
            action=Options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, choose again.")

if __name__=="__main__":
    main()




