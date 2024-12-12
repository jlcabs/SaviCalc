from PySide6.QtWidgets import QApplication
from screens import Window

app = QApplication([])

window = Window()
window.show()

app.exec()
