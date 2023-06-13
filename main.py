import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow
from ui_newrec import Ui_Dialog
from connection import Data

class MegaCRUD(QMainWindow):
    def __init__(self):
        super(MegaCRUD, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.btn_newrec.clicked.connect(self.open_new_record_window)
        self.ui.btn_editrec.clicked.connect(self.open_new_record_window)
        self.ui.btn_delrec.clicked.connect(self.delete_current_record)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('contacts')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_record_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "New":
            self.ui_window.btn_saverec.clicked.connect(self.add_new_record)
        else:
            self.ui_window.btn_saverec.clicked.connect(self.edit_current_record)

    def add_new_record(self):
        fname = self.ui_window.le_fname.text()
        sname = self.ui_window.le_sname.text()
        phone = self.ui_window.le_pnumber.text()
        self.conn.add_new_record_query(fname, sname, phone)
        self.view_data()
        self.new_window.close()

    def edit_current_record(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        fname = self.ui_window.le_fname.text()
        sname = self.ui_window.le_sname.text()
        phone = self.ui_window.le_pnumber.text()
        self.conn.update_record_query(fname, sname, phone, id)
        self.view_data()
        self.new_window.close()

    def delete_current_record(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        self.conn.delete_record_query(id)
        self.view_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MegaCRUD()
    window.show()

    sys.exit(app.exec())
