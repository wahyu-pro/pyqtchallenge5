from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QStackedLayout, QVBoxLayout
from PyQt5 import uic
import res

class FormLogin(QWidget):
    def __init__(self):
        super(FormLogin, self).__init__()
        uic.loadUi("formlogin.ui", self)

class FormSurvey(QWidget):
    def __init__(self):
        super(FormSurvey, self).__init__()
        uic.loadUi("formsurvey.ui", self)

class Result(QWidget):
    def __init__(self):
        super(Result, self).__init__()
        uic.loadUi("result.ui", self)

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.mainUi()
        self.mainLayout()
        self.action()

    def mainUi(self):
        self.form_login = FormLogin()
        self.form_survey = FormSurvey()
        self.result = Result()
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.form_login)
        self.stackedLayout.addWidget(self.form_survey)
        self.stackedLayout.addWidget(self.result)

    def mainLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.stackedLayout)
        self.setLayout(self.layout)

    def action(self):
        self.form_login.pushButton.clicked.connect(self.act_login)

    def act_login(self):
        self.stackedLayout.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
