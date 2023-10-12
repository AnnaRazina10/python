import wave
import struct

custom_factor = 2

with wave.open("in.wav", mode="rb") as source, wave.open("out_processed.wav", mode="wb") as dest:
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = data[::custom_factor]
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
