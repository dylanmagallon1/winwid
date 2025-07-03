from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QSystemTrayIcon, QMenu
from PySide6.QtGui import QFontDatabase, QFont, QIcon, QAction
from PySide6.QtCore import Qt, QTimer
import datetime, os, sys
app = QApplication([])
if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")
font_path = os.path.join(base_path, "Anurati-Regular.otf")
font_id = QFontDatabase.addApplicationFont(font_path)
if font_id == -1:
    print("Font couldn't load")
    sys.exit(1)
font_families = QFontDatabase.applicationFontFamilies(font_id)
if not font_families:
    print("No font families found in font file")
    sys.exit(1)
font_name = font_families[0]
winwid = QWidget()
winwid.setWindowTitle("winwid")
winwid.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.Tool)
winwid.setAttribute(Qt.WA_TranslucentBackground)
winwid.setAttribute(Qt.WA_TransparentForMouseEvents)
try:
    icon_path = os.path.join(base_path, "duck.ico")
    icon = QIcon(icon_path)
    winwid.setWindowIcon(icon)
    app.setWindowIcon(icon)
except Exception as e:
    print(f"An error has occurred: {e}")
label = QLabel()
label.setFont(QFont(font_name, 36))
label.setStyleSheet("color: white; background-color: transparent; letter-spacing: 16px;")
label.setAlignment(Qt.AlignCenter)
layout = QVBoxLayout()
layout.addWidget(label)
winwid.setLayout(layout)
winwid.resize(600, 200)
winwid.show()
def manage_week():
    days = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
    week_day = datetime.datetime.now().weekday()
    label.setText(days[week_day])
win_timer = QTimer()
win_timer.timeout.connect(manage_week)
win_timer.start(60000)
manage_week()
tray = QSystemTrayIcon(QIcon(icon_path), app)
tray.setToolTip("winwid - Día actual")
tray_menu = QMenu()
exit_action = QAction("Salir")
exit_action.triggered.connect(app.quit)
tray_menu.addAction(exit_action)

tray.setContextMenu(tray_menu)
tray.show()
try:
    app.exec()
except KeyboardInterrupt:
    winwid.close()
    app.quit()