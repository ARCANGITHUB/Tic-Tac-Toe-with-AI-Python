# the list "students" is already defined

# students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]

print([group[0] for group in students for student in group if student == "A"])
