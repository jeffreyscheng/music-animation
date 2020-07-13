import music21
from wave import Wave

def get_dissonance_of_chord(chord_kind: str):
    chord = music21.harmony.ChordSymbol(root='C', kind=chord_kind)
    pitches = chord.pitches
    wave = Wave([p.frequency for p in pitches])
    print(wave.period_multiple)


# get_dissonance_of_chord("perfect-fifth")
# get_dissonance_of_chord("major")
# get_dissonance_of_chord("minor")
# get_dissonance_of_chord("dominant-seventh")
get_dissonance_of_chord("major-seventh")
# get_dissonance_of_chord("minor-seventh")
# get_dissonance_of_chord("diminished-seventh")
# get_dissonance_of_chord("half-diminished-seventh")