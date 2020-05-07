import random


def hangman():
    word = random.choice(
        ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes",
         "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar",
         "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb",
         "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex",
         "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord",
         "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby",
         "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip",
         "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot",
         "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey",
         "jogging", "joking", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte",
         "kiosk", "kitsch", "kiwifruit","klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz",
         "microwave", "mnemonic", "mystify", "naphtha","nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo",
         "phlegm", "pixel", "pizazz", "pneumonia", "polka","pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum",
         "razzmatazz", "rhubarb", "rhythm", "rickshaw","schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths",
         "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz",
         "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip",
         "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy",
         "waxy", "wellspring", "wheezy", "whiskey", "whizzing""whomever", "wimpy", "witchcraft", "wizard", "woozy",
         "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag",
         "zigzagging", "zilch", "zipper", "zodiac", "zombie"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""
        if main == word:
            print(main)
            print("You Win!")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print(" ----------- ")
            if turns == 8:
                print("8 turns left")
                print(" ----------- ")
                print("      O      ")
            if turns == 7:
                print("7 turns left")
                print(" ----------- ")
                print("      O      ")
                print("      |      ")
            if turns == 6:
                print("6 turns left")
                print(" ----------- ")
                print("      O      ")
                print("      |      ")
                print("     /       ")
            if turns == 5:
                print("5 turns left")
                print(" ----------- ")
                print("      O      ")
                print("      |      ")
                print("     / \     ")
            if turns == 4:
                print("4 turns left")
                print(" ----------- ")
                print("    \ O      ")
                print("      |      ")
                print("     / \     ")
            if turns == 3:
                print("3 turns left")
                print(" ----------- ")
                print("    \ O /    ")
                print("      |      ")
                print("     / \     ")
            if turns == 2:
                print("2 turns left")
                print(" ----------- ")
                print("    \ O /|   ")
                print("      |      ")
                print("     / \     ")
            if turns == 1:
                print("1 turn left")
                print("Last breaths counting, Take care")
                print(" ----------- ")
                print("    \ O_|/   ")
                print("      |      ")
                print("     / \     ")
            if turns == 0:
                print("You Loose")
                print("You killed the kind man")
                print(" ----------- ")
                print("      O_|   ")
                print("     /|\      ")
                print("     / \     ")
                print("The word is {}".format(word))
                break


name = input("Enter you name: ")
print("Welcome ", name)
print("--------------------------------------------------")
print("Try to guess the word in less than 10 tries")
hangman()
