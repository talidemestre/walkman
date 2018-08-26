import vlc
import time

#rewind start
reStart=vlc.MediaPlayer("rewind_begin.wav")

reMiddle = vlc.MediaPlayer("rewind_middle.wav")


reEnd = vlc.MediaPlayer("rewind_end.wav")




song = vlc.MediaPlayer("s2.mp3")

def BeginScrub():
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
  reEnd.stop()
  newTime = time.time() - endSong
  song.set_time(int((endSong-beginSong)*1000) - int(newTime*3000))
  song.play()
  return(time.time() - (endSong-beginSong) + (newTime*3))

def EndForward(beginSong, endSong):
  reMiddle.stop()
  reEnd.play()
  time.sleep(0.5)  
  reEnd.stop()

  newTime = time.time() - endSong
  song.set_time(int((endSong-beginSong)*1000) + int(newTime*3000))
  song.play()
  return(time.time() - (endSong-beginSong) - (newTime*3))
  

beginSong = time.time()
while True:
  song.play()

  continued = input('Major: ')
  if continued =='r' or continued == 'f':
    endSong  = BeginScrub()
    continued = input('Minor: ')

    if continued == 'r':
      beginSong = EndRewind(beginSong, endSong)

    elif continued == 'f':
      beginSong = EndForward(beginSong, endSong)

#note to solve the lag time between pressing buttons the middle audio file could be rendered with 0.317 second gap at start
    


#must handl
