# ui/base_page.py
"""Base page class for all parameter-related pages"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from .constants import PRIMARY_COLOR, ACCENT_COLOR, TITLE_FONT, MAIN_FONT, TEXT_PRIMARY
from .utils import background
from .dialogs import AboutDialog


class AquaPage(QWidget):
    """Base class for all parameter-related pages."""
    def __init__(self, title: str, stacked_widget):
        super().__init__()
        background(self)
        self.stacked_widget = stacked_widget

        self.layout_main = QVBoxLayout(self)
        self.layout_main.setSpacing(20)

        # Header with Home button (left), title (center), and About button (right)
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(20, 10, 20, 10)
        
        # Home button (left side)
        from .components import ButtonFactory
        home_btn = ButtonFactory.create_icon_button("🏠", QFont("Segoe UI", 16), (40, 40), "Home")
        home_btn.clicked.connect(lambda: stacked_widget.setCurrentIndex(3))
        header_layout.addWidget(home_btn)
        
        # Stretch before title
        header_layout.addStretch()
        
        # Page title (truly centered)
        title_label = QLabel(title)
        title_label.setFont(TITLE_FONT)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(f"color: {TEXT_PRIMARY};")
        header_layout.addWidget(title_label)
        
        # Stretch after title
        header_layout.addStretch()
        
        # About button (right side)
        about_btn = ButtonFactory.create_icon_button("❓", QFont("Segoe UI", 16), (40, 40), "About Traquarium", secondary=True)
        about_btn.clicked.connect(self.show_about_dialog)
        header_layout.addWidget(about_btn)

        self.layout_main.addLayout(header_layout)

        # Placeholder for dynamic content (subclass fills this)
        self.content_layout = QVBoxLayout()
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addLayout(self.content_layout)

        # Navigation bar (bottom consistent) - Always show Input, History, Graph
        nav_bar = QHBoxLayout()
        nav_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav_bar.setSpacing(15)
        
        # Fixed navigation buttons
        nav_items = [
            ("➕ Input", 4),
            ("📋 History", 5),
            ("📊 Graph", 6)
        ]
        
        for btn_text, index in nav_items:
            btn = ButtonFactory.create_nav_button(btn_text, MAIN_FONT)
            btn.clicked.connect(lambda _, i=index: stacked_widget.setCurrentIndex(i))
            nav_bar.addWidget(btn)
        self.layout_main.addLayout(nav_bar)

    def show_about_dialog(self):
        """Show the About dialog"""
        dialog = AboutDialog(self)
        dialog.exec()
    
    def keyPressEvent(self, event):
        """Handle keyboard shortcuts"""
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QKeySequence
        
        # Ctrl+H to go to home page
        if event.key() == Qt.Key.Key_H and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stacked_widget.setCurrentIndex(3)  # Home page is at index 3
            event.accept()
        # Ctrl+1 to go to input page
        elif event.key() == Qt.Key.Key_1 and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stacked_widget.setCurrentIndex(4)  # Input page is at index 4
            event.accept()
        # Ctrl+2 to go to history page
        elif event.key() == Qt.Key.Key_2 and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stacked_widget.setCurrentIndex(5)  # History page is at index 5
            event.accept()
        # Ctrl+3 to go to graph page
        elif event.key() == Qt.Key.Key_3 and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stacked_widget.setCurrentIndex(6)  # Graph page is at index 6
            event.accept()
        else:
            super().keyPressEvent(event)