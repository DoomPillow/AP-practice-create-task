"""
    The program lets you store and read notes.
    The function `dothething()` is being called on line 29
"""

notes = {
    "drink water": "remember to drink water eventually.",
    "Dubloons": "The treasure is hidden at the coords 44.5123° N, 64.2949° W.",
}

def dothething(response):
    match(response):
        case "A":
            notes[input("Type the title of your new note")] = input("Type out the content of your new note:")
        case "R":
            for note in notes:
                print(f" - {note} : {notes[note]}")
            del notes[input("Type the title of the note you want to remove: ")]
        case "Q":
            for note in notes:
                print(f" - {note} : {notes[note]}")
            return False
    return True


keepgoing = True
while keepgoing == True:
    print("do you want to add a note, remove a note, or quit? A/R/Q")
    keepgoing = dothething(input("respond here:"))
