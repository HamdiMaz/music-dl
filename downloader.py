import yt_dlp
import os
from pathlib import Path

def download_audio(url, output_dir="downloads"):
    """
    Download YouTube video as MP3 with highest possible quality.
    
    Args:
        url (str): YouTube video URL
        output_dir (str): Directory to save the downloaded file
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Configure yt-dlp options for best audio quality
    ydl_opts = {
        'format': 'bestaudio/best',  # Select best quality audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # Highest MP3 bitrate
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'verbose': False,
        # Additional options for better quality
        'audioformat': 'mp3',
        'audioquality': '0',  # Highest quality
        'noplaylist': True,   # Download single video, not playlist
        # Error handling
        'ignoreerrors': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Starting download...")
            ydl.download([url])
            print("\nDownload completed successfully!")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise


# if __name__ == "__main__":
#     # Example usage
#     download_audio("https://youtu.be/5zjMnIQRRfI?si=N9pM_AYUncWXO2eg")