import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QInputDialog, QApplication, QTextBrowser)

class Simplex(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.objective()
        self.constrains()
        self.resize(600, 300)
        self.setWindowTitle('Simplex solver')
        print("exit", objective_global)
        self.show()

    def objective(self):
        self.objective_btn = QPushButton('Objective function', self)
        self.objective_btn.move(20, 20)
        self.objective_btn.clicked.connect(self.objectiveDialog)
        self.objective_line = QTextBrowser(self)
        self.objective_line.setGeometry(250, 28, 250, 28)
        self.objective_line.move(200, 20)

    def constrains(self):
        self.constrains_btn = QPushButton('Constrains', self)
        self.constrains_btn.move(20, 60)
        self.constrains_btn.clicked.connect(self.constrainsDialog)
        self.constrains_line = QTextBrowser(self)
        self.constrains_line.setGeometry(250, 28, 250, 28)
        self.constrains_line.move(200, 60)

    def objectiveDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter objective function:')
        if ok:
            self.objective_line.setText(str(text))

    def constrainsDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter constrains:')
        if ok:
            self.constrains_line.setText(str(text))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    simplex = Simplex()
    sys.exit(app.exec_())