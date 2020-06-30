from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5.Qt import Qt
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import *
import res, json, requests

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

class Chart(QWidget):
    def __init__(self):
        super(Chart, self).__init__()


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.mainUi()
        self.mainLayout()
        self.action()
        self.toolBars()
        self.addToolBar(self.toolBarHome)
        self.addToolBar(self.toolBar)

    def mainUi(self):
        self.form_login = FormLogin()
        self.form_survey = FormSurvey()
        self.result = Result()
        # self.text = self.getText()
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.form_login)
        self.stackedLayout.addWidget(self.form_survey)
        self.stackedLayout.addWidget(self.result)
        self.stackedLayout.addWidget(self.chart())
        # self.stackedLayout.addWidget(self.getText())
        self.itemfavorite = ""

        # get combobox
        self.form_survey.comboBox.activated.connect(self.getValCombo)
        # self.result.pushButton_2.clicked.connect(self.print)

    def mainLayout(self):
        self.widget = QWidget()
        self.setFixedSize(600,700)
        self.widget.setStyleSheet("background-color: rgb(46, 109, 255)")
        self.widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.widget)

    def toolBars(self):
        self.toolBar = QToolBar()
        buttonToolbar = QAction(QIcon("icon/grafik.png"), "test", self)
        self.toolBar.addAction(buttonToolbar)
        buttonToolbar.triggered.connect(self.act_chart)

        self.toolBarHome = QToolBar()
        buttonToolbar = QAction(QIcon("icon/home.png"), "test", self)
        self.toolBarHome.addAction(buttonToolbar)
        buttonToolbar.triggered.connect(self.act_home)

    def act_chart(self):
        self.stackedLayout.setCurrentIndex(3)

    def act_home(self):
        self.stackedLayout.setCurrentIndex(0)

    def chart(self):
        respon = requests.get("https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json")
        json = respon.json()

        harga = list(map(lambda a: a['price'], json))
        barset0 = QBarSet("Harga Buah")
        for i in harga:
            barset0.append(i)

        series = QBarSeries()
        series.append(barset0)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        name = list(map(lambda a: a['name'], json))
        axisX = QBarCategoryAxis()
        axisX.append(name)

        axisY = QValueAxis()
        axisY.setRange(0, 950)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chartView = QChartView(chart)
        return chartView


    def getDataJson(self):
        with open('data.json', 'r') as respon:
            data = json.load(respon)
        return data

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

    def getText(self):
        data = self.getValues()
        text = """
            Hasil Penilaian Supermarket


            Item Favorite: {}
            Kelengkapan Stok: {}
            Toilet: {}
            Rak Makanan: {}
            Rak Buah: {}
            Rak Pecah Belah: {}
            Refrigrator: {}
            Lantai Toko: {}
            Lokasi Strategis: {}
            Lahan Parkir: {}
        """.format(data["ItemFavorite"], data["KelengkapanStok"], data["Toilet"], data['RakMakanan'], data["RakBuah"], data["RakPecahBelah"], data["Refrigrator"], data["LantaiToko"], data["LokasiStrategis"], data["LahanParkir"])
        self.textArea = QTextEdit()
        self.textArea.setText(text)
        self.button = QPushButton("print")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textArea)
        self.layout.addWidget(self.button)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.button.clicked.connect(self.print)

    def print(self):
        self.printer = QPrinter()
        self.dialog = QPrintDialog(self.printer)
        if self.dialog.exec_()  == QDialog.Accepted:
            self.textArea.document().print_(self.dialog.printer())

    def action(self):
        self.username = self.form_login.findChild(QLineEdit, "lineEdit")
        self.password = self.form_login.findChild(QLineEdit, "lineEdit_2")
        self.form_login.pushButton.clicked.connect(self.act_login)
        self.form_survey.pushButton.clicked.connect(self.act_survey)
        self.result.pushButton.clicked.connect(self.addToJson)
        btnPdf = self.result.findChild(QPushButton, "pushButton_2")
        btnPdf.clicked.connect(self.getText)

    def act_login(self):
        if self.username.text() == "" and self.password.text() == "":
            QMessageBox.warning(self, "Warning", "Please input username and password !")
        elif self.username.text() != "wahyu":
            QMessageBox.warning(self, "Warning", "Username or password wrong !")
        elif self.password.text() != "wahyu":
            QMessageBox.warning(self, "Warning", "Username or password wrong !")
        else:
            QMessageBox.information(self, "Info", "Login success ...")
            self.stackedLayout.setCurrentIndex(1)

    def act_survey(self):
        self.viewResult()
        self.stackedLayout.setCurrentIndex(2)

    def addToJson(self):
        Json = self.getDataJson()
        data = self.getValues()
        Json.append(data)
        toJson =  json.dumps(Json, indent=4)
        fwrite = open('data.json', 'w')
        fwrite.write(toJson)
        QMessageBox.information(self, "About", "Export to Json Success")


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
