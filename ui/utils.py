# ui/utils.py
"""UI utility functions"""

import os
from PyQt6.QtGui import QPalette, QLinearGradient, QBrush, QColor
from .constants import BG_GRADIENT_TOP, BG_GRADIENT_BOTTOM, LIGHT_COLOR


def find_logo_path():
    """Find the logo file in common locations. Returns path or None if not found."""
    possible_paths = [
        "aquarium_logo.png",
        "./aquarium_logo.png",
        os.path.join(os.getcwd(), "aquarium_logo.png"),
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "aquarium_logo.png"),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def background(widget):
    """Applies modern blue gradient background."""
    palette = QPalette()
    bg = QLinearGradient(0, 0, 0, widget.height())
    bg.setColorAt(0.0, QColor("#1e3c72"))  # Deep blue
    bg.setColorAt(0.5, QColor("#2a5298"))  # Medium blue
    bg.setColorAt(1.0, QColor("#1e3c72"))  # Deep blue
    palette.setBrush(QPalette.ColorRole.Window, QBrush(bg))
    widget.setAutoFillBackground(True)
    widget.setPalette(palette)