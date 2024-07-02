# Video File Format Converter Python Script

This Python script was created to solve a real problem I faced when needing to upload a video for my college summer class. My iPhone saves videos in `.mov` format, but the required format for submission was `.mp4`. The available app store options were either unsatisfactory or not free, so I decided to create my own script using Python and `ffmpeg`. The process was both practical and enjoyable.

## Features
- Converts `.mov` files to `.mp4` format.
- Utilizes `ffmpeg` for efficient and reliable video conversion.
- Easy to use with command-line arguments.

## Technologies Used

- **Python**: A powerful programming language that is easy to learn and use.
- **ffmpeg**: A comprehensive multimedia framework used to decode, encode, transcode, mux, demux, stream, filter, and play almost anything that humans and machines have created.
- **ffmpeg-python**: A Python library that provides a fluent interface to `ffmpeg`, making it easier to work with multimedia files in Python.

## Prerequisites

1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. Install the `ffmpeg` library using `pip`:
   ```bash
   pip install ffmpeg-python
   
3. python video_file_format_converter.py <input_file.mov> <output_file.mp4>
