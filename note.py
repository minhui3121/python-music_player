# Student name: Minhui Roh
# McGill ID: 261120462

import musicalbeeps

class Note:
    """ A class to represent a note.
    
    Instance attributes:
    * duration: float
    * pitch: str
    * octave: int
    * accidental: str
    """
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave=1, accidental="natural"):
        """ (float, str, int, str) -> NoneType
        Creates an object of type Note.
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        
        >>> note = Note(2, "B", 4, "natural")
        Traceback (most recent call last):
        AssertionError: Invalid duration
        
        >>> note = Note(2.0, "B", 4.5, "natural")
        Traceback (most recent call last):
        AssertionError: Invalid octave
        
        >>> note = Note(2.0, 3, 4, "natural")
        Traceback (most recent call last):
        AssertionError: Invalid pitch
        
        >>> note = Note(2.0, "J", 4, "natural")
        Traceback (most recent call last):
        AssertionError: Invalid pitch
        
        >>> note = Note(2.0, "R", 4, 5)
        Traceback (most recent call last):
        AssertionError: Invalid accidental value
        """
        if type(duration) != float or duration <= 0:
            raise AssertionError ("Invalid duration")
        elif type(pitch) != str or pitch not in "ABCDEFGR" or len(pitch) != 1:
            raise AssertionError ("Invalid pitch")
        elif type(octave) != int or octave < 1 or octave > 7:
            raise AssertionError ("Invalid octave")
        elif type(accidental)!= str or (accidental!="sharp" and accidental!="flat" and accidental!="natural"):
            raise AssertionError ("Invalid accidental value")
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
    
    def __str__(self):
        """ () -> str
        Returns the duration, pitch, octave and accidental of a note.
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        
        >>> note = Note(2.0, "R")
        >>> print(note)
        2.0 R 1 natural
        
        >>> note = Note(0.5, "B", 4, "sharp")
        >>> print(note)
        0.5 B 4 sharp
        """
        return str(self.duration) + " " + self.pitch + " " + str(self.octave) + " " + self.accidental
    
    def play(self, player):
        """ (Player) -> NoneType
        Plays the note through speaker using the given player.
        """
        if self.pitch == "R":
            note_str = "pause"
        else:
            note_str = self.pitch + str(self.octave)
            if self.accidental == "sharp":
                note_str += "#"
            elif self.accidental == "flat":
                note_str += "b"
        player.play_note(note_str, self.duration)
    