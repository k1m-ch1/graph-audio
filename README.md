# Display


https://github.com/user-attachments/assets/1572f64a-af52-4e29-bf8b-840580080518


Sound from this ![YouTube video](https://youtu.be/lU7nARUa2CA?si=vPn20fQ5m4wuF8r_)


https://github.com/user-attachments/assets/1f44ace2-13b6-46e6-bd6b-a961c67eddf0

Sound from this ![YouTube video](https://youtu.be/6tI-0LBamGg?si=8GZ9T_O47nJY5Zf-)

https://github.com/user-attachments/assets/83fe1d5a-8dfd-452d-9b58-97fc8e7ae825

Sound from this ![YouTube video](https://youtu.be/dxDpdfzwuD4?si=JWRt_Lk3XisGJw0m)

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
