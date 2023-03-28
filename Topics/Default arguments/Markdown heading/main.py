def heading(text, head=1):
    if head <= 1:
        head = 1
    elif head > 6:
        head = 6

    return '#'*head + " " + text

#
# print(heading("A"))      # Returns "# A"
# print(heading("A", 3))   # Returns "### A"
# print(heading("A", 1))   # Returns "# A"
# print(heading("A", 0))   # Returns "# A"
# print(heading("A", 10))  # Returns "###### A"
