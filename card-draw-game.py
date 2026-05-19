import random

cards = {
        1: ("------------",
            "|     1    |",
            "____________"),
        2: ("------------",
            "|     2    |",
            "____________"),
        3: ("------------",
            "|     3    |",
            "____________"),
        4: ("------------",
            "|     4    |",
            "____________"),
        5: ("------------",
            "|     5    |",
            "____________")
}

total = 0
showcase = []

hits = int(input("How many cards would you like to hit: "))

for hit in range(hits):
    showcase.append(random.randint(1,5))

for hit in range(hits):
    for line in cards.get(showcase[hit]):
       print(line)
    print()

#for line in range(3):                                ------- Cards show horizontally if activated.
#    for hit in showcase:
#       print(cards.get(hit)[line], end="")
#    print()
for hit in showcase:
    total += hit

print(f"total: {total}")
