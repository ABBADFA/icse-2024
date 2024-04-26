def calculate_percentage(total_marks):
    total_possible_marks = 500  # Assuming each subject is out of 100 marks
    percentage = (total_marks / total_possible_marks) * 100
    return percentage

def main():
    print("\033[1;32mAssalamualaikum Shamsians... Abbad is here..BEST OF LUCK\033[0m")  # Green color for the welcome message
    print("\033[1;34mPlease enter the marks for your top five subjects.\033[0m")  # Blue color for the instruction

    marks = []
    for i in range(5):
        subject_name = input("\033[1;36mEnter the marks for subject {}: \033[0m".format(i+1))  # Cyan color for input prompt
        marks.append(int(subject_name))

    total_marks = sum(sorted(marks, reverse=True)[:5])  # Sum of top five marks
    percentage = calculate_percentage(total_marks)

    print("\n\033[1;35mTotal Marks: {}\033[0m".format(total_marks))  # Magenta color for total marks
    print("\033[1;33mPercentage: {:.2f}%\033[0m".format(percentage))  # Yellow color for percentage
    print("\033[1;31mCONGRATULATIONS FROM ABBAD\033[0m")  # Red color for congratulatory message

if __name__ == "__main__":
    main()
