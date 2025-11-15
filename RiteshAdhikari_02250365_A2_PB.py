# Part B – Sorting Algorithms
# Bubble Sort, Insertion Sort, and Quick Sort with menu system

def bubble_sort(names_list):
    """Alphabetically sort a list of names using the Bubble Sort technique."""
    length = len(names_list)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if names_list[j] > names_list[j + 1]:
                names_list[j], names_list[j + 1] = names_list[j + 1], names_list[j]


def insertion_sort(values):
    """Sort a list of numeric scores in ascending order using Insertion Sort."""
    for i in range(1, len(values)):
        temp = values[i]
        pos = i - 1

        while pos >= 0 and values[pos] > temp:
            values[pos + 1] = values[pos]
            pos -= 1

        values[pos + 1] = temp


def quick_sort(arr, start, end, counter):
    """Quick Sort implementation with recursion count tracking."""
    if start < end:
        counter["steps"] += 1
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1, counter)
        quick_sort(arr, pivot_index + 1, end, counter)


def partition(arr, start, end):
    """Partition helper for Quick Sort using last element as pivot."""
    pivot = arr[end]
    small = start - 1

    for cur in range(start, end):
        if arr[cur] <= pivot:
            small += 1
            arr[small], arr[cur] = arr[cur], arr[small]

    arr[small + 1], arr[end] = arr[end], arr[small + 1]
    return small + 1


def ask_yes_no(question):
    """Ask a yes/no question until the user enters a valid answer."""
    while True:
        answer = input(question).strip().lower()
        if answer in ("y", "n"):
            return answer
        print("Please respond with 'y' or 'n' only.")


def main():
    # Names list for Bubble Sort
    names = [
        "Kado", "Nado", "Zangmo", "Karma", "Lemo", "Karchung",
        "Pema", "Tashi", "Dolkar", "Kinley", "Ritesh", "Yoezer",
        "Lhachen", "Lhazin", "Sangay"
    ]

    # Scores list for Insertion Sort
    scores = [
        78, 45, 92, 67, 88, 54, 73, 82, 91, 59,
        76, 85, 48, 93, 71, 89, 57, 80, 69, 62
    ]

    # Book prices list for Quick Sort
    prices = [
        450, 230, 678, 125, 890, 340, 560, 310,
        710, 620, 470, 380, 410, 540, 290
    ]

    while True:
        print("\n=== Sorting Algorithms Menu ===")
        print("1. Bubble Sort – Student Names")
        print("2. Insertion Sort – Test Scores")
        print("3. Quick Sort – Book Prices")
        print("4. Exit Program")

        user_choice = input("Choose an option: ").strip()

        if user_choice == "1":
            print("\nOriginal Names:")
            print(", ".join(names))
            temp_list = names[:]
            print("Sorting with Bubble Sort...")
            bubble_sort(temp_list)
            print("Sorted Names:")
            print(", ".join(temp_list))

        elif user_choice == "2":
            print("\nOriginal Scores:")
            print(", ".join(map(str, scores)))
            sorted_scores = scores[:]
            print("Sorting with Insertion Sort...")
            insertion_sort(sorted_scores)
            print("Sorted Scores:")
            print(", ".join(map(str, sorted_scores)))

            print("\nTop 5 Scores:")
            for rank, score in enumerate(sorted(sorted_scores, reverse=True)[:5], start=1):
                print(f"{rank}. {score}")

        elif user_choice == "3":
            print("\nOriginal Book Prices:")
            print(", ".join(map(str, prices)))
            price_copy = prices[:]
            count = {"steps": 0}
            print("Sorting with Quick Sort...")
            quick_sort(price_copy, 0, len(price_copy) - 1, count)
            print("Sorted Book Prices:")
            print(", ".join(map(str, price_copy)))
            print("Total Recursive Calls:", count["steps"])

        elif user_choice == "4":
            print("Exiting… Thank you for using the program!")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")
            continue

        again = ask_yes_no("Perform another sorting operation? (y/n): ")
        if again == "n":
            print("Goodbye! Thanks for using the sorting program.")
            break


if __name__ == "__main__":
    main()
