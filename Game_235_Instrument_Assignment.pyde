# Game 235 Instrument Assignment

# Welcome to the game Instruments.
# To play a sound, please press the left mouse button to play a sound dependent upon where you click on the canvas.
# During start up Coolio - Gansta Paradise will play. Press CNTRL to Pause Gangsta Paradise. Press the UP arrow to play Gangsta Paradise.
# You can also press e, s, j, t, w, g for additional sounds. Press the escape or "1" or "!" to exit the game.
# Its okay if you forget what keys to press as the instructions of what keys to press are also displayed on the screen.

add_library('sound') # add_library used to load a library into a Processing sketch
# https://processing.org/reference/libraries/sound/index.html

isReleased = False
keyEReleased = False

NOTE_MAX_SIZE = 200.0 # All caps denote constant variable.
noteX = []
noteY = []
noteSize = []

keyX = []
keyY = []
keySize = []

keyPress1 = []
keyPress2 = []
keyPressVariable = []

attackTime = 0.001 # 0 volume to sustain level
sustainTime = 0.008 # time at the sustain level
sustainLevel = 0.2 # maximum volume
releaseTime = 0.4 # sustain level to 0 volume

def setup (): # starts
    global osc, env, Gunshot, Explosion7, Scream, Terminator, Wazzup, Coolio, Jason
    size(640,480)
    rectMode(CENTER)
    strokeWeight(.1)
    
    # Sounds imported to processing
    Coolio = SoundFile(this, "Coolio.wav")
    Gunshot = SoundFile(this, "Gunshot.wav") # sound file needs to be in your folder.
    Explosion7 = SoundFile(this, "Explosion7.wav")
    Scream = SoundFile(this, "Scream.wav")
    Jason = SoundFile(this, "Jason.wav")
    Terminator = SoundFile(this, "Terminator.wav")
    Wazzup = SoundFile(this, "Wazzup.wav")
    
    # functions taken from the sound library
    osc = TriOsc(this) # SqrOsc, TriOsc, SawOsc, SinOsc, PulseOsc
    sqr = SqrOsc(this)
    env = Env(this)
    
    # This function plays during startup.
    Coolio.play()
    
def draw(): # update
    # releasing mouse button if pressed once. # if mouse is released previous True statement is false and it prints released.
    global isReleased, osc, attackTime, sustainTime, sustainLevel, releaseTime, keyEReleased, sqr, keySize, releventKeyPressed, keyPress
    background (0)
    
    # --- Logic
    
    if mousePressed:
        isReleased = True
    elif isReleased:
        print("Released")
        # Play a sound
        osc.play()
        osc.freq(mouseX + 100)
        env.play(osc, attackTime, sustainTime, sustainLevel, releaseTime)
        
        #Create a Note Visual
        noteX.append(mouseX)
        noteY.append(mouseY)
        startingNoteSize = 3
        noteSize.append(startingNoteSize)
        
        isReleased = False
    
    # --- Draw
    fill (0,0,0,0) # red, green, blue, alpha
    
        
    for i in range(len(noteX)):
        noteSize[i] += 1
        
        # integer division needs to be a float division or it will equal to 0. 
        # multiplying float adds all integers in numbers.v
        colorAlphaValue = 255 * ((NOTE_MAX_SIZE - noteSize[i])/float(NOTE_MAX_SIZE))
        stroke(mouseX, mouseY, 255, colorAlphaValue) # added mouseX or mouseY to have it depend on the mouse position.
        
        # for each of our note we want to make a note on that spot.
        circle (noteX[i], noteY[i], noteSize[i])
        circle (noteX[i], noteY[i], noteSize[i]/2)
        circle (noteX[i], noteY[i], noteSize[i]/3)
        
    for g in range(len(keyX)):
        keySize[g] += 1
        
        colorAlphaValue = 255 * ((NOTE_MAX_SIZE - keySize[g])/float(NOTE_MAX_SIZE))
        stroke(mouseX, mouseY, 255, colorAlphaValue)
        
        square (keyX[g], keyY[g], keySize[g])
        square (keyX[g], keyY[g], keySize[g]/2)
    
    for e in range(len(keyPress1)):
        keyPressVariable[e] += 1
        
        colorAlphaValue = 255 * ((NOTE_MAX_SIZE - keyPressVariable[e])/float(NOTE_MAX_SIZE))
        stroke(mouseX, mouseY, 255, colorAlphaValue)
        
        ellipse (keyPress1[e], keyPress2[e], keyPressVariable[e], 10)
        ellipse (keyPress1[e], keyPress2[e], keyPressVariable[e]/3, 10)
    
    
    # In game text's
    fill(255)
    text ("Notes: " + str(len(noteX)), 10, 20)
    text ("Press CNTRL to stop Gangsta Paradise.", 10, 35)
    text ("Press W for Wazzup..", 10, 50)
    text ("Press S for Scream.", 10, 65)
    text ("Press J for Jason Theme.", 10, 80)
    text ("Press T for Terminator Theme.", 10, 95)
    text ("Press E for Explosions.", 10, 110)
    text ("Press G for Gun Shots.", 10, 125)
    text ("Press Escape Key to Exit.", 10, 155)
    text ("Key inputted:"+ str(key), 10, 170)

def keyPressed():
    # Extra key to exit by default escape is exit key
    if key == '1' or key == '!':
        exit()
        
        
def keyReleased(): # upon key released so keys cant be hold down.
    relevantKeyPressed = False
    otherArtKeyPress = False
        
    #Stop sounds by keys
    if keyCode == CONTROL:
        Coolio.pause()
    elif keyCode == UP:
        Coolio.play()
        otherArtKeyPress  = True
    
    #Play sounds by keys
    if key == "s" or key == "S":
        Scream.jump(0)
        otherArtKeyPress = True
        
    if key == "e" or key == "E":   
        Explosion7.jump(0)
        otherArtKeyPress = True

    if key == "w" or key == "W":    
        Wazzup.jump(0)
        relevantKeyPressed = True
        
    if key == "j" or key == "J":   
        Jason.jump(0)
        relevantKeyPressed = True
        
    if key == "t" or key == "T":   
        Terminator.jump(0)
        relevantKeyPressed = True
        
    if key == "g" or key == "G":    
        Gunshot.jump(0)
        relevantKeyPressed = True

    if relevantKeyPressed:
        keyX.append(mouseX)
        keyY.append(mouseY)
        startingNoteSize = 3
        keySize.append(startingNoteSize)
        
    if otherArtKeyPress: 
        keyPress1.append(mouseX)
        keyPress2.append(mouseY)
        startingNoteSize = 3
        keyPressVariable.append(startingNoteSize)
