import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    idx = 0
    Kernels = {
        "original": np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.float32),
        "blur": np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]], dtype=np.float32),
        "gaussian blur": np.array([[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]], dtype=np.float32),
        "sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32),
        "sobel (X)": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32),
        "sobel (Y)": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32),
        "edge detection": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32),
        "emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32),
    }
    kernel_name = []
    
    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        self.kernel_name = list(self.kernels.keys())
        # TODO: Implement internal variables

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        return self.kernel_name[self.idx]

    def switch_next_filter(self):
        self.idx += 1
        self.idx %= len(self.kernel_name)

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        self.idx -= 1
        self.idx %= len(self.kernel_name)
