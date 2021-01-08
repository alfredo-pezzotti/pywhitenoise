#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa


fs = 44100  # 44100 samples per second


print("How long should the wav file be in seconds?")
seconds = int(input())

num_samples = fs*seconds
# create the random signal:
samples = np.random.random(size=num_samples)
# Ensure that highest value is in 16-bit range:
audio = samples * (2**15 - 1) / np.max(np.abs(samples))
# Convert to 16-bit data:
audio = audio.astype(np.int16)

# Start playback
play_obj = sa.play_buffer(audio, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()







#num_samples = 10000
#num_bins = 200

#samples = np.random.random(size=num_samples)

# to see an histogram of the created signal:
#plt.hist(samples, num_bins)
#plt.show()

# to see the signal:
#plt.plot(samples)
#plt.show()

#EOF
