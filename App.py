from PyQt5.QtWidgets import *
from PyQt5 import uic
import res, json

class FormLogin(QWidget):
    def __init__(self):
        super(FormLogin, self).__init__()
        uic.loadUi("formlogin.ui", self)

class FormSurvey(QWidget):
    def __init__(self):
        super(FormSurvey, self).__init__()
        uic.loadUi("formsurvey.ui", self)
        listdata = ["Apel", "Mangga", "Strawberry", "Melon", "Pepaya"]
        for i in listdata:
            self.comboBox.addItem(i)

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
        # self.viewResult()

    def mainUi(self):
        self.form_login = FormLogin()
        self.form_survey = FormSurvey()
        self.result = Result()
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.form_login)
        self.stackedLayout.addWidget(self.form_survey)
        self.stackedLayout.addWidget(self.result)
        self.itemfavorite = ""

        # get combobox
        self.form_survey.comboBox.activated.connect(self.getValCombo)

    def mainLayout(self):
        self.widget = QWidget()
        self.setFixedSize(600,700)
        self.widget.setStyleSheet("background-color: rgb(46, 109, 255)")
        self.widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.widget)

    def getValCombo(self, index):
        self.itemfavorite = self.form_survey.comboBox.itemText(index)

    def getValues(self):
        itemFavorite = self.itemfavorite
        kelengkapanStok = self.form_survey.spinBox_7.value()
        toilet = self.form_survey.spinBox_7.value()
        rakMakanan = self.form_survey.spinBox_7.value()
        rakBuah = self.form_survey.spinBox_7.value()
        rakPecahBelah = self.form_survey.spinBox_7.value()
        refrigrator = self.form_survey.spinBox_7.value()
        lantaiToko = self.form_survey.spinBox_7.value()
        lokasiStrategis = self.form_survey.horizontalSlider.value()
        lahanParkir = ""
        if self.form_survey.checkBox.isChecked():
            lahanParkir = self.form_survey.checkBox.text()
        elif self.form_survey.checkBox_2.isChecked():
            lahanParkir = self.form_survey.checkBox_2.text()
        elif self.form_survey.checkBox_3.isChecked():
            lahanParkir = self.form_survey.checkBox_3.text()

        self.data = {
            "ItemFavorite": itemFavorite,
            "KelengkapanStok": kelengkapanStok,
            "Toilet": toilet,
            "RakMakanan": rakMakanan,
            "RakBuah": rakBuah,
            "RakPecahBelah": rakPecahBelah,
            "Refrigrator": refrigrator,
            "LantaiToko": lantaiToko,
            "LokasiStrategis": lokasiStrategis,
            "LahanParkir": lahanParkir
        }
        return self.data

    def viewResult(self):
        data = self.getValues()
        Item = self.result.findChild(QLabel, "label_21")
        Item.setText(data["ItemFavorite"])
        Stok = self.result.findChild(QLabel, "label_22")
        Stok.setText(str(data["KelengkapanStok"]))
        Toilet = self.result.findChild(QLabel, "label_2")
        Toilet.setText(str(data["Toilet"]))
        RakMakanan = self.result.findChild(QLabel, "label_11")
        RakMakanan.setText(str(data["RakMakanan"]))
        RakBuah = self.result.findChild(QLabel, "label_16")
        RakBuah.setText(str(data["RakBuah"]))
        RakPecahBelah = self.result.findChild(QLabel, "label_12")
        RakPecahBelah.setText(str(data["RakPecahBelah"]))
        Refrigrator = self.result.findChild(QLabel, "label_13")
        Refrigrator.setText(str(data["Refrigrator"]))
        LantaiToko = self.result.findChild(QLabel, "label_14")
        LantaiToko.setText(str(data["LantaiToko"]))
        LokasiStrategis = self.result.findChild(QLabel, "label_18")
        LokasiStrategis.setText(str(data["LokasiStrategis"]))
        lokasi = self.result.findChild(QLabel, "label_19")
        lokasi.setText(data["LahanParkir"])

    def action(self):
        username = self.form_login.findChild(QLineEdit, "lineEdit")
        password = self.form_login.findChild(QLineEdit, "lineEdit")
        self.user = [username.text(), password.text()]
        self.form_login.pushButton.clicked.connect(self.act_login)
        self.form_survey.pushButton.clicked.connect(self.act_survey)
        self.result.pushButton.clicked.connect(self.addToJson)

    def act_login(self):
        self.stackedLayout.setCurrentIndex(1)

    def act_survey(self):
        self.viewResult()
        self.stackedLayout.setCurrentIndex(2)

    def addToJson(self):
        data = self.getValues()
        toJson =  json.dumps(data, indent=4)
        fwrite = open('data.json', 'w')
        fwrite.write(toJson)
        QMessageBox.information(self, "About", "Export to Json Success")


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
