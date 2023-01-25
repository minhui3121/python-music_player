# Student name: Minhui Roh
# McGill ID: 261120462

from note import Note

class Melody:
    """ A class to represent a melody of a song.

    Instance attributes:
    * title: str
    * author: str
    * notes: list
    """
    def __init__(self, filename):
        """ (str) -> NoneType
        Creates an object of type Melody from the file with filename input.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[5])
        1.0 F 4 sharp
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> len(hot_cross_buns.notes)
        17
        >>> print(happy_birthday.notes[10])
        0.5 A 4 natural
        
        >>> tetris = Melody("tetris.txt")
        >>> len(tetris.notes)
        40
        >>> print(tetris.title)
        Tetris
        
        >>> twinkle = Melody("twinkle.txt")
        >>> print(twinkle.author)
        Traditional
        """
        fobj = open(filename, "r")
        line_list = []
        for line in fobj:
            line = line.strip("\n")
            line_list.append(line)
        fobj.close()
        self.title = line_list[0]
        self.author = line_list[1]
        self.notes = []
        line_list = line_list[2 : len(line_list)]
        new_list = []
        i=0
        while i < len(line_list):
            if "false" in line_list[i]:
                new_list.append(line_list[i])
                i += 1
            else:
                first_index = i
                i += 1
                while "true" not in line_list[i]:
                    i += 1
                second_index = i
                for k in range(2):
                    index = first_index
                    while index != second_index + 1:
                        new_list.append(line_list[index])
                        index += 1
                i += 1
        for e in new_list:
            if e.count(" ") == 2:
                duration, pitch, bool_1 = e.split(" ")
                single_note = Note(float(duration), pitch)
                self.notes.append(single_note)
            else: 
                duration, pitch, octave, accidental, bool_1 = e.split(" ")
                single_note = Note(float(duration), pitch, int(octave), accidental.lower())
                self.notes.append(single_note)
            
    def play(self, player):
        """ (Player) -> NoneType
        Plays the melody through speaker using given player. 
        """
        for e in self.notes:
            e.play(player)
        
    def get_total_duration(self):
        """ () -> float
        Returns the total duration of a song as a float
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.get_total_duration()
        8.0
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.get_total_duration()
        15.5
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.get_total_duration()
        24.5
        """
        duration = 0.0
        for e in self.notes:
            duration += e.duration
        return duration
            
    def lower_octave(self):
        """ () -> bool
        Reduces the octave of all notes in the song by 1 and returns True.
        If the octave cannot be reduced, returns False.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.lower_octave()
        True
        >>> tetris.notes[5].octave
        3
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.lower_octave()
        True
        >>> twinkle.notes[5].octave
        3
        """ 
        for e in self.notes:
            if e.octave == 1 and e.pitch != "R":
                return False
        for e in self.notes:
            if e.pitch == "R":
                continue
            e.octave -= 1
        return True

    def upper_octave(self):
        """ () -> bool
        Increases the octave of all notes in the song by 1 and returns True.
        If the octave cannot be increased, returns False.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.upper_octave()
        True
        >>> tetris.notes[5].octave
        5
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.upper_octave()
        True
        >>> twinkle.notes[5].octave
        5
        """
        for e in self.notes:
            if e.octave == 7:
                return False
        for e in self.notes:
            e.octave += 1
        return True
    
    def change_tempo(self, float):
        """ (float) -> NoneType
        Multiplies the duration of each note by a given float.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.change_tempo(0.5)
        >>> hot_cross_buns.get_total_duration()
        4.0
        
        >>> tetris = Melody("tetris.txt")
        >>> tetris.change_tempo(2.0)
        >>> tetris.get_total_duration()
        31.0
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.change_tempo(1.0)
        >>> twinkle.get_total_duration()
        24.5
        """
        for e in self.notes:
            e.duration *= float
