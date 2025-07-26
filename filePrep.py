from pydub import AudioSegment

song = AudioSegment.from_wav("note2_mono.wav")

firstsecond = song[:1000]
firstsecond.export("oneSecondNote.wav", format="wav")