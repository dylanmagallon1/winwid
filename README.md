# 🪟 winwid

**winwid** is a lightweight, frameless desktop widget for Windows that displays the current weekday.  
Built in Python using PySide6, it stays always visible but non-intrusive — click-through, transparent, and docked to your desktop. It also includes a system tray icon for silent background operation.

---

## ✨ Features

- 🖥️ Frameless and transparent window  
- 🔤 Custom futuristic font (Anurati)  
- 🔄 Auto-updates the weekday every minute  
- 🖱️ Click-through: doesn't block desktop interactions  
- 📌 Always below other windows  
- 🧊 Lives in the Windows system tray  
- ⚡ Minimal and resource-friendly  

---

## 📦 Install dependencies

If you're running from source, install the required Python packages:

```bash
pip install -r requirements.txt


## 🔧 Build the `.exe`

To compile the widget into a standalone Windows executable:

```bash
pip install pyinstaller
pyinstaller winwid.spec
