import cmath
import numpy as np
import matplotlib.pyplot as plt
import threading

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.midi import fluidsynth

from time import sleep

############################################
### HYPERPARAMETERS
count = 0
precision = 2000
pixel = 800
ratio = (int) (pixel/400)
# interesting center (-1.41, 0), (-0.7746806106269039, -0.1374168856037867)
xcenter = -0.7746806106269039
ycenter = -0.1374168856037867

#############################################
### FUNCTIONS

def mandelbrot(c):
    global count, precision
    count = 0
    z = complex(0, 0)
    z = z * z + c
    for i in range(2000):
        z = z * z + c
        if abs(z) > 4:
            count = i
            return False
    count = i
    return True

### method to play and stop notes in the container, used for multithreading
def play():
    global n, n_1, n_2
    for x in range(len(n)):
        note, note_1, note_2 = n[x], n_1[x], n_2[x]
        fluidsynth.play_Note(note, 1, note.velocity)
        fluidsynth.play_Note(note_2, 2, note_2.velocity)
        fluidsynth.play_Note(note_1, 3, note_1.velocity)
        sleep(.3)

    sleep(3)
    for x in range(len(n)):
        fluidsynth.stop_Note(n[x])
        sleep(.2)
        fluidsynth.stop_Note(n_1[x])
        sleep(.2)
        fluidsynth.stop_Note(n_2[x])
        sleep(.2)

### switches used to select zone in the picture and note to be played
def switch(argument):
    switcher = {
        1: ["F", 80, 80],
        2: ["G", 180, 80],
        3: ["A", 280, 80],
        4: ["Bb", 280, 180],
        5: ["C", 280, 280],
        6: ["D", 180, 280],
        7: ["E", 80, 280],
        8: ["F", 80, 180],
    }
    return switcher.get(argument)

def switch_secondary(argument):
    switcher = {
        1: ["Db", 340, 340],
        2: ["Eb", 381, 340],
        3: ["F", 421, 340],
        4: ["Gb", 421, 381],
        5: ["Ab", 421, 421],
        6: ["Bb", 381, 421],
        7: ["C", 340, 421],
        8: ["Db", 340, 381],
    }
    return switcher.get(argument)

###############################################
### START of main 

# create NoteContainer
n = NoteContainer()
n_1 = NoteContainer()
n_2 = NoteContainer()

# initialize synth
fluidsynth.init("/usr/share/sounds/sf2/FluidR3_GM.sf2", "alsa")
fluidsynth.set_instrument(1,108)
fluidsynth.set_instrument(2,53) 
fluidsynth.set_instrument(3,112)

for step in range(16, 100):
    """ fluidsynth.play_Note(64, 0, 100)
    sleep(1)
    fluidsynth.stop_Note(64, 0) """
    print("zoom x", 2**step)
    rate = 2**step
    amin = xcenter - 2/rate
    amax = xcenter + 2/rate
    aoffset = 0
    bmin = ycenter - 2/rate
    bmax = ycenter + 2/rate
    boffset = 0

    if amin < 0:
        aoffset = -amin
    else:
        aoffset = -amin

    if bmin < 0:
        boffset = -bmin
    else:
        boffset = -bmin

    M = np.zeros((pixel+1, pixel+1))
    a = np.linspace(amin, amax, pixel)
    b = np.linspace(bmin, bmax, pixel)

    for i in a:
        for j in b:
            mandelbrot(complex(i, j))
            M[(int)((j + boffset) * (100*ratio*rate)), (int)
              ((i + aoffset) * (100*ratio*rate))] = count

    # empty containers for new notes 
    n.empty()
    n_1.empty()
    n_2.empty()

    # determine notes to be put in the container
    max_volume = 0
    min_volume = cmath.inf

    ### primary instrument
    for case in range(1,8):
        arr = switch(case)
        note_name = arr[0]
        x_offset = arr[1]
        y_offset = arr[2]
        sum = 0
        for x in range(40):
            for y in range(40):
                sum += M[(x_offset + x)*ratio, (y_offset + y)*ratio]

        if sum < min_volume:
            min_volume = sum 
        if sum > max_volume:
            max_volume = sum
        note = Note(note_name)
        note.velocity = sum
        note.channel = 1
        n.add_note(note)
        note.channel = 2
        n_2.add_note(note)
    

    precision = (max_volume/1600)/127
    scale = 1600*precision

    for x in range(len(n)):
        n[x].velocity = ((n[x].velocity-min_volume)/(max_volume-min_volume))*127
        if n[x].velocity<129 and n[x].velocity>127:
            n[x].velocity=127


    ### secondary instrument
    max_volume = 0
    min_volume = cmath.inf

    for case in range(1,8):
        arr = switch_secondary(case)
        note_name = arr[0]
        x_offset = arr[1]
        y_offset = arr[2]
        sum = 0
        for x in range(40):
            for y in range(40):
                sum += M[(x_offset + x), (y_offset + y)]

        if sum < min_volume:
            min_volume = sum 
        if sum > max_volume:
            max_volume = sum
        note = Note(note_name)
        note.velocity = sum
        note.channel = 3
        n_1.add_note(note)
    

    precision = (max_volume/1600)/127
    scale = 1600*precision

    for x in range(len(n)):
        n_1[x].velocity = ((n_1[x].velocity-min_volume)/(max_volume-min_volume))*127
        if n_1[x].velocity<129 and n_1[x].velocity>127:
            n_1[x].velocity=127


    plt.figure(figsize=(15,15))

    
    plt.imshow(M, cmap='gist_ncar_r', extent=(amin, amax, bmin, bmax))
    
    plt.axis('off')

    # if we want to save the picture
    #plt.savefig('mandelbrot_images_2/mandelbrot_zoom_acc10000_{}.svg'.format(2**step), format='svg', dpi=1200)

    # thread to play music at the same time as plotting
    music_thread = threading.Thread(target=play)
    music_thread.start()

    plt.show(block=False)
    plt.pause(3)
    plt.close()
