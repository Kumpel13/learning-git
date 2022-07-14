shopping_list = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for key, value in shopping_list.items():
    value = [i.capitalize() for i in value]
    key = key.capitalize()
    print(f"Idę do {key}, kupuję tu następujące rzeczy: {value}")

x = len(shopping_list["piekarnia"]) + len(shopping_list["warzywniak"])

print(f"W sumie kupuję {x} produktów")

for i in range (1,29):
    if i % 2 ==0:
        print(i)
