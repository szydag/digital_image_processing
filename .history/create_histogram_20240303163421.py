import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageProcessor:
    def __init__(self, master):
        self.master = master
        self.master.title("Görüntü İşleme Programı")

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.load_button = tk.Button(self.master, text="Resim Aç", command=self.load_image)
        self.load_button.pack()

        self.histogram_button = tk.Button(self.master, text="Histogram Göster", command=self.show_histogram)
        self.histogram_button.pack()

        self.threshold_label = tk.Label(self.master, text="Eşik Değeri:")
        self.threshold_label.pack()

        self.threshold_slider = tk.Scale(self.master, from_=0, to=255, orient=tk.HORIZONTAL, length=200)
        self.threshold_slider.set(128)
        self.threshold_slider.pack()

        self.threshold_button = tk.Button(self.master, text="Eşikle", command=self.apply_threshold)
        self.threshold_button.pack()

        self.image = None
        self.thresholded_image = None
        self.histogram_window = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if self.image is not None:
            img = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=img)
            self.image_label.image = img

    def show_histogram(self):
        if self.image is not None:
            # Convert image to grayscale
            img_gray = self.image.convert("L")

            # Plot histogram
            histogram_values, bins, _ = plt.hist(img_gray.getdata(), bins=256, range=(0, 256), density=True, color='gray', alpha=0.75)
            plt.title('Histogram')
            plt.xlabel('Pixel Değeri')
            plt.ylabel('Frekans')

            # Create a new window for histogram
            self.histogram_window = tk.Toplevel(self.master)
            self.histogram_window.title("Histogram")

            # Embed the matplotlib figure in the Tkinter window
            figure = plt.Figure(figsize=(5, 4), dpi=100)
            subplot = figure.add_subplot(1, 1, 1)
            subplot.bar(bins[:-1], histogram_values, width=1, color='gray', alpha=0.75)
            subplot.set_title('Histogram')
            subplot.set_xlabel('Pixel Değeri')
            subplot.set_ylabel('Frekans')

            canvas = FigureCanvasTkAgg(figure, master=self.histogram_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            toolbar = NavigationToolbar2Tk(canvas, self.histogram_window)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def apply_threshold(self):
        if self.image is not None:
            img_gray = self.image.convert("L")
            threshold_value = self.threshold_slider.get()
            self.thresholded_image = img_gray.point(lambda x: 255 if x > threshold_value else 0)
            self.display_thresholded_image()

    def display_thresholded_image(self):
        if self.thresholded_image is not None:
            img = ImageTk.PhotoImage(self.thresholded_image)
            self.image_label.config(image=img)
            self.image_label.image = img

def main():
    root = tk.Tk()
    app = ImageProcessor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
