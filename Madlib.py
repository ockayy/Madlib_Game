import random

def identify_placeholders(story):
    """
    Identifies placeholders in a given story.

    Parameters:
    - story (str): A story string.

    Returns:
    - set: A set containing identified placeholders.
    """
    placeholders = set()
    for word in story.split():
        # Check if the word contains both "[" and "]" characters
        if "[" in word and "]" in word:
            placeholders.add(word)
    return placeholders

def main():
    # List of stories with placeholders
    stories = [
        "One sunny afternoon, I received a mysterious package at my doorstep. Intrigued by its unusual shape and vibrant color, I cautiously unwrapped it to reveal a(n) [Adjective1] [Noun1]. Confused but excited, I decided to [Verb1] it. To my surprise, the moment I touched it, the room filled with an enchanting glow. The [Adjective2] object transported me to a magical realm where talking animals and floating castles were the norm. It turned out that the mysterious package was a portal to an alternate universe filled with whimsical wonders.",
        "In the heart of the [Adjective1] forest, there stood a magnificent [Noun1]. Legend had it that anyone who dared to [Verb1] through the dense woods would discover a hidden world of enchantment. Curiosity overcoming fear, I embarked on the journey. As I [Verb2] deeper into the forest, the air became filled with the sweet scent of [Adjective2] flowers, and the trees whispered ancient secrets. Suddenly, a friendly [Noun2] appeared, guiding me to a sparkling waterfall that led to a magical realm beyond imagination.",
        "In a bustling city of futuristic skyscrapers, there lived a curious [Noun1] named Robo. Despite being made of [Adjective1] metal, Robo harbored a deep desire to [Verb1] and explore the world beyond circuits and wires. One day, with gears whirring and lights blinking, Robo set out on a grand adventure to [Verb2] the mysteries of the human world. Along the way, Robo encountered [Adjective2] characters, from singing street performers to wise old [Noun2], learning valuable lessons about the beauty of diversity and the power of [Verb3].",
        "In the dusty corner of an old bookstore, I stumbled upon a peculiar [Noun1]: a weathered diary with [Adjective1] pages. As I started to [Verb1] its contents, I discovered that this wasn't an ordinary journal but a magical time-traveling device. With each turn of the page, I was transported to different eras, experiencing the [Adjective2] events of history firsthand. From dancing in the Roaring Twenties to witnessing groundbreaking scientific discoveries, the time-traveling diary became my passport to a kaleidoscope of [Adjective3] adventures.",
        "On the outskirts of the galaxy, there existed a cosmic cafe with an otherworldly menu. Customers could order [Adjective1] dishes like starlight soup and nebula noodles, all served by charming [Noun1]. One day, I decided to [Verb1] the mysterious cafe and taste the intergalactic delights. As I savored each [Adjective2] bite, the walls shimmered with constellations, and the waitstaff danced among the planets. It turned out that the cafe was a gathering place for beings from across the cosmos, creating a [Adjective3] atmosphere of unity and celestial joy."
    ]

    # Randomly select a story from the list
    randStory = random.choice(stories)

    # Identify placeholders in the randomly selected story using the function
    placeholders = identify_placeholders(randStory)

    # List of story names corresponding to the stories
    storyName = ["The Mysterious Package", "The Enchanted Forest Adventure", "The Curious Robot", "The Time-Traveling Diary", "The Galactic Cafe"]

    # Print the selected story name and the story itself for the user
    for i, story in enumerate(stories):
        if story == randStory:
            print("\n" + storyName[i])
            print(story)

    # Take input of Verb, Noun, and Adjective from the user
    for placeholder in placeholders:
        user_input = input(f"Enter {placeholder}: ")
        randStory = randStory.replace(placeholder, user_input)

    # Print the completed story
    print("\nCompleted Story:")
    print(randStory)

# Call the main function to execute the program
main()
