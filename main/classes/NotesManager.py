import os


class NotesManager:
    def __init__(self, student_id, filename_prefix='notes_'):
        self.student_id = student_id
        self.filename = f"{filename_prefix}{self.student_id}.txt"
        self.notes = self.load_notes()

    def load_notes(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            content = file.read().strip().split('\n\n')
            return [self.parse_note(note) for note in content if note.strip()]

    def parse_note(self, note):
        lines = note.strip().splitlines()
        title = lines[0].strip()
        content = "\n".join(lines[2:]).strip()
        return {'title': title, 'content': content}

    def save_notes(self):
        with open(self.filename, 'w') as file:
            for index, note in enumerate(self.notes):
                file.write(f"Note: {note['title']}\n")
                file.write("------------\n")
                file.write(f"{note['content']}\n\n")

    def add_note(self, title, content):
        if self.is_title_duplicate(title):
            print(f"Note with title '{title}' already exists.")
            return

        self.notes.append({'title': title, 'content': content})
        self.save_notes()
        print(f"Note '{title}' added successfully.")

    def is_title_duplicate(self, title):
        return any(note['title'] == title for note in self.notes)

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return

        for index, note in enumerate(self.notes):
            print(f"{note['title']}\n   Content: {note['content']}\n")

    def edit_note(self, index, new_title, new_content):
        if self.is_valid_index(index):
            self.notes[index]['title'] = new_title
            self.notes[index]['content'] = new_content
            self.save_notes()
            print(f"Note '{new_title}' updated successfully.")
        else:
            print("Invalid note index.")

    def remove_note(self, index):
        if self.is_valid_index(index):
            removed_note = self.notes.pop(index)
            self.save_notes()
            print(f"Note '{removed_note['title']}' removed successfully.")
        else:
            print("Invalid note index.")

    def is_valid_index(self, index):
        return 0 <= index < len(self.notes)


def main():
    student_id = input("Enter your student ID: ")
    notes_manager = NotesManager(student_id)

    while True:
        print("\nOptions:")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Edit Note")
        print("4. Remove Note")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter the note title: ")
            content = input("Enter the note content: ")
            notes_manager.add_note(title, content)

        elif choice == '2':
            notes_manager.view_notes()

        elif choice == '3':
            notes_manager.view_notes()
            index = int(input("Enter the note number to edit: ")) - 1
            new_title = input("Enter the new title: ")
            new_content = input("Enter the new content: ")
            notes_manager.edit_note(index, new_title, new_content)

        elif choice == '4':
            notes_manager.view_notes()
            index = int(input("Enter the note number to remove: ")) - 1
            notes_manager.remove_note(index)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose again.")
