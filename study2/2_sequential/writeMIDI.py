# writeMIDI.py
# version 2

import music21 as m21

def writeMIDI(key,instr,bpm,notes,fname):

    # start stream
    stream = m21.stream.Stream()

    # Add tempo to stream
    bpm = m21.tempo.MetronomeMark(number = bpm)
    stream.append(bpm)

    # Add key to stream
    k = m21.key.Key(key)
    stream.append(k)

    # Add instrument
    ins = m21.instrument.fromString(instr)
    stream.append(ins)

    # Add notes to stream at different offsets
    for tup in notes:
        note = m21.note.Note(tup[0])
        offset = tup[1]
        note.quarterLength = tup[2]
        note.volume.velocity = tup[3]
        stream.insert(offset,note)

    # convert stream to midi and write out
    mf = m21.midi.translate.streamToMidiFile(stream)
    mf.open(fname+'.mid', 'wb')
    mf.write()