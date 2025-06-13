sharp_notes_bank = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
flat_notes_bank = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "bb", "b"]

def create_chord(root_note, chord_type):
    """
    Create a chord based on the root note and chord type.
    
    Args:
        root_note (str): The root note of the chord (e.g., "c", "d#", "f").
        chord_type (str): The type of chord (e.g., "major", "minor", "maj7", "min7").
    
    Returns:
        list: A list of notes that make up the chord.
    """
    
