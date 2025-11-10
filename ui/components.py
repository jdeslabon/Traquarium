# ui/components.py
"""Reusable UI component classes and factory methods"""

from PyQt6.QtWidgets import QPushButton, QLabel, QFrame, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QDoubleValidator
from .styles import *


class StrictDoubleValidator(QDoubleValidator):
    """Strict validator that blocks invalid input and limits decimal places"""
    def validate(self, input_str, pos):
        if not input_str or input_str in ['.', '-', '-.']:
            return (QDoubleValidator.State.Intermediate, input_str, pos)
        
        # Prevent multiple leading zeros (like 0000)
        if len(input_str) > 1 and input_str[0] == '0' and input_str[1] != '.':
            return (QDoubleValidator.State.Invalid, input_str, pos)
        
        # Check for too many decimal places
        if '.' in input_str:
            decimal_part = input_str.split('.')[1]
            if len(decimal_part) > self.decimals():
                return (QDoubleValidator.State.Invalid, input_str, pos)
        
        try:
            value = float(input_str)
            if self.bottom() <= value <= self.top():
                return (QDoubleValidator.State.Acceptable, input_str, pos)
            else:
                return (QDoubleValidator.State.Invalid, input_str, pos)
        except ValueError:
            return (QDoubleValidator.State.Invalid, input_str, pos)


class ButtonFactory:
    """Factory class for creating styled buttons"""
    
    @staticmethod
    def create_primary_button(text, font, size=None):
        """Create a primary button with standard styling"""
        btn = QPushButton(text)
        btn.setFont(font)
        if size:
            btn.setFixedSize(*size)
        btn.setStyleSheet(PRIMARY_BUTTON_STYLE)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn
    
    @staticmethod
    def create_secondary_button(text, font, size=None):
        """Create a secondary button with standard styling"""
        btn = QPushButton(text)
        btn.setFont(font)
        if size:
            btn.setFixedHeight(size[1]) if size else None
        btn.setStyleSheet(SECONDARY_BUTTON_STYLE)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn
    
    @staticmethod
    def create_success_button(text, font):
        """Create a success/save button"""
        btn = QPushButton(text)
        btn.setFont(font)
        btn.setStyleSheet(SUCCESS_BUTTON_STYLE)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn
    
    @staticmethod
    def create_danger_button(text, font):
        """Create a danger/delete button"""
        btn = QPushButton(text)
        btn.setFont(font)
        btn.setStyleSheet(DANGER_BUTTON_STYLE)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn
    
    @staticmethod
    def create_nav_button(text, font):
        """Create a navigation button"""
        btn = QPushButton(text)
        btn.setFont(font)
        btn.setStyleSheet(NAV_BUTTON_STYLE)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn
    
    @staticmethod
    def create_icon_button(text, font, size, tooltip=None, secondary=False):
        """Create an icon button"""
        btn = QPushButton(text)
        btn.setFont(font)
        btn.setFixedSize(*size)
        if tooltip:
            btn.setToolTip(tooltip)
        btn.setStyleSheet(ICON_BUTTON_SECONDARY_STYLE if secondary else ICON_BUTTON_STYLE)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn
    
    @staticmethod
    def create_edit_button(text, font):
        """Create an edit button"""
        btn = QPushButton(text)
        btn.setFont(font)
        btn.setStyleSheet(EDIT_BUTTON_STYLE)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        return btn


class InputFieldFactory:
    """Factory class for creating styled input fields"""
    
    @staticmethod
    def create_login_input(placeholder, is_password=False):
        """Create a login/register style input field"""
        field = QLineEdit()
        field.setPlaceholderText(placeholder)
        if is_password:
            field.setEchoMode(QLineEdit.EchoMode.Password)
        field.setFixedSize(380, 50)
        field.setStyleSheet(INPUT_FIELD_STYLE)
        return field
    
    @staticmethod
    def create_form_input(placeholder, font, size, validator=None):
        """Create a form input field with optional validator"""
        field = QLineEdit()
        field.setPlaceholderText(placeholder)
        field.setFont(font)
        field.setMinimumSize(*size[:2])
        field.setMaximumSize(*size[2:])
        field.setStyleSheet(INPUT_FIELD_SMALL_STYLE)
        if validator:
            field.setValidator(validator)
        return field
    
    @staticmethod
    def create_search_input(placeholder, font):
        """Create a search input field"""
        field = QLineEdit()
        field.setPlaceholderText(placeholder)
        field.setFont(font)
        field.setStyleSheet(SEARCH_INPUT_STYLE)
        return field
    
    @staticmethod
    def create_validated_input(placeholder, min_val, max_val, decimals=2):
        """Create an input with strict numeric validation"""
        field = QLineEdit()
        field.setPlaceholderText(placeholder)
        validator = StrictDoubleValidator(min_val, max_val, decimals)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        field.setValidator(validator)
        return field


class FrameFactory:
    """Factory class for creating styled frames"""
    
    @staticmethod
    def create_card_frame(min_size=None, max_width=None):
        """Create a card-style frame"""
        frame = QFrame()
        if min_size:
            frame.setMinimumSize(*min_size)
        if max_width:
            frame.setMaximumWidth(max_width)
        frame.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        frame.setStyleSheet(CARD_FRAME_STYLE)
        return frame
    
    @staticmethod
    def create_guide_section(title, description, actions):
        """Create a styled guide section"""
        section = QFrame()
        section.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        section.setStyleSheet(GUIDE_SECTION_STYLE)
        
        section_layout = QVBoxLayout(section)
        section_layout.setSpacing(8)
        section_layout.setContentsMargins(5, 5, 5, 5)
        
        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #6BB3FF; background: transparent;")
        title_label.setWordWrap(True)
        section_layout.addWidget(title_label)
        
        # Description
        desc_label = QLabel(description)
        desc_label.setFont(QFont("Segoe UI", 10))
        desc_label.setStyleSheet("color: #FFFFFF; background: transparent;")
        desc_label.setWordWrap(True)
        section_layout.addWidget(desc_label)
        
        # Actions
        actions_label = QLabel(actions)
        actions_label.setFont(QFont("Segoe UI", 9, QFont.Weight.DemiBold))
        actions_label.setStyleSheet("color: #FFD700; background: transparent;")
        actions_label.setWordWrap(True)
        section_layout.addWidget(actions_label)
        
        return section


class LabelFactory:
    """Factory class for creating styled labels"""
    
    @staticmethod
    def create_title(text, font, color="#E8E8E8"):
        """Create a title label"""
        label = QLabel(text)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(f"color: {color};")
        return label
    
    @staticmethod
    def create_subtitle(text, font, color="#9CA3AF"):
        """Create a subtitle label"""
        label = QLabel(text)
        label.setFont(font)
        label.setStyleSheet(f"color: {color};")
        return label
    
    @staticmethod
    def create_feedback(font, color="#9CA3AF"):
        """Create a feedback label"""
        label = QLabel("")
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(f"color: {color};")
        return label


class ValidatorFactory:
    """Factory class for creating validators"""
    
    @staticmethod
    def create_ph_validator():
        """Create pH validator (0-14)"""
        validator = StrictDoubleValidator(0.0, 14.0, 2)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        return validator
    
    @staticmethod
    def create_temp_validator():
        """Create temperature validator (0-40°C)"""
        validator = StrictDoubleValidator(0.0, 40.0, 2)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        return validator
    
    @staticmethod
    def create_ammonia_validator():
        """Create ammonia validator (0-10 ppm)"""
        validator = StrictDoubleValidator(0.0, 10.0, 2)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        return validator
