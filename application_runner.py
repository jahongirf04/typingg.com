import frontend,data_base_connection

import sys

from PyQt5.QtWidgets import QApplication

app=QApplication(sys.argv)
Win=frontend.RegistrationWin()
Win.setStyleSheet('background-color: #e6e6ff;')
Win.setGeometry(500,100,1200,800)
Win.show()
sys.exit(app.exec_())