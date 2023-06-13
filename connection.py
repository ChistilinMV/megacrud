from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('contacts_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS contacts (ID integer primary key AUTOINCREMENT, "
                   "FName VARCHAR(20), SName VARCHAR(20), Phone VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

    def add_new_record_query(self, fname, sname, phone):
        sql_query = "INSERT INTO contacts (FName, SName, Phone) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [fname, sname, phone])

    def update_record_query(self,  fname, sname, phone, id):
        sql_query = "UPDATE contacts SET FName=?, SName=?, Phone=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [fname, sname, phone, id])

    def delete_record_query(self, id):
        sql_query = "DELETE FROM contacts WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

