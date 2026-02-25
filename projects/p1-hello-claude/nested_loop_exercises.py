# ================================================================
# Nested Loop Exercises
# Concept: Loops inside loops — working with lists of lists
# ================================================================
# How to use this file:
#   - Read the exercise description
#   - Look at the expected output
#   - Write your code in the space provided
#   - Run the file to check your result
#
# Run with: python nested_loop_exercises.py
# ================================================================


# ================================================================
# EXERCISE 1 — Number Grid (Warm-up)
# ================================================================
# Build a 4x4 grid of numbers and print it.
# Each cell should show: row number x column number
#
# Expected output:
#
#   1  2  3  4
#   2  4  6  8
#   3  6  9  12
#   4  8  12 16
#
# Concepts practiced:
#   - Nested loops with range()
#   - print(value, end="") to stay on the same line
#   - print('') to move to next line after each row
#
# Hint: You need two loops.
#       Outer loop: rows 1 through 4
#       Inner loop: columns 1 through 4
#       Each cell = row * column
# ================================================================

print("=" * 40)
print("EXERCISE 1 — Number Grid")
print("=" * 40)

# Write your code here:

for row in range(1, 5):
    for col in range(1, 5):
        print(row * col, end="  ")
    print('')  # Move to next line after each row


# ================================================================
# EXERCISE 2 — Ticket Status Board
# ================================================================
# You are given a list of tickets. Each ticket is itself a list
# containing: [ticket_id, severity, assignee]
#
# Loop through all tickets and print each field on the same line,
# then move to the next line for the next ticket.
#
# Expected output:
#
#   TKT-001  |  HIGH      |  duane
#   TKT-002  |  LOW       |  marcus
#   TKT-003  |  CRITICAL  |  sarah
#   TKT-004  |  MEDIUM    |  duane
#   TKT-005  |  HIGH      |  marcus
#
# Concepts practiced:
#   - Nested loops on real data (not just numbers)
#   - Accessing items inside inner lists
#   - Formatting output neatly
#
# Hint: The outer loop gives you one ticket (a list of 3 items).
#       The inner loop gives you one field at a time from that ticket.
#       Use print(field, end="  |  ") to separate fields on one line.
#       Use print('') at the end of each ticket to move to next line.
# ================================================================

tickets = [
    ["TKT-001", "HIGH",     "duane"],
    ["TKT-002", "LOW",      "marcus"],
    ["TKT-003", "CRITICAL", "sarah"],
    ["TKT-004", "MEDIUM",   "duane"],
    ["TKT-005", "HIGH",     "marcus"],
]

print("\n" + "=" * 40)
print("EXERCISE 2 — Ticket Status Board")
print("=" * 40)

# Write your code here:

for ticket in tickets:
    for field in ticket:
        print(field, end="  |  ")
    print('')  # Move to next line after each ticket
# ================================================================
# EXERCISE 3 — Find the Critical Tickets
# ================================================================
# You are given a 2D grid of severity levels (a list of lists).
# Each row represents a team. Each item is a ticket severity.
#
# Your job:
#   Loop through the grid and print the location (row, column)
#   of every ticket that is "CRITICAL"
#
# Expected output:
#
#   CRITICAL found at row 0, column 2
#   CRITICAL found at row 1, column 0
#   CRITICAL found at row 2, column 1
#   CRITICAL found at row 2, column 3
#
# Concepts practiced:
#   - Nested loops with enumerate() to track position
#   - Conditionals inside nested loops
#   - Finding specific items in a 2D grid
#
# Hint: Use enumerate() on both loops so you always know
#       which row and which column you are on.
#       if severity == "CRITICAL": print the location
# ================================================================

grid = [
    ["LOW",      "MEDIUM",   "CRITICAL", "LOW"     ],
    ["CRITICAL", "HIGH",     "MEDIUM",   "LOW"     ],
    ["HIGH",     "CRITICAL", "LOW",      "CRITICAL"],
]

print("\n" + "=" * 40)
print("EXERCISE 3 — Find the Critical Tickets")
print("=" * 40)

# Write your code here:

for i, row in enumerate(grid):
    for j, severity in enumerate(row):
        if severity == "CRITICAL":
            print(f"CRITICAL found at row {i}, column {j}")



# ================================================================
# EXERCISE 4 — Build Your Own Shape
# ================================================================
# Design your own picture using 0s and 1s — just like tree.py.
# Then write the nested loops to print it as stars and spaces.
#
# Requirements:
#   - Your picture list must have at least 5 rows
#   - Each row must have at least 7 columns
#   - The 1s must form a recognizable shape (letter, symbol, anything)
#   - Use the exact same loop structure as tree.py
#
# Ideas: the letter D, H, or I  |  a house  |  a rocket  |  an arrow
#
# Concepts practiced:
#   - Designing a 2D grid from scratch
#   - Writing the nested loop pattern yourself without a reference
#   - Understanding how 0s and 1s map to visual output
#
# Hint: Draw your shape on paper with Xs first.
#       Then replace X with 1 and blank with 0.
#       Then write the loops exactly like tree.py.
# ================================================================

print("\n" + "=" * 40)
print("EXERCISE 4 — Build Your Own Shape")
print("=" * 40)

# Define your picture here:
my_picture = [
[1,0,0,0,0,0,1],
[0,1,0,0,0,1,0],
[0,0,1,0,1,0,0],
[0,0,0,1,0,0,0],
[0,0,1,0,1,0,0],
[1,1,0,0,0,1,1]
]

# Write your loops here:
for row in my_picture:
    for pixel in row:
        if pixel == 1:
            print('*', end="  ")
        else:
            print(' ', end="  ")
    print('')  # Move to next line after each row