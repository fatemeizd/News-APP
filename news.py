# Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from newsdataapi import NewsDataApiClient

# Base Structure
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 688)
        MainWindow.setStyleSheet("background-color: rgb(126, 220, 85);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.news_label = QtWidgets.QLabel(self.centralwidget)
        self.news_label.setGeometry(QtCore.QRect(60, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.news_label.setFont(font)
        self.news_label.setStyleSheet("color: rgb(255, 10, 75);")
        self.news_label.setObjectName("news_label")
        self.query_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.query_lineEdit.setGeometry(QtCore.QRect(160, 20, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.query_lineEdit.setFont(font)
        self.query_lineEdit.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(9, 80, 5);\n"
"border-radius: 10px;\n"
"")
        self.query_lineEdit.setObjectName("query_lineEdit")
        self.search_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.get_news())
        self.search_pushButton.setGeometry(QtCore.QRect(567, 20, 91, 31))
        self.search_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.search_pushButton.setStyleSheet("background-color: rgb(0, 112, 0);\n"
"font: 10pt \"Segoe Print\";\n"
"color: rgb(170, 244, 255);\n"
"border-radius: 15px;")
        self.search_pushButton.setObjectName("search_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 704, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear())
        self.clear_pushButton.setGeometry(QtCore.QRect(260, 580, 121, 23))
        self.clear_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.clear_pushButton.setStyleSheet("color: rgb(170, 255, 127);\n"
"font: 10pt \"Segoe Print\";\n"
"background-color: rgb(78, 106, 106);")
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.art1_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.art1_listWidget.setGeometry(QtCore.QRect(0, 151, 701, 171))
        self.art1_listWidget.setObjectName("art1_listWidget")
        self.title1_label = QtWidgets.QLabel(self.centralwidget)
        self.title1_label.setGeometry(QtCore.QRect(0, 70, 701, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        self.title1_label.setFont(font)
        self.title1_label.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(172, 255, 239);\n"
"border-radius: 10px;")
        self.title1_label.setObjectName("title1_label")
        self.date1_label = QtWidgets.QLabel(self.centralwidget)
        self.date1_label.setGeometry(QtCore.QRect(0, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.date1_label.setFont(font)
        self.date1_label.setStyleSheet("color: rgb(172, 255, 239); \n"
"background-color:rgb(0, 85, 0);\n"
"border-radius: 10px;")
        self.date1_label.setObjectName("date1_label")
        self.authors1_label = QtWidgets.QLabel(self.centralwidget)
        self.authors1_label.setGeometry(QtCore.QRect(200, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.authors1_label.setFont(font)
        self.authors1_label.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(172, 255, 239);\n"
"border-radius: 10px;")
        self.authors1_label.setObjectName("authors1_label")
        self.taccount1_label = QtWidgets.QLabel(self.centralwidget)
        self.taccount1_label.setGeometry(QtCore.QRect(500, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.taccount1_label.setFont(font)
        self.taccount1_label.setStyleSheet("color: rgb(172, 255, 239); \n"
"background-color:rgb(0, 85, 0);\n"
"border-radius: 10px;")
        self.taccount1_label.setObjectName("taccount1_label")
        self.title2_label = QtWidgets.QLabel(self.centralwidget)
        self.title2_label.setGeometry(QtCore.QRect(0, 330, 701, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        self.title2_label.setFont(font)
        self.title2_label.setStyleSheet("color: rgb(172, 255, 239); \n"
"background-color:rgb(0, 85, 0);\n"
"border-radius: 10px;")
        self.title2_label.setObjectName("title2_label")
        self.date2_label = QtWidgets.QLabel(self.centralwidget)
        self.date2_label.setGeometry(QtCore.QRect(0, 370, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.date2_label.setFont(font)
        self.date2_label.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(172, 255, 239);\n"
"border-radius: 10px;")
        self.date2_label.setObjectName("date2_label")
        self.authors2_label = QtWidgets.QLabel(self.centralwidget)
        self.authors2_label.setGeometry(QtCore.QRect(200, 370, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.authors2_label.setFont(font)
        self.authors2_label.setStyleSheet("color: rgb(172, 255, 239); \n"
"background-color:rgb(0, 85, 0);\n"
"border-radius: 10px;")
        self.authors2_label.setObjectName("authors2_label")
        self.taccount2_label = QtWidgets.QLabel(self.centralwidget)
        self.taccount2_label.setGeometry(QtCore.QRect(490, 370, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.taccount2_label.setFont(font)
        self.taccount2_label.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(172, 255, 239);\n"
"border-radius: 10px;")
        self.taccount2_label.setObjectName("taccount2_label")
        self.art2_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.art2_listWidget.setGeometry(QtCore.QRect(0, 410, 701, 171))
        self.art2_listWidget.setObjectName("art2_listWidget")
        self.link1_label = QtWidgets.QLabel(self.centralwidget)
        self.link1_label.setGeometry(QtCore.QRect(10, 610, 691, 20))
        self.link1_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.link1_label.setStyleSheet("color: rgb(78, 106, 106);\n"
"font: 8pt \"Segoe Print\";")
        self.link1_label.setText("")
        self.link1_label.setObjectName("link1_label")
        self.link2_label = QtWidgets.QLabel(self.centralwidget)
        self.link2_label.setGeometry(QtCore.QRect(10, 640, 691, 20))
        self.link2_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.link2_label.setStyleSheet("color: rgb(78, 106, 106);\n"
"font: 8pt \"Segoe Print\";")
        self.link2_label.setText("")
        self.link2_label.setOpenExternalLinks(True)
        self.link2_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByMouse)
        self.link2_label.setObjectName("link2_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_news(self):
        query = self.query_lineEdit.text()
        URL = f'https://api.newscatcherapi.com/v2/search?q=\"{query}\"&lang=en'
        payload={}
        headers = {
          'X-API-KEY': 'Ioppqq-NWFAxHbIAApJ69DXqEPUNp1zu7CWE0T1OakY'
        }
     
        r = requests.get(URL, headers=headers, data=payload)
        res = r.json()
        print(res)

        title_1 = res['articles'][0]['title']
        published_date1 = res['articles'][0]['published_date']
        link_1 = res['articles'][0]['link']
        summary_1 = res['articles'][0]['summary']
        authors_1 = res['articles'][0]['authors']
        twitter_account1 = res['articles'][0]['twitter_account']

        self.title1_label.setText(f'{title_1}')
        self.date1_label.setText(f'{published_date1}')
        self.link1_label.setText(f'{link_1}')
        self.art1_listWidget.addItem(f'{summary_1}')
        self.authors1_label.setText(f'{authors_1}')
        if twitter_account1 == '@' or 'None':
            self.taccount1_label.setText('There is no account')
        else:
            self.taccount1_label.setText(f'{twitter_account1}')


        title_2 = res['articles'][1]['title']
        published_date2 = res['articles'][1]['published_date']
        link_2 = res['articles'][1]['link']
        summary_2 = res['articles'][1]['summary']
        authors_2 = res['articles'][1]['authors']
        twitter_account2 = res['articles'][1]['twitter_account']

        self.title2_label.setText(f'{title_2}')
        self.date2_label.setText(f'{published_date2}')
        self.link2_label.setText(f'{link_2}')
        self.art2_listWidget.addItem(f'{summary_2}')
        self.authors2_label.setText(f'{authors_2}')
        
        if twitter_account2 == '@' or 'None':
            self.taccount2_label.setText('There is no account')
        else:
            self.taccount2_label.setText(f'{twitter_account2}')
            

    def clear(self):
        self.title1_label.clear()
        self.date1_label.clear()
        self.authors1_label.clear()
        self.taccount1_label.clear()
        self.art1_listWidget.clear()
        self.link1_label.clear()
        self.title2_label.clear()
        self.date2_label.clear()
        self.authors2_label.clear()
        self.taccount2_label.clear()
        self.art2_listWidget.clear()
        self.link2_label.clear()
        self.query_lineEdit.clear()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "News App"))
        self.news_label.setText(_translate("MainWindow", "Query:"))
        self.search_pushButton.setText(_translate("MainWindow", "Search"))
        self.clear_pushButton.setText(_translate("MainWindow", "Clear Content"))
        self.title1_label.setText(_translate("MainWindow", "Title Of Article1"))
        self.date1_label.setText(_translate("MainWindow", "Published_Date"))
        self.authors1_label.setText(_translate("MainWindow", "Authors"))
        self.taccount1_label.setText(_translate("MainWindow", "Twitter_Account"))
        self.title2_label.setText(_translate("MainWindow", "Title Of Article2"))
        self.date2_label.setText(_translate("MainWindow", "Published_Date"))
        self.authors2_label.setText(_translate("MainWindow", "Authors"))
        self.taccount2_label.setText(_translate("MainWindow", "Twitter_Account"))



# Initialize the app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
