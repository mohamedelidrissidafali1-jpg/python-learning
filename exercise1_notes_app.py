# Note-taking application
import os
from datetime import datetime

NOTES_FILE = "notes.txt"

def save_note(note):
    """Save a note with timestamp"""
    try:
        with open(NOTES_FILE, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {note}\n")
        print("✓ Note saved!")
    except Exception as e:
        print(f"Error saving note: {e}")

def view_all_notes():
    """Display all notes"""
    if not os.path.exists(NOTES_FILE):
        print("No notes yet!")
        return
    
    try:
        with open(NOTES_FILE, "r") as file:
            notes = file.readlines()
            if len(notes) == 0:
                print("No notes yet!")
            else:
                print("\n--- Your Notes ---")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
    except Exception as e:
        print(f"Error reading notes: {e}")

def clear_all_notes():
    """Delete all notes"""
    try:
        with open(NOTES_FILE, "w") as file:
            pass  # Just opens and closes, clearing content
        print("✓ All notes cleared!")
    except Exception as e:
        print(f"Error clearing notes: {e}")

def search_notes(keyword):
    """Search for notes containing keyword"""
    if not os.path.exists(NOTES_FILE):
        print("No notes to search!")
        return
    
    try:
        with open(NOTES_FILE, "r") as file:
            matching_notes = []
            for note in file:
                if keyword.lower() in note.lower():
                    matching_notes.append(note.strip())
        
        if len(matching_notes) == 0:
            print(f"No notes found containing '{keyword}'")
        else:
            print(f"\n--- Notes containing '{keyword}' ---")
            for note in matching_notes:
                print(f"- {note}")
    except Exception as e:
        print(f"Error searching notes: {e}")

def delete_note(note_number):
        try:
            note_number = int(note_number) 
        except ValueError:
            print("Please enter a valid number!")
            return
        if not os.path.exists(NOTES_FILE):
            print("No notes to delete!")
            return 
        try:
            with open(NOTES_FILE, "r") as file:
                notes = file.readlines()
                if note_number > len(notes) or note_number < 1:
                    print("Invalid note number!")
                    return 
                del notes[note_number - 1]
            with open(NOTES_FILE, "w") as file:
                file.writelines(notes)
            print("✓ Note deleted!")
        except Exception as e:
            print(f"Error deleting note: {e}")

            
def backup_notes():

    if not os.path.exists(NOTES_FILE):
        print("No notes to backup!")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    backup_file = (f"notes_backup_{today}.txt")  

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines() 

    with open(backup_file, "w") as file:
        file.writelines(notes)  

    print(f"✓ Backup created: {backup_file}")  

def count_notes():

    if not os.path.exists(NOTES_FILE):
        print("No notes found!")
        return

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()  

    total = len(notes) 

    print(f"Total notes: {total}")   

def show_today_notes():

    if not os.path.exists(NOTES_FILE):
        print("No notes found!")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()

    print("\n--- Notes from today ---")

    for note in notes:
        if today in note:
            print(note.strip())        




# Main menu
while True:
    print("\n=== Note-Taking App ===")
    print("1. Add note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Clear all notes")
    print("5. Delete a note")
    print("6. Backup notes")
    print("7. Count notes")
    print("8. Show today's notes")
    print("9. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        note = input("Enter your note: ")
        save_note(note)
    
    elif choice == "2":
        view_all_notes()
    
    elif choice == "3":
        keyword = input("Search for: ")
        search_notes(keyword)
    
    elif choice == "4":
        confirm = input("Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            clear_all_notes()
    
    elif choice == "5":
        view_all_notes()
        try:
            note_number = int(input("Enter the number of the note to delete: "))
            delete_note(note_number)
        except ValueError:
            print("Please enter a valid number.")
    
    
    elif choice == "6":
        backup_notes()

    
    elif choice == "7":
        count_notes()

    elif choice == "8":
        show_today_notes()

    elif choice == "9":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")