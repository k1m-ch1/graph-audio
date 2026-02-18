import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation
import sounddevice as sd
import soundfile as sf
import argparse

parser = argparse.ArgumentParser(description="simply renders a graph of an audio signal in the time domain and the frequency domain")

parser.add_argument("--input", 
                    "-i",
                    help="Audio input as a lossless audio format (flac or wav etc)")

parser.add_argument("--output",
                    "-o",
                    help="The name of the output of the audio file (it's an mp4 video)")

def main():
    args = parser.parse_args()
    data, f_s = sf.read(args.input)
    FPS = 30
    fig, ax = plt.subplots(nrows = 1, ncols = 2,
                          figsize=(16, 9));

    FPS = 30
    CHUNK = int(f_s * (1/FPS))
    #total_duration = len(data) / f_s
    TOTAL_FRAMES = len(data)// CHUNK
    print(CHUNK)
    #print(total_duration)
    print(TOTAL_FRAMES)
    line_t, = ax[0].plot([], [])
    ax[0].set_ylim(-1, 1)
    line_f, = ax[1].plot([], [])

    # to calculate ylim, consider that the signal will be comprised of a maximum of f_s/2 waves, each of which has a maximum amplitude of 1, so y will have a maximum value of f_s/2 which is approximately 20000, take the log of that to get log(20000) = log (2 * (10**4)) = 4 log(2)
    ax[1].set_ylim(0, int(np.log(f_s//2)))

    def init(): 
        line_t.set_data([], [])
        line_f.set_data([], []) 
        return line_t, line_f

    def update(frame):
        #ax.set_xlim(frame*CHUNK, (frame + 1)*CHUNK)
        #line_f.set_data(np.arange(frame*CHUNK, (frame + 1)*CHUNK),
        #              data[frame*CHUNK:(frame + 1)*CHUNK, 0]
        #)

        lower, upper = frame*CHUNK, (frame + 1)*CHUNK
        y = data[lower:upper, 0]
        ax[0].set_xlim(lower, upper)
        line_t.set_data(
            np.arange(lower, upper),
            y
        )

        # now do the frequency domain

        ax[1].set_xlim(0, f_s//2)

        # w = 2 pi f
        dft_res = np.log(np.abs(np.fft.fft(y)))
        f = ((np.arange(CHUNK//2))/CHUNK)*f_s
        #print(f"{min(f)}, {max(f)}, {len(f)}")
        #print(CHUNK//2)
        line_f.set_data(
            (f),
            dft_res[:CHUNK//2]
        )
        return line_t, line_f

    anim = FuncAnimation(fig, update, init_func=init,
                        frames = TOTAL_FRAMES
                        )

    writer = FFMpegWriter(fps=FPS)
    anim.save(args.output, writer=writer)

if __name__ == "__main__":
    main()
