class Stats:
    """Keeping track of the notes you play.
    """

    notes_playing = []     #array to track midi notes with on/off value
    MAX_MIDI_NOTES = 128    #number of midi notes available
    SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    def __init__(self):
        """Initialise the class and set variables.
        """
        self.notes_playing = [0 for x in range(0,self.MAX_MIDI_NOTES)]

    def _check_note_range(self, midinumber):
        """Helper function to check if midinumber is valid.
        
        :param int midinumber: the midi not number to check
        :return boolean: True if succesful
        """
        if (midinumber < 0 and midinumber >self.MAX_MIDI_NOTES):
            raise  TypeError("Invalid midi number")
        return True
    
    def note_on(self, midinumber):
        """Register the note with midinumber to on.
        
        :param int midinumber: the midinumber of the note being played
        """
        self._check_note_range(midinumber)
        self.notes_playing[midinumber] += 1

    def print_stats(self):
        """Print the statistics of the notes played thus far.
        """
        notes_per_scale = len(self.SCALE)
        for i, note in enumerate(self.notes_playing):
            print("Note {0:>3} ({1:>2}{2:<2}):".format(i, self.SCALE[i%notes_per_scale],i//notes_per_scale),end="")
            print("x" * self.notes_playing[i], end="")
            print(" ({0})".format(self.notes_playing[i]))

def main():
    stats = Stats()
    stats.note_on(5)
    stats.note_on(15)
    stats.note_on(25)
    stats.note_on(35)
    stats.note_on(45)
    stats.note_on(55)
    stats.note_on(65)
    stats.note_on(75)
    stats.note_on(85)
    stats.note_on(95)
    stats.note_on(105)
    for i in range(10):
        stats.note_on(115)
    for i in range(20):
        stats.note_on(116)
    for i in range(17):
        stats.note_on(117)
    stats.print_stats()

if __name__ == '__main__':
    main()
