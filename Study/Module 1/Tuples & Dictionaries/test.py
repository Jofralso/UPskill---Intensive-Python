import random

jokes = {
    "knock-knock": [
        ("Knock, knock.", "Who’s there?", "Lettuce.", "Lettuce who?", "Lettuce in, it's cold out here!"),
        ("Knock, knock.", "Who’s there?", "Boo.", "Boo who?", "Don't cry, it's just a joke!"),
    ],
    "one-liner": [
        ("Why don't scientists trust atoms?", "Because they make up everything!"),
        ("Why don't skeletons fight each other?", "They don't have the guts!"),
    ]
}

def generate_joke(category):
    if category in jokes:
        joke_list = jokes[category]
        return random.choice(joke_list)
    else:
        return "Sorry, I don't have any jokes in that category."

category = input("Enter a joke category (knock-knock or one-liner): ")
joke = generate_joke(category)
print("\n".join(joke))
