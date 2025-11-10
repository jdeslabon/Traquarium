# ui/constants.py
"""UI constants and styling configuration"""

from PyQt6.QtGui import QFont

# Fonts - Clean and readable
MAIN_FONT = QFont("Segoe UI", 11)
TITLE_FONT = QFont("Segoe UI", 24, QFont.Weight.Bold)
SUBTITLE_FONT = QFont("Segoe UI", 14)

# Colors - Modern dark theme with vibrant accents
PRIMARY_COLOR = "#3E4E5E"        # Dark slate blue (sidebar)
ACCENT_COLOR = "#7E87E1"         # Periwinkle blue
ACCENT_HOVER = "#8A93E8"         # Lighter periwinkle (hover)
LIGHT_COLOR = "#E8E8E8"          # Light gray text
BG_GRADIENT_TOP = "#3A3A3A"      # Dark charcoal (top)
BG_GRADIENT_BOTTOM = "#2B2B2B"   # Darker charcoal (bottom)
TEXT_PRIMARY = "#FFFFFF"         # White text for dark bg
TEXT_SECONDARY = "#B8B8B8"       # Medium gray text
SUCCESS_COLOR = "#66BB6A"        # Green
WARNING_COLOR = "#FFA726"        # Orange
DANGER_COLOR = "#EF5350"         # Coral red
CYAN_ACCENT = "#26C6DA"          # Cyan for cards
