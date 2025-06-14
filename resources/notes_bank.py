sharp_notes_bank = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
flat_notes_bank = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "bb", "b"]

sharp_chords = ["C", "G", "D", "A", "E", "B", "F#", "a", "e", "h", "f#", "c#", "g#"]
flat_chords = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "b", "eb"], 

chords_types = {"min":[0, 3, 7], "maj":[0, 4, 7]}

def define_chord(root_note, chord_type):
    """
    Define a chord based on the root note and chord type.
    
    Args:
        root_note (str): The root note of the chord (e.g., "c", "d#", "f").
        chord_type (str): The type of chord (e.g., "major", "minor", "maj7", "min7").
    
    Returns:
        list: A list of notes that make up the chord.
    """
    if chord_type == "maj":
        root_note_upper = root_note.capitalize()
        if root_note_upper in sharp_chords:
            chord = build_chord(root_note, chord_type, sharp_notes_bank)
        else:
            chord = build_chord(root_note, chord_type, flat_notes_bank)
    else:
        if root_note in sharp_chords:
            chord = build_chord(root_note, chord_type, sharp_notes_bank)
        else:
            chord = build_chord(root_note, chord_type, flat_notes_bank)
    return chord
        
        

def build_chord(root_note, chord_type, bank_of_notes):
    """
    Build a chord based on the root note and chord type using the specified bank of notes.

    Args:
        root_note (str): The root note of the chord (e.g., "c", "d#", "f").
        chord_type (str): The type of chord (e.g., "major", "minor", "maj7", "min7").
    """

    chord_elements = []
    root_note_index = bank_of_notes.index(root_note)
    for element in chords_types[chord_type]:
        if root_note_index + int(element) >= len(bank_of_notes):
            new_index = (root_note_index + element) - len(bank_of_notes)
            chord_elements.append(bank_of_notes[new_index])
        else: 
            chord_elements.append(bank_of_notes[root_note_index + int(element)])
    print("Chord's elements: " + str(chord_elements))
    return chord_elements

    



a = build_chord("a", "maj", sharp_notes_bank)
print(a)
b = define_chord("a", "maj")
print(b)
