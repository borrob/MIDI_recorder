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

    def print_stats_horizontal(self):
        """Print the stats in a bar graph.
        """
        max_hits = max(self.notes_playing)
        for i in range(max_hits):
            j = max_hits - i
            printline = [" " if x < j else "x" for x in self.notes_playing]
            print("".join(printline))

    def print_header(self):
        """Print a header line.
        
        This should help you to navigate between midinumbers.
        """
        print(" 1   5    10   15   20   25   30   35   40   45   50   55   " \
             +"60   65   70   75   80   85   90   95   100  105  110  115  " \
             +"120  125")
        print("C0   F0   A#0  D#1  G#1  C#2  F#2  B2   E3   A3   D4   G4   " \
             +"C5   F5   A#5  D#6  G#6  C#7  F#7  B7   E8   A8   D9   G9   " \
             +"C10  F10")
        print("_|___|____|____|____|____|____|____|____|____|____|____|____" \
             +"|____|____|____|____|____|____|____|____|____|____|____|____" \
             +"|____|__")

    def print_footer(self):
        """Print a footer line.
        
        This should help you to navigate between midinumbers.
        """
        print("_ ___ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____" \
             +" ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____" \
             +" ____ __")
        print(" |   |    |    |    |    |    |    |    |    |    |    |    " \
             +"|    |    |    |    |    |    |    |    |    |    |    |    " \
             +"|    |  ")
        print(" 1   5    10   15   20   25   30   35   40   45   50   55   " \
             +"60   65   70   75   80   85   90   95   100  105  110  115  " \
             +"120  125")
        print("C0   F0   A#0  D#1  G#1  C#2  F#2  B2   E3   A3   D4   G4   " \
             +"C5   F5   A#5  D#6  G#6  C#7  F#7  B7   E8   A8   D9   G9   " \
             +"C10  F10")

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
    stats.print_header()
    stats.print_stats_horizontal()
    stats.print_footer()

if __name__ == '__main__':
    main()
