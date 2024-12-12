from PySide6.QtWidgets import QWidget, QLineEdit,  QComboBox, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QIcon
from darkdetect import isDark

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(320, 240)
        self.setWindowTitle('SaviCalc')

        if (isDark()):
            self.setWindowIcon(QIcon('assets/toolbar_icons/savings_16dp_D3D3D3_FILL0_wght400_GRAD0_opsz20.png'))
        else:
            self.setWindowIcon(QIcon('assets/toolbar_icons/savings_16dp_2C2C2C_FILL0_wght400_GRAD0_opsz20.png'))

        self.amount_fld = QLineEdit()
        self.percent_cmb = QComboBox()

        self.amount_fld.setPlaceholderText('Amount')
        self.percent_cmb.setPlaceholderText('Interest rate (%)')

        self.calc_btn = QPushButton(text='Calculate')
        self.total_lbl = QLabel('Total: ?')
        self.per_day_lbl = QLabel('Per day: ?')
        self.per_month_lbl = QLabel('Per month: ?')
        self.per_year_lbl = QLabel('Per year: ?')

        self.verti = QVBoxLayout()
        self.hori = QHBoxLayout()

        first_row_widgets = [self.amount_fld, self.percent_cmb]
        second_row_widgets = [self.calc_btn, self.total_lbl, self.per_day_lbl, self.per_month_lbl, self.per_year_lbl]
        
        for percent in range(1, 100+1):
            self.percent_cmb.addItem(f'{percent}%')

        for first_row_widget in first_row_widgets:
            self.hori.addWidget(first_row_widget)

        self.verti.addLayout(self.hori)
        for second_row_widget in second_row_widgets:
            self.verti.addWidget(second_row_widget)

        self.calc_btn.clicked.connect(self.calculate)

        self.setLayout(self.verti)

    def calculate(self):
        res = self.percent_cmb.currentText().removesuffix('%')
        total = int(self.amount_fld.text()) + int(self.amount_fld.text()) * ((int(res)) / 100)
        self.total_lbl.setText(f'Total: {str(total)}')
        self.per_day_lbl.setText(f'Per day: {round((int(self.amount_fld.text())) * (int(res) / 100) / 365, 2)}')
        self.per_month_lbl.setText(f'Per month: {round((int(self.amount_fld.text())) * (int(res) / 100) / 12, 2)}')
        self.per_year_lbl.setText(f'Per year: {int(self.amount_fld.text()) * ((int(res)) / 100)}')
