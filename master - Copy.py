import vlc
import time

#rewind start
reStart=vlc.MediaPlayer("rewind_begin.wav")
reMiddle = vlc.MediaPlayer("rewind_middle.wav")
reEnd = vlc.MediaPlayer("rewind_end.wav")

song = vlc.MediaPlayer("s2.mp3")

def BeginRewind():
  endSong=time.time()
  song.pause()
  reStart.play()
  time.sleep(0.317)
  reMiddle.play()
  reStart.stop()
  return (endSong)

def EndRewind(beginSong, endSong):  
  reMiddle.stop()
  reEnd.play()
  time.sleep(0.5)
  song.play()
  reEnd.stop()
  song.set_time(int((endSong-beginSong)*1000))


beginSong = time.time()
song.play()

continued = input()
endSong  = BeginRewind()

continued = input()
EndRewind(beginSong, endSong)
