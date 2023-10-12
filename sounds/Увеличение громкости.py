import wave
import struct


def custom_processing(frame, count):
    frame *= count
    if frame <= -32768:
        return -32768
    elif frame >= 32767:
        return 32767
    return frame


custom_factor = 100

with wave.open("in.wav", mode="rb") as source, wave.open("out_processed.wav", mode="wb") as dest:
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))

    newdata = list(map(lambda frame: custom_processing(frame, custom_factor), data))
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes)
