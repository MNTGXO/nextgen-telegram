import cv2
import numpy as np
from PIL import Image, ImageEnhance

class MediaEnhancer:
    @staticmethod
    async def enhance_image(image_path: str, output_path: str):
        # Read image
        img = Image.open(image_path)
        
        # Enhance contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.5)
        
        # Remove noise
        img_array = np.array(img)
        img_array = cv2.fastNlMeansDenoisingColored(img_array, None, 10, 10, 7, 21)
        
        # Save enhanced image
        enhanced_img = Image.fromarray(img_array)
        enhanced_img.save(output_path)
