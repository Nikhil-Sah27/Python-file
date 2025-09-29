import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("400x300")

        tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12)).pack(pady=10)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        self.download_button = tk.Button(root, text="Download", command=self.download_video, font=("Arial", 12))
        self.download_button.pack(pady=20)

        self.status_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
        self.status_label.pack(pady=5)

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        try:
            self.status_label.config(text="Downloading...")
            self.root.update()

            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            save_path = filedialog.askdirectory()

            if save_path:
                video.download(save_path)
                messagebox.showinfo("Success", "Download complete!")
            else:
                messagebox.showwarning("Warning", "Download cancelled.")

            self.status_label.config(text="")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to download: {str(e)}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
