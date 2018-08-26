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
  return(time.time() - (endSong-beginSong) + (newTime*3))#subtract end and begin to get current place in song, subtract newtime because we've moved forward, multiply by 3 because we fast forward faster than default speed 

def EndForward(beginSong, endSong):
  reMiddle.stop()
  reEnd.play()
  time.sleep(0.5)  
  reEnd.stop()

  newTime = time.time() - endSong
  song.set_time(int((endSong-beginSong)*1000) + int(newTime*3000))
  song.play()
  return(time.time() - (endSong-beginSong) - (newTime*3))#subtract end and begin to get current place in song, subtract newtime because we've moved forward, multiply by 3 because we fast forward faster than default speed

def Pause():
  song.pause()
  pauseTime = time.time()
  return pauseTime

def unPause(pauseTime):
  return(time.time() - (pauseTime - beginSong))
  


beginSong = time.time()
while True:
  song.play()

  continued = input('Major: ')
  if continued =='r' or continued == 'f':
    endSong  = BeginScrub()
    dud_await_input = input('Minor: ')

    if continued == 'r':
      beginSong = EndRewind(beginSong, endSong)

    elif continued == 'f':
      beginSong = EndForward(beginSong, endSong)

  elif continued == 'p':
    pauseTime = Pause()
    continued = input('Paused: ')
    beginSong = unPause(pauseTime)
    song.play()
    if continued =='r' or continued == 'f':
      endSong  = BeginScrub()
      dud_await_input = input('Minor: ')

      if continued == 'r':
        beginSong = EndRewind(beginSong, endSong)

      elif continued == 'f':
        beginSong = EndForward(beginSong, endSong)     
      

#note to solve the lag time between pressing buttons the middle audio file could be rendered with 0.317 second gap at start
#handling for blanks
#playist of music
