# YouTube-Video-Downloader

YouTube, the second most popular global website, is widely recognized as the top video hosting platform. However, there are limitations to directly downloading videos from YouTube.

This is a simple YouTube video downloader that allows you to download videos from YouTube in a variety of formats.

Requirements:

    Python 3.6 or later
    The pytube library
Installation:

    pip install pytube

Usage
To use the downloader, simply enter the URL of the YouTube video or playlist you want to download.


# If the previous system doesn't work

## FFmpeg Installation Guide for Windows

`ffmpeg` is required for downloading videos in 720p (or any resolution where `yt-dlp` needs to merge separate video and audio streams). YouTube often provides video and audio as separate streams, especially for higher resolutions (like 720p, 1080p, etc.), so `yt-dlp` needs `ffmpeg` to combine them into a single file.

## Installation Steps



### 1. Download FFmpeg

- Under Windows, visit [FFmpeg Builds by BtbN](https://github.com/BtbN/FFmpeg-Builds/releases).
- Download the latest full build ZIP file (e.g., `ffmpeg-n4.4-win64-gpl.zip` if you’re on 64-bit Windows).

### 2. Extract the ZIP File

- Once downloaded, extract the ZIP file to a convenient location (e.g., `C:\ffmpeg`).

### 3. Add FFmpeg to PATH

1. Open the extracted folder and navigate to the `bin` folder inside it. This folder contains `ffmpeg.exe`.
2. Copy the path to this `bin` folder (e.g., `C:\ffmpeg\bin`).
3. Go to **Control Panel** → **System and Security** → **System** → **Advanced system settings**.
4. In the **System Properties** window, click on **Environment Variables**.
5. Under **System Variables**, find the `Path` variable, select it, and click **Edit**.
6. Click **New** and paste the path to the `bin` folder (e.g., `C:\ffmpeg\bin`), then click **OK** to save.

## Verification

To verify that `ffmpeg` is correctly installed and added to your PATH:

1. Open a new command prompt window.
2. Type the following command:
   ```bash
   ffmpeg -version

