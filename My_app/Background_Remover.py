import os
from datetime import datetime
from rembg import remove

class BackgroundRemover:
    def _init_(self,input_folder, output_folder):
        self.input_folder = input_folder
        self.outut_folder = output_folder
        
    def process_images(self):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        processed_folder = os.path.join(self.outut_folder, today)
        os.makedirs(processed_folder)
    def remove_background(self):
        pass
    
    def move_original(self):
        pass
    