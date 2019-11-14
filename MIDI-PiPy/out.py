import time
import rtmidi

midiout = rtmidi.MidiOut()

available_ports = midiout.get_ports()

if available_ports:
    mioport = 1
    # midiout.open_port(mioport)
else:
    midiout.open_virtual_port("My virtual output")

note = 36
dirct = 1

while True:
    note_on = [0x90, note, 112]  # channel 1, middle C, velocity 112
    note_off = [0x80, note, 0]
    with midiout:
        midiout.open_port(mioport)
        midiout.send_message(note_on)
        time.sleep(0.0001)
        midiout.send_message(note_off)
        time.sleep(0.0001)
        midiout.close_port()

    if dirct == 1:
        note += 1
    else:
        note -= 1

    if note == 96:
        dirct = 0
    elif note == 36:
        dirct = 1

del midiout
