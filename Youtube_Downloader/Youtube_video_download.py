import yt_dlp

url = input("Enter the link: ")
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Download best video up to 1080p
    'merge_output_format': 'mp4'  # Ensures the final file is in mp4 format after merging
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    print("Title:", info.get('title'))
    print("Download complete!")

