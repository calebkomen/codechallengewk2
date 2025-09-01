# Alternative: Separate functions for each task

def task1_list_sum():
    """Task 1: List of integers and their sum"""
    print("\n1. LIST OF INTEGERS AND SUM")
    int_list = []
    n = int(input("How many integers would you like to enter? "))
    
    for i in range(n):
        num = int(input(f"Enter integer {i+1}: "))
        int_list.append(num)
    
    print(f"Your list: {int_list}")
    print(f"Sum of integers: {sum(int_list)}")

def task2_book_tuple():
    """Task 2: Tuple of favorite books"""
    print("\n2. FAVORITE BOOKS")
    favorite_books = (
        "To Kill a Mockingbird",
        "1984",
        "The Great Gatsby",
        "Pride and Prejudice",
        "The Catcher in the Rye"
    )
    
    print("My favorite books:")
    for book in favorite_books:
        print(f"• {book}")

def task3_person_dict():
    """Task 3: Dictionary for person information"""
    print("\n3. PERSON INFORMATION")
    person = {}
    
    person['name'] = input("Enter your name: ")
    person['age'] = int(input("Enter your age: "))
    person['favorite_color'] = input("Enter your favorite color: ")
    
    print("\nPerson information:")
    for key, value in person.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

def task4_set_operations():
    """Task 4: Sets with common elements"""
    print("\n4. SET OPERATIONS")
    set1 = set()
    set2 = set()
    
    print("Creating first set:")
    n1 = int(input("How many integers for set 1? "))
    for i in range(n1):
        num = int(input(f"Enter integer {i+1} for set 1: "))
        set1.add(num)
    
    print("\nCreating second set:")
    n2 = int(input("How many integers for set 2? "))
    for i in range(n2):
        num = int(input(f"Enter integer {i+1} for set 2: "))
        set2.add(num)
    
    common_elements = set1.intersection(set2)
    print(f"\nSet 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Common elements: {common_elements}")

def task5_odd_length_words():
    """Task 5: Words with odd number of characters"""
    print("\n5. WORDS WITH ODD NUMBER OF CHARACTERS")
    words = ['python', 'java', 'javascript', 'c', 'ruby', 'html', 'css', 'sql']
    
    print(f"Original word list: {words}")
    
    # List comprehension to filter words with odd number of characters
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    
    print(f"Words with odd number of characters: {odd_length_words}")

# Run all tasks
if __name__ == "__main__":
    print("=" * 50)
    print("PYTHON DATA STRUCTURES PROGRAM")
    print("=" * 50)
    
    task1_list_sum()
    task2_book_tuple()
    task3_person_dict()
    task4_set_operations()
    task5_odd_length_words()