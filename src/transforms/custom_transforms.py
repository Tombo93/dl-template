from typing import callable
import torch
from torchvision.transforms import functional as F


class CustomImageCenterCrop(torch.nn.Module):
    def __init__(self, mid_size=380, large_size=2000):
        super().__init__()
        self.mid_size = mid_size
        self.large_size = large_size

    def forward(self, img):
        """
        Args:
            img (PIL Image or Tensor): Image to be worked cropped.

        Returns:
            PIL Image or Tensor: Worked on image.
        """
        width, _ = img.size
        if width <= 1024:
            return img
        if width < 6000 and width > 1024:
            return F.center_crop(img, self.mid_size)
        return F.center_crop(img, self.large_size)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class ApplyBackdoor(torch.nn.Module):
    def __init__(self, apply_to_img: callable):
        super().__init__()
        self._apply_to_img = apply_to_img

    def forward(self, img, label):
        """
        Args:
            img (PIL Image or Tensor)

        Returns:
            PIL Image or tensor with backdoor applied to image
        """
        if self._apply_to_img(label):
           # apply backdoor function here
            return img
        return img
