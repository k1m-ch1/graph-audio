# Requirements

- `ffmpeg`. Check that it's in your path by doing `ffmpeg -h`.

## Optional

- `uv`

# Usage

Make sure that your input file is a `mp3`, `wav`, `flac`, `ogg`, etc. If it's not supported, just convert the audio using `ffmpeg`.

```
ffmpeg -i audio.m4a audio.mp3
```

## With `uvx`

```
uvx --from graph-audio graph-audio -i <input_audio> -o <output_video>.mp4
```

Enjoy!

## Without uvx

First create a new virtual environment

```
python3 -m venv .venv
```

Activate it

```
source ./.venv/bin/activate
```

Download

```
pip install graph-audio
```

Run

```
graph_audio -i <input_audio> -o <output_video>.mp4
```

# About

This is pretty simple, I hard coded the FPS to 30 and the frequency graph could be a bar graph with better scaling in the x-direction (since we're not that sensitive to the higher frequencies).
