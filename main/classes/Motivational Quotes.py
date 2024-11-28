import random
import os

class DailyInspiration:
    def __init__(self, filename='inspirations.txt'):
        self.filename = filename
        self.inspirations = self._load_inspirations()

    def _load_inspirations(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [line.strip() for line in file if line.strip()]
        return []

    def _save_inspirations(self):
        with open(self.filename, 'w') as file:
            file.write('\n'.join(self.inspirations))

    def get_daily_inspiration(self):
        return random.choice(self.inspirations) if self.inspirations else "No inspiration messages available."

    def add_inspiration(self, message):
        self.inspirations.append(message)
        self._save_inspirations()
        print(f'Added: "{message}"')

    def remove_inspiration(self, message):
        if message in self.inspirations:
            self.inspirations.remove(message)
            self._save_inspirations()
            print(f'Removed: "{message}"')
        else:
            print(f'Message not found: "{message}"')

def main():
    app = DailyInspiration()

    while True:
        print("\nMenu:\n1. Get Inspiration\n2. Add Inspiration\n3. Remove Inspiration\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print(f"\nDaily Inspiration: {app.get_daily_inspiration()}")
        elif choice == '2':
            app.add_inspiration(input("Enter a new inspiration: "))
        elif choice == '3':
            app.remove_inspiration(input("Enter the message to remove: "))
        elif choice == '4':
            print("Goodbye!"); break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()