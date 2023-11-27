from XIANG import XIANG
import utils
import sys
from Ui_MainWindow import Ui_Dialog
from PyQt6 import QtCore, QtGui, QtWidgets
from initialize import initialization

class Logic_MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    xiang = None

    startSignal = QtCore.pyqtSignal()
    clearSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Logic_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.startSignal.connect(self.liuYaoDivining)
        self.start_pushButton.clicked.connect(self.emitStartSignal)
        
        self.clearSignal.connect(self.clearPage)
        self.clear_pushButton.clicked.connect(self.emitClearSignal)

        self.exit_pushButton.clicked.connect(self.close)

    def emitStartSignal(self):
        self.startSignal.emit()
    
    def emitClearSignal(self):
        self.clearSignal.emit()

    def liuYaoDivining(self):
        question = self.question_lineEdit.text()
        sex = self.sex_comboBox.currentText()
        if question=='' or sex=='':
            message = QtWidgets.QMessageBox
            message.about(self,"警告","请确保完整填写所占事项与卦主性别")
            return
        
        self.xiang = initialization(question, sex)
        # 本卦推变卦
        utils.deriveChange(self.xiang)
        # 寻世应
        utils.seekForEgo(self.xiang)
        # 纳甲
        utils.matchSkyandEarch(self.xiang)
        # 寻卦宫，定六亲
        utils.seekForReps(self.xiang)
        # 缺六亲
        utils.seekForDefects(self.xiang)
        # 寻六神
        utils.seekForSouls(self.xiang)
        # 输出
        self.showUI()
        return

    def showUI(self):
        self.showDate()
        self.showSoul()
        self.showBaseReps()
        self.showBaseYAOs()
        self.showEgo()
        self.showChangeReps()
        self.showChangeYAOs()
        return

    def showDate(self):
        year = self.xiang.year
        month = self.xiang.month
        day = self.xiang.day
        hour = self.xiang.hour
        lacks = self.xiang.lacks
        date = ''
        date += year[0].value + year[1].value + '年，'
        date += month[0].value + month[1].value + '月，'
        date += day[0].value + day[1].value + '日，'
        date += hour[0].value + hour[1].value + '时   '
        date += '(空亡：' + lacks[0].value + lacks[1].value + ')'
        
        self.date_label.setText(date)
        return

    def showSoul(self):
        yaos = self.xiang.base.yaos
        widgets = [self.soul_1, self.soul_2, self.soul_3, self.soul_4, self.soul_5, self.soul_6]
        for i in range(6):
            soul = yaos[i].soul
            widgets[i].setText(soul.value)
        return

    def showBaseReps(self):
        yaos = self.xiang.base.yaos
        widgets = [self.base_rep_1, self.base_rep_2, self.base_rep_3, self.base_rep_4, self.base_rep_5, self.base_rep_6]
        for i in range(6):
            rep = yaos[i].representation
            najia = yaos[i].najia
            text = rep.value + najia[0].value + najia[1].value
            widgets[i].setText(text)
        return

    def showBaseYAOs(self):
        yaos = self.xiang.base.yaos
        widgets = [self.base_yao_1, self.base_yao_2, self.base_yao_3, self.base_yao_4, self.base_yao_5, self.base_yao_6]
        for i in range(6):
            if yaos[i].essence == 0:
                text = '▅▅▅▅▅▅▅▅  ▅▅▅▅▅▅▅▅'
            elif yaos[i].essence == 1:
                text = '▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅'
            widgets[i].setText(text)
        return

    def showEgo(self):
        yaos = self.xiang.base.yaos
        widgets = [self.ego_1, self.ego_2, self.ego_3, self.ego_4, self.ego_5, self.ego_6]
        for i in range(6):
            text = ['   ', ' ', ' ', '   ']
            if yaos[i].feature == 0:
                text[0] = '变'
            if yaos[i].ego == 1:
                text[3] = '世'
            if yaos[i].other == 1:
                text[3] = '应'
            t = ''
            for j in text:
                t += str(j)
            widgets[i].setText(t)
            widgets[i].setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        return

    def showChangeReps(self):
        widgets = [self.change_rep_1, self.change_rep_2, self.change_rep_3, self.change_rep_4, self.change_rep_5, self.change_rep_6]
        if self.xiang.flag == 0:
            for w in widgets:
                w.setText('')
            return
        yaos = self.xiang.change.yaos
        for i in range(6):
            rep = yaos[i].representation
            najia = yaos[i].najia
            text = rep.value + najia[0].value + najia[1].value
            widgets[i].setText(text)
        return

    def showChangeYAOs(self):
        widgets = [self.change_yao_1, self.change_yao_2, self.change_yao_3, self.change_yao_4, self.change_yao_5, self.change_yao_6]
        if self.xiang.flag == 0:
            for w in widgets:
                w.setText('')
            return
        yaos = self.xiang.change.yaos
        for i in range(6):
            if yaos[i].essence == 0:
                text = '▅▅▅▅▅▅▅▅  ▅▅▅▅▅▅▅▅'
            elif yaos[i].essence == 1:
                text = '▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅'
            widgets[i].setText(text)
        return

    def clearPage(self):
        self.question_lineEdit.setText('')
        self.sex_comboBox.setCurrentIndex(-1)
        self.date_label.setText('')
        widgets = [self.soul_1, self.soul_2, self.soul_3, self.soul_4, self.soul_5, self.soul_6, 
                   self.base_rep_1, self.base_rep_2, self.base_rep_3, self.base_rep_4, self.base_rep_5, self.base_rep_6, 
                   self.base_yao_1, self.base_yao_2, self.base_yao_3, self.base_yao_4, self.base_yao_5, self.base_yao_6, 
                   self.ego_1, self.ego_2, self.ego_3, self.ego_4, self.ego_5, self.ego_6, 
                   self.change_rep_1, self.change_rep_2, self.change_rep_3, self.change_rep_4, self.change_rep_5, self.change_rep_6, 
                   self.change_yao_1, self.change_yao_2, self.change_yao_3, self.change_yao_4, self.change_yao_5, self.change_yao_6
                   ]
        for w in widgets:
            w.setText('')
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Logic_MainWindow()
    win.show()
    sys.exit(app.exec())