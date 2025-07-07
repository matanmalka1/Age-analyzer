from services.api_services import get_data_with_headers
from utils.parser import save_response_to_file, load_responses_from_file, filter_by_name, average_age, sort_by_age, get_last_entries
from utils.excel_export import export_to_excel


def show_menu():
     print("\n--- Menu ---")
     print("1.Search age by name ")
     print("2.View all data ")
     print("3.Filter by name ")
     print("4.Average age ")
     print("5.Last five entries ")
     print("6.Sort by high age to low age ")
     print("7.Export to excel")
     print("8.Exit the program")

def main():
     while True:
          show_menu()
          choice = input("Enter your choice (1-8): ")

          if choice == "1":
               name = input("Enter your name: ").lower()
               data = get_data_with_headers(name)
               if data:
                    print(data)
                    print(save_response_to_file(data))


          elif choice == "2":
               data = load_responses_from_file()
               print(f"\nLoaded {len(data)} entries:\n")
               for entry in data:
                    print(entry)

          elif choice == "3":
               data = load_responses_from_file()
               name = input("Enter name to filter: ")
               matches = filter_by_name(name, data)
               if matches:
                    print(f"Matches found for {name}:")
                    for m in matches:
                         print(m)

          elif choice == "4":
               data = load_responses_from_file()
               avg = average_age(data)
               print(f"Average age is: {avg}")

          elif choice == "5":
               data = load_responses_from_file()
               recent = get_last_entries(data)
               print("Last 5 entries:")
               for record in recent:
                    print(record)

          elif choice == "6":
               data = load_responses_from_file()
               sorted_data = sort_by_age(data)
               print("Sorted by age (high to low) desc:")
               for record in sorted_data:
                    print(record)

          elif choice == "7":
               data = load_responses_from_file()
               export_to_excel(data)

          elif choice == "8":
               print("Thank you goodbye!")
               break
          else:
               print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# checkpoint checkpoint