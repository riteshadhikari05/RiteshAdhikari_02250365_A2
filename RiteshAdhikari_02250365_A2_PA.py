# Part A – Search Algorithms
# Linear Search and Binary Search to locate student IDs and scores

def linear_lookup(data_list, key):
    """Scan the list from start to end to find a matching item."""
    checks = 0
    for index, item in enumerate(data_list):
        checks += 1
        if item == key:
            return index + 1, checks  # return 1-based index
    return -1, checks


def binary_lookup(sorted_list, key):
    """Use binary search on a sorted list to locate the key value."""
    left, right = 0, len(sorted_list) - 1
    checks = 0

    while left <= right:
        mid = (left + right) // 2
        checks += 1

        if sorted_list[mid] == key:
            return mid + 1, checks
        elif sorted_list[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1, checks


def ask_yes_no(question):
    """Keep asking the user until they type 'y' or 'n'."""
    while True:
        answer = input(question).strip().lower()
        if answer in ('y', 'n'):
            return answer
        print("Please enter 'y' or 'n' only.")


def main():
    id_list = [
        1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012,
        1011, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021
    ]

    score_list = [
        45, 52, 58, 63, 67, 72, 75, 78, 82, 85,
        88, 90, 92, 95, 98, 99, 100, 102, 105, 110
    ]

    while True:
        print("\n=== Search Menu ===")
        print("1. Linear Search (Student ID)")
        print("2. Binary Search (Score)")
        print("3. Exit Program")

        option = input("Choose an option: ").strip()

        if option == '1':
            # Linear search block
            print("\nSearching Student IDs:", id_list)
            try:
                user_id = int(input("Enter the Student ID to locate: "))
            except ValueError:
                print("Invalid entry. Enter a valid integer.")
                continue

            position, attempts = linear_lookup(id_list, user_id)

            if position != -1:
                print(f"✓ Student ID {user_id} found at position {position}. Comparisons: {attempts}")
            else:
                print(f"✗ Student ID {user_id} not found. Comparisons: {attempts}")

        elif option == '2':
            # Binary search block
            print("\nAvailable Scores (sorted):", score_list)
            try:
                user_score = int(input("Enter the score to locate: "))
            except ValueError:
                print("Invalid entry. Enter a valid integer.")
                continue

            position, attempts = binary_lookup(score_list, user_score)

            if position != -1:
                print(f"✓ Score {user_score} located at position {position}. Comparisons: {attempts}")
            else:
                print(f"✗ Score {user_score} not found. Comparisons: {attempts}")

        elif option == '3':
            print("Exiting program… Goodbye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, or 3.")
            continue

        # Ask user if they want to continue
        repeat = ask_yes_no("Do you want to perform another search? (y/n): ")
        if repeat == 'n':
            print("Thanks for using the search tool!")
            break


if __name__ == "__main__":
    main()
