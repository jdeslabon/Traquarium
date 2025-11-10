================================================================================
                    TRAQUARIUM - AQUARIUM WATER QUALITY MONITOR
================================================================================

Version: 1.0.0
Python: 3.8+

================================================================================
PROJECT OVERVIEW
================================================================================

Traquarium is a desktop application developed as an academic project by 2nd year 
Computer Engineering students. The application addresses the practical challenge 
of monitoring and tracking aquarium water quality parameters over extended periods.

PROJECT RATIONALE:
Traditional methods of recording water quality measurements rely on manual 
record-keeping, which is prone to human error and lacks analytical capabilities. 
Traquarium provides a comprehensive digital solution that enables aquarium 
enthusiasts to:
  - Systematically record water parameter measurements
  - Visualize trends through graphical representations
  - Receive automated warnings for unsafe parameter levels
  - Maintain historical records for multiple aquarium profiles

TECHNICAL SCOPE:
This project represents our first major GUI application development using Python 
and the PyQt6 framework. The implementation demonstrates our understanding of 
object-oriented programming, data persistence, user interface design, and 
software testing methodologies.

================================================================================
WHAT DOES IT DO?
================================================================================

Traquarium allows you to:

  * Track Water Parameters: Monitor pH levels, temperature, and ammonia 
    concentrations
  * Visualize Trends: View your water quality data through interactive graphs
  * Get Warnings: Receive automatic alerts when parameters fall outside safe 
    ranges
  * Manage Multiple Profiles: Track different tanks or aquariums separately
  * Review History: Access complete historical data with search and filtering
  * Edit Records: Modify past readings if you need to correct mistakes

================================================================================
KEY FEATURES
================================================================================

REAL-TIME MONITORING
--------------------
Track three critical water parameters:
  - pH Level (0-14): Measures water acidity/alkalinity
  - Temperature (0-40°C): Monitors water temperature
  - Ammonia (0-10 ppm): Detects toxic ammonia levels

DATA VISUALIZATION
------------------
  - Interactive bar graphs showing parameter trends
  - Color-coded warnings for unsafe levels
  - Latest reading dashboard with circular stat cards
  - Historical data comparison

MULTI-USER SUPPORT
------------------
  - Individual user accounts with secure login
  - Separate data storage for each user
  - Profile-based reading management

INTELLIGENT WARNINGS
--------------------
  - Automatic detection of unsafe water conditions
  - Actionable suggestions for correcting problems
  - Color-coded alerts (green = safe, yellow = caution, red = danger)

DATA MANAGEMENT
---------------
  - Persistent storage of all readings
  - Search and filter by profile name
  - Edit or delete historical records
  - Export-ready JSON format

MODERN USER INTERFACE
---------------------
Traquarium features a beautiful, modern dark theme with:
  - Smooth blue gradient backgrounds
  - Intuitive navigation with keyboard shortcuts
  - Responsive design that works on different screen sizes
  - Clean, professional layout
  - Hover animations and visual feedback

================================================================================
GETTING STARTED
================================================================================

PREREQUISITES
-------------
  - Python 3.8 or higher
  - pip (Python package manager)

INSTALLATION
------------
1. Clone or download this repository
   
2. Install required dependencies:
   pip install PyQt6 pyqtgraph numpy

3. Run the application:
   python main.py

FIRST TIME SETUP
----------------
1. Launch the application - You'll see a loading screen
2. Create an account - Click "Sign Up" and enter your credentials
3. Login - Use your username and password to access the dashboard
4. Add your first reading - Navigate to the Input page and enter water 
   parameters

================================================================================
HOW TO USE
================================================================================

ADDING WATER READINGS
----------------------
1. Click "+ Add New Reading" or navigate to the Input page
2. Enter a profile name (e.g., "Main Tank", "Betta Tank")
3. Input your water parameters:
   - pH level (0-14)
   - Temperature in Celsius (0-40°C)
   - Ammonia in ppm (0-10)
4. Click "Save Reading"

VIEWING HISTORY
---------------
1. Navigate to the History page
2. Use the search bar to filter by profile name
3. Click on any row to see detailed warnings and suggestions
4. Use Edit to modify readings or Delete to remove them

ANALYZING TRENDS (GRAPH PAGE)
-----------------------------
The Graph page helps you visualize your water quality data over time!

How to use it:
1. First, select a profile from the History page (click on any row)
2. Navigate to the Graph page (Ctrl + 3)
3. You'll see a bar graph showing all readings for that profile:
   - Blue bars = pH levels
   - Orange bars = Temperature
   - Red bars = Ammonia levels
4. Check the info box below the graph for:
   - Profile name
   - Latest reading values with color coding
   - Timestamp of the last reading

What it shows:
- Each set of bars represents one reading
- Multiple readings are displayed side-by-side
- Easy to spot trends (going up, down, or staying stable)
- Helps you see if your water quality is improving or getting worse

Tip: Use this page to track how your water changes affect the parameters!

UNDERSTANDING WARNINGS
----------------------
The application provides color-coded warnings:

  - Green (Safe): Parameters are within optimal range
  - Yellow (Caution): Parameters need attention
  - Red (Danger): Immediate action required

Each warning includes specific suggestions for correcting the issue.

================================================================================
KEYBOARD SHORTCUTS
================================================================================

  Ctrl + H    Go to Home page
  Ctrl + 1    Go to Input page
  Ctrl + 2    Go to History page
  Ctrl + 3    Go to Graph page
  F11         Toggle fullscreen mode
  Ctrl + Q    Exit application
  F1          Show keyboard shortcuts help
  Ctrl + I    Show About dialog

================================================================================
WATER PARAMETER GUIDE
================================================================================

pH LEVEL (IDEAL: 6.5 - 8.0)
----------------------------
What it measures: Water acidity/alkalinity
Why it matters: Affects fish health, metabolism, and stress levels
Freshwater fish: 6.5-7.5
Marine aquariums: 8.0-8.4

Troubleshooting:
  - Too low? Add pH buffer or reduce CO2
  - Too high? Perform partial water change

TEMPERATURE (IDEAL: 20-28°C / 68-82°F)
---------------------------------------
What it measures: Water temperature
Why it matters: Critical for fish metabolism and immune function
Tropical fish: 24-28°C
Coldwater fish: 18-22°C

Troubleshooting:
  - Too low? Increase heater temperature
  - Too high? Improve ventilation or add cooling

AMMONIA (IDEAL: 0-0.5 PPM)
---------------------------
What it measures: Toxic ammonia concentration
Why it matters: Highly toxic to fish even in small amounts
Established tanks: Should be 0 ppm
New tanks: May spike during cycling

Troubleshooting:
  - >0.5 ppm? URGENT - Immediate water change required
  - 0.2-0.5 ppm? Check filter, reduce feeding

================================================================================
TECHNICAL DETAILS
================================================================================

LEARNING OUTCOMES
-----------------
Through the development of this project, the team successfully applied and 
enhanced their knowledge in the following areas:
  - Object-Oriented Programming (OOP) principles and design patterns
  - Graphical User Interface (GUI) development using PyQt6 framework
  - Data visualization techniques with PyQtGraph library
  - File I/O operations and JSON data serialization
  - User authentication and session management systems
  - Software design patterns and architectural principles
  - Version control systems and collaborative development workflows
  - Software testing and quality assurance methodologies

TECHNOLOGY STACK
----------------
  - Python 3.x: Core programming language for application logic
  - PyQt6: Cross-platform GUI framework for desktop applications
  - PyQtGraph: Scientific graphics and data visualization library
  - NumPy: Numerical computing library for data processing
  - JSON: Lightweight data-interchange format for persistent storage

PROJECT STRUCTURE
-----------------
traquarium/
├── main.py                 # Application entry point
├── main_app.py            # Main window and navigation
├── auth.py                # User authentication
├── data_model.py          # Data management
├── pages/                 # Application pages
│   ├── loading_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── welcome_page.py
│   ├── home_page.py
│   ├── input_page.py
│   ├── history_page.py
│   └── graph_page.py
├── ui/                    # UI components
│   ├── constants.py       # Colors and fonts
│   ├── styles.py          # CSS stylesheets
│   ├── components.py      # Reusable components
│   ├── helpers.py         # Helper functions
│   ├── utils.py           # Utility functions
│   ├── dialogs.py         # Dialog windows
│   └── base_page.py       # Base page class
└── users/                 # User data storage
    └── [username]/
        └── readings.json

DATA STORAGE
------------
  - User data is stored locally in JSON format
  - Each user has a separate folder in users/[username]/
  - Readings are stored in readings.json with timestamps
  - No internet connection required - fully offline

================================================================================
DEVELOPMENT TEAM
================================================================================

PROJECT MEMBERS (2nd Year Computer Engineering Students):

  Arindaeng, Paul Daniel
    Position: Lead Developer & System Architect
    Responsibilities: Application architecture, system integration, core 
                     functionality, and navigation implementation
    
  Dela Cruz, Gabriel
    Position: UI/UX Designer & Frontend Developer
    Responsibilities: User interface design, page layouts, visual styling, 
                     and component development
    
  Eslabon, John Donald
    Position: Backend Developer & Data Management Specialist
    Responsibilities: Data persistence, file handling, storage systems, 
                     and data processing logic
    
  Garcia, Rain
    Position: Quality Assurance & Documentation Specialist
    Responsibilities: Software testing, debugging, user documentation, 
                     and technical writing

PROJECT CONTEXT:
This application represents the culmination of our semester project, demonstrating 
the practical application of software engineering principles and programming 
concepts learned throughout our Computer Engineering curriculum.

================================================================================
FEEDBACK & FUTURE ENHANCEMENTS
================================================================================

As an academic project, we welcome constructive feedback and suggestions for 
improvement. This application serves as a foundation for understanding software 
development principles, and we recognize opportunities for future enhancement.

POTENTIAL IMPROVEMENTS:
  - Implementation of additional water parameters (nitrite, nitrate, GH, KH)
  - Export functionality for data analysis in external applications
  - Automated reminder system for scheduled water testing
  - Cloud synchronization for multi-device access
  - Mobile application development for on-the-go monitoring

CONTRIBUTION GUIDELINES:
For fellow students or developers interested in contributing:
1. Review the existing codebase and documentation
2. Identify areas for improvement or feature additions
3. Follow established coding standards and conventions
4. Submit detailed pull requests with clear descriptions
5. Participate in code review processes

We acknowledge that continuous improvement is essential in software development 
and welcome collaborative efforts to enhance this application.

================================================================================
PROJECT INFORMATION
================================================================================

This is a student project created for our Computer Engineering course. We built 
it to learn more about software development and to create something useful for 
aquarium hobbyists.

CONTACT US
----------
If you have questions about the project or want to give us feedback:
  - GitHub: Check our repository for issues and updates
  - Email: Feel free to reach out to any of our team members

Note: This is an academic project, so response times may vary depending on our 
class schedules!

================================================================================
ACKNOWLEDGMENTS
================================================================================

The development team would like to acknowledge the following contributions to 
this project:

ACADEMIC SUPPORT:
  - Computer Engineering faculty for providing foundational knowledge and guidance
  - Department resources and laboratory facilities for development and testing

TECHNICAL RESOURCES:
  - PyQt6 and PyQtGraph official documentation and community forums
  - Python Software Foundation for comprehensive language documentation
  - Open-source community for valuable libraries and frameworks
  - Stack Overflow community for technical problem-solving assistance

TESTING & FEEDBACK:
  - Fellow students who participated in user acceptance testing
  - Aquarium hobbyist community for domain knowledge and requirements validation

This project would not have been possible without the collective support of 
these individuals and communities.

================================================================================
VERSION HISTORY
================================================================================

v1.0.0 (2025) - Our First Release!
  - Initial release for our course project
  - Core water parameter tracking (pH, temperature, ammonia)
  - Multi-user support (so everyone in the family can track their tanks)
  - Data visualization with graphs (the fun part!)
  - Warning system (to help keep fish safe)
  - Modern UI with dark theme

FUTURE DEVELOPMENT ROADMAP:
  - CSV/Excel export functionality for external data analysis
  - Extended parameter monitoring (nitrite, nitrate, GH, KH)
  - Automated notification system for scheduled testing
  - Cloud-based data synchronization
  - Mobile application development for cross-platform accessibility

================================================================================

Developed by 2nd Year Computer Engineering Students
Academic Year 2024-2025

This application demonstrates the practical application of software engineering 
principles and serves as a comprehensive solution for aquarium water quality 
monitoring.

================================================================================