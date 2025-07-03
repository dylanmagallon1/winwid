from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QFontDatabase, QFont, QIcon
from PySide6.QtCore import Qt, QTimer
import datetime
app = QApplication([])
font_id = QFontDatabase.addApplicationFont("Anurati-Regular.otf")
if font_id == -1:
    print("font couldn't load")
    exit()
font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
winwid = QWidget()
winwid.setWindowTitle("winwid")
winwid.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.Tool)
winwid.setAttribute(Qt.WA_TranslucentBackground)
winwid.setAttribute(Qt.WA_TransparentForMouseEvents)
try:
    icon = QIcon("duck.ico")
    winwid.setWindowIcon(icon)
except Exception as e:
    print(f"An error has ocurred: {e}")
label = QLabel()
label.setFont(QFont(font_name, 36))
label.setStyleSheet(
    "color: white; background-color: transparent; letter-spacing: 16px;"
)
label.setAlignment(Qt.AlignCenter)
layout = QVBoxLayout()
layout.addWidget(label)
winwid.setLayout(layout)
winwid.resize(600, 200)
winwid.show()
def manage_week():
    days = ["DOMINGO", "LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO"]
    week_day = datetime.datetime.now().isoweekday() % 7
    label.setText(days[week_day])
win_timer = QTimer()
win_timer.timeout.connect(manage_week)
win_timer.start(60000)
manage_week()
try:
    app.exec()
except KeyboardInterrupt:
    winwid.close()
    app.quit()