# main_app_new.py
"""Main application window - refactored and modular"""

import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QMenuBar, QMenu, QMessageBox, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QFont
from data_model import ReadingManager
from ui.constants import PRIMARY_COLOR, ACCENT_COLOR, BG_GRADIENT_BOTTOM
from ui.utils import find_logo_path
from pages import LoadingPage, LoginPage, WelcomePage, HomePage, InputPage, HistoryPage, GraphPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traquarium")
        
        icon_path = find_logo_path()
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
            print(f"[OK] Logo found at: {icon_path}")
        else:
            print("[WARNING] Logo not found")
        
        # Set minimum size and start at minimum size
        self.setMinimumSize(1050, 750)
        self.resize(1050, 750)  # Start at minimum size
        
        # Center the window on screen
        self.center_on_screen()

        self.current_user = None
        self.manager = None
        self.is_closing = False

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create menu bar
        self.create_menu_bar()
        main_layout.addWidget(self.menu_bar)

        # Create stacked widget for pages
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Add base pages
        self.loading_page = LoadingPage(self.stacked_widget)
        self.login_page = LoginPage(self.stacked_widget, main_window=self)
        self.welcome_page = WelcomePage(self.stacked_widget)

        self.stacked_widget.addWidget(self.loading_page)  # 0
        self.stacked_widget.addWidget(self.login_page)    # 1
        self.stacked_widget.addWidget(self.welcome_page)  # 2
        self.stacked_widget.setCurrentIndex(0)

        self.setup_shortcuts()
    
    def center_on_screen(self):
        """Center the window on the screen"""
        from ui.helpers import WindowHelper
        WindowHelper.center_window(self)

    def create_menu_bar(self):
        """Creates the top menu bar for File and Help"""
        from ui.styles import MENU_BAR_STYLE
        self.menu_bar = QMenuBar(self)
        self.menu_bar.setStyleSheet(MENU_BAR_STYLE)

        # File Menu
        file_menu = self.menu_bar.addMenu("File")
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        exit_action.triggered.connect(self.quit_app)
        file_menu.addAction(exit_action)

        # Help Menu
        help_menu = self.menu_bar.addMenu("Help")
        
        shortcuts_action = QAction("Keyboard Shortcuts", self)
        shortcuts_action.setShortcut(QKeySequence("F1"))
        shortcuts_action.triggered.connect(self.show_shortcuts_guide)
        help_menu.addAction(shortcuts_action)

        about_action = QAction("About Traquarium", self)
        about_action.setShortcut(QKeySequence("Ctrl+I"))
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def setup_shortcuts(self):
        """Set up global keyboard shortcuts"""
        from PyQt6.QtGui import QShortcut, QKeySequence
        from PyQt6.QtCore import Qt
        
        # F11 for fullscreen toggle
        fullscreen_shortcut = QShortcut(QKeySequence(Qt.Key.Key_F11), self)
        fullscreen_shortcut.activated.connect(self.toggle_fullscreen)
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        from ui.helpers import WindowHelper
        WindowHelper.toggle_fullscreen(self)

    def show_shortcuts_guide(self):
        """Shows a help dialog listing keyboard shortcuts"""
        from ui.styles import MESSAGE_BOX_STYLE
        msg = QMessageBox(self)
        msg.setWindowTitle("Keyboard Shortcuts")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(
            "<b style='font-size: 14pt;'>Keyboard Shortcuts</b><br><br>"
            "<b>Navigation:</b><br>"
            "<table cellpadding='5'>"
            "<tr><td><b>Ctrl + H</b></td><td>→</td><td>Go to Home Page</td></tr>"
            "<tr><td><b>Ctrl + 1</b></td><td>→</td><td>Go to Input Page</td></tr>"
            "<tr><td><b>Ctrl + 2</b></td><td>→</td><td>Go to History Page</td></tr>"
            "<tr><td><b>Ctrl + 3</b></td><td>→</td><td>Go to Graph Page</td></tr>"
            "</table><br>"
            "<b>Application:</b><br>"
            "<table cellpadding='5'>"
            "<tr><td><b>F11</b></td><td>→</td><td>Toggle Fullscreen</td></tr>"
            "<tr><td><b>Ctrl + Q</b></td><td>→</td><td>Exit Application</td></tr>"
            "<tr><td><b>F1</b></td><td>→</td><td>Show This Help</td></tr>"
            "<tr><td><b>Ctrl + I</b></td><td>→</td><td>About Traquarium</td></tr>"
            "</table><br>"
            "<i>Tip: Use the menu bar at the top for additional options!</i>"
        )
        msg.setStyleSheet(MESSAGE_BOX_STYLE)
        msg.exec()

    def show_about(self):
        """Show About dialog from menu"""
        from ui.dialogs import AboutDialog
        dialog = AboutDialog(self)
        dialog.exec()

    def quit_app(self):
        """Properly closes the application with confirmation (for keyboard shortcut)"""
        if not self.is_closing:
            self.is_closing = True
            reply = QMessageBox.question(
                self,
                'Exit Traquarium',
                'Close Traquarium and save all data?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                QApplication.instance().quit()
            else:
                self.is_closing = False
    
    def closeEvent(self, event):
        """Handle window close event (X button) - show confirmation"""
        if self.is_closing:
            event.accept()
            return
            
        reply = QMessageBox.question(
            self,
            'Exit Traquarium',
            'Close Traquarium and save all data?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def set_current_user(self, username):
        """Called after successful login"""
        self.current_user = username
        self.manager = ReadingManager(username)

        # Build user-specific pages
        self.home_page = HomePage(self.stacked_widget, self.manager, username)
        self.history_page = HistoryPage(self.stacked_widget, self.manager)
        self.graph_page = GraphPage(self.stacked_widget)
        self.input_page = InputPage(self.stacked_widget, self.history_page, self.graph_page, self.manager)

        # Clear old pages (if any)
        while self.stacked_widget.count() > 3:
            widget = self.stacked_widget.widget(3)
            self.stacked_widget.removeWidget(widget)
            widget.deleteLater()

        # Add new ones
        self.stacked_widget.addWidget(self.home_page)      # 3
        self.stacked_widget.addWidget(self.input_page)     # 4
        self.stacked_widget.addWidget(self.history_page)   # 5
        self.stacked_widget.addWidget(self.graph_page)     # 6

        # Refresh with existing data
        readings = self.manager.get_all()
        self.home_page.update_latest(readings)
        self.history_page.update_table(readings)
        self.graph_page.update_graph(readings)

    @staticmethod
    def apply_global_styles(app: QApplication):
        """Applies global ocean-inspired theme"""
        from ui.constants import PRIMARY_COLOR, ACCENT_COLOR
        app.setStyleSheet(f"""
            QWidget {{
                font-family: 'Poppins';
                color: {PRIMARY_COLOR};
            }}
            QPushButton {{
                background-color: {ACCENT_COLOR};
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {PRIMARY_COLOR};
            }}
        """)
