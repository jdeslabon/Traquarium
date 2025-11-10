# ui/animations.py
"""Animation utilities for UI elements"""

from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QSize, pyqtProperty
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QColor


class AnimatedButton(QPushButton):
    """Button with smooth hover animations"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._scale = 1.0
        self._original_size = None
        
        # Animation for scale
        self.scale_animation = QPropertyAnimation(self, b"scale")
        self.scale_animation.setDuration(200)
        self.scale_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
    def get_scale(self):
        return self._scale
    
    def set_scale(self, scale):
        self._scale = scale
        if self._original_size:
            new_width = int(self._original_size.width() * scale)
            new_height = int(self._original_size.height() * scale)
            self.setFixedSize(new_width, new_height)
    
    scale = pyqtProperty(float, get_scale, set_scale)
    
    def enterEvent(self, event):
        """Animate on hover enter"""
        if not self._original_size:
            self._original_size = self.size()
        
        self.scale_animation.stop()
        self.scale_animation.setStartValue(self._scale)
        self.scale_animation.setEndValue(1.05)
        self.scale_animation.start()
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        """Animate on hover leave"""
        self.scale_animation.stop()
        self.scale_animation.setStartValue(self._scale)
        self.scale_animation.setEndValue(1.0)
        self.scale_animation.start()
        super().leaveEvent(event)