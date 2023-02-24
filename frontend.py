import sys

from os import system
system("cls")

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QLabel,QPushButton,QComboBox,QCheckBox,QListWidget,QLineEdit

from PyQt5.QtGui import QFont

class RegistrationWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typingg.com Registration")
        self.setStyleSheet("background-color: #e6e6ff;")
        
        self.win_login = LoginWin()
        self.win_login.setGeometry(500,100,1200,800)
        
        
        self.h_box = QHBoxLayout()
        
        self.v_box = QVBoxLayout()
        self.v_box2 = QVBoxLayout()
        
        self.setLayout(self.h_box)
        
        self.appname = QListWidget()
        self.appname.addItem(" typingg.com")
        self.appname.setFixedSize(580, 350)
        self.appname.setStyleSheet("background-color: #6495ED;"
                                   "font-size: 40px;"
                                   "color: #FFFAFA;"
                                   "border: #e6f9ff;"
                                   "border-radius: 15px;")
        self.appname.setFont(QFont("Arial Rounded MT Bold",40))
        self.v_box.addWidget(self.appname)
        
        self.info_text = QListWidget()
        self.appname = QListWidget()
        

        self.info_text.addItem("""Learn the Foundations of\nTechnology, FREE!\n\nBuild essential skills with our comprehensive
                curriculum including keyboarding, digital
                literacy, and coding!""")
        self.info_text.setStyleSheet("background-color: #6495ED;"
                                   "font-size: 22px;"
                                   "border: #e6f9ff;"
                                   "border-radius: 15px;"
                                   "color: #FFFAFA;")
        self.info_text.setFixedSize(580, 440)
        self.info_text.setFont(QFont("Calibri"))
        self.v_box.addWidget(self.info_text)
        
        self.h_box.addLayout(self.v_box)
        
        self.Label_sign_up = QLabel("                     Sign Up")
        self.Label_sign_up.setStyleSheet("color: #00004d;"
                           "font-size: 40px;")
        self.Label_sign_up.setFont(QFont("Sitka Banner Semibold"))
        self.v_box2.addWidget(self.Label_sign_up)
        
        self.label_username = QLabel("Username*")
        self.v_box2.addWidget(self.label_username)
        self.label_username.setStyleSheet("color: #000066;"
                                           "font-size: 18px;")
        self.label_username.setFont(QFont("Sitka Banner Semibold"))
        
        self.edit_username = QLineEdit()
        self.edit_username.setPlaceholderText("Username")
        self.edit_username.setFont(QFont("Sitka Banner Semibold"))
        self.edit_username.setStyleSheet("border: 2px solid #00004d;"
                                          "border-radius: 10px;"
                                          "font-size: 20px;")
        self.v_box2.addWidget(self.edit_username)
        
        self.label_email = QLabel("Email*")
        self.label_email.setFont(QFont("Sitka Banner Semibold"))
        self.label_email.setStyleSheet("color: #000066;"
                                           "font-size: 18px;")
        self.v_box2.addWidget(self.label_email)
        
        self.edit_email = QLineEdit()
        self.edit_email.setPlaceholderText("Email")
        self.edit_email.setFont(QFont("Sitka Banner Semibold"))
        self.edit_email.setStyleSheet("border: 2px solid #00004d;"
                                          "border-radius: 10px;"
                                          "font-size: 20px;")
        self.v_box2.addWidget(self.edit_email)
        
        self.label_password = QLabel("Password*")
        self.label_password.setFont(QFont("Sitka Banner Semibold"))
        self.label_password.setStyleSheet("color: #000066;"
                                           "font-size: 18px;")
        self.v_box2.addWidget(self.label_password)
        
        self.edit_password = QLineEdit()
        self.edit_password.setPlaceholderText("Password")
        self.edit_password.setFont(QFont("Sitka Banner Semibold"))
        self.edit_password.setStyleSheet("border: 2px solid #00004d;"
                                          "border-radius: 10px;"
                                          "font-size: 20px;")
        self.v_box2.addWidget(self.edit_password)
        
        self.label_confirm_password = QLabel("Confirm password*")
        self.label_confirm_password.setFont(QFont("Sitka Banner Semibold"))
        self.label_confirm_password.setStyleSheet("color: #000066;"
                                           "font-size: 18px;")
        self.v_box2.addWidget(self.label_confirm_password)
        
        self.edit_confirm_password = QLineEdit()
        self.edit_confirm_password.setPlaceholderText("Confirm password")
        self.edit_confirm_password.setFont(QFont("Sitka Banner Semibold"))
        self.edit_confirm_password.setStyleSheet("border: 2px solid #00004d;"
                                          "border-radius: 10px;"
                                          "font-size: 20px;")
        self.v_box2.addWidget(self.edit_confirm_password)
        
        self.label_error = QLabel("Error")
        self.label_error.setFont(QFont("Sitka Banner Semibold"))
        self.label_error.setStyleSheet("font-size: 20px;")
        self.label_error.setStyleSheet("color: #e6e6ff;")
        self.v_box2.addWidget(self.label_error)
        
        self.v_box2.addSpacing(150)
        
        self.h_box2 = QHBoxLayout()
        
        self.login_btn = QPushButton("Log in")
        self.login_btn.setFont(QFont("Sitka Banner Semibold"))
        self.login_btn.setStyleSheet("border: 2px solid #00FFFF;"
                                        "border-radius: 15px;"
                                          "font-size: 35px;"
                                          "background-color: #7B68EE;")
        self.h_box2.addWidget(self.login_btn)
        self.login_btn.clicked.connect(self.Login_bos)
        
        self.register = QPushButton("Sign Up")
        self.register.setFont(QFont("Sitka Banner Semibold",20))
        self.register.setStyleSheet( "border: 2px solid #00FFFF;"
                                         "border-radius: 15px;"
                                          "font-size: 35px;"
                                          "background-color: #00FF7F;")
        self.h_box2.addWidget(self.register)
        self.register.clicked.connect(self.signup_bos)
        
        self.v_box2.addLayout(self.h_box2)
        self.v_box2.addSpacing(150)
    
                
        self.h_box.addSpacing(70)
        self.h_box.addLayout(self.v_box2)
        
    def Login_bos(self):
            self.close()
            self.win_login.show()
            
    def signup_bos(self):
        self.close()
        win_main.show()
        
        
class LoginWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typingg.com Log In")
        self.setStyleSheet("background-color: #e6e6ff;")
        
        
        self.h_box = QHBoxLayout()
        
        self.v_box = QVBoxLayout()
        self.v_box2 = QVBoxLayout()
        
        self.setLayout(self.h_box)
        
        self.appname = QListWidget()
        self.appname.addItem(" typingg.com")
        self.appname.setFixedSize(580, 350)
        self.appname.setStyleSheet("background-color: #6495ED;"
                                   "font-size: 40px;"
                                   "color: #FFFAFA;"
                                   "border: #e6f9ff;"
                                   "border-radius: 15px;")
        self.appname.setFont(QFont("Arial Rounded MT Bold",40))
        self.v_box.addWidget(self.appname)
        
        self.info_text = QListWidget()
        self.appname = QListWidget()
        

        self.info_text.addItem("""Learn the Foundations of\nTechnology, FREE!\n\nBuild essential skills with our comprehensive
        curriculum including keyboarding, digital
        literacy, and coding!""")
        self.info_text.setStyleSheet("background-color: #6495ED;"
                                   "font-size: 22px;"
                                   "border: #e6f9ff;"
                                   "border-radius: 15px;"
                                   "color: #FFFAFA;")
        self.info_text.setFixedSize(580, 440)
        self.info_text.setFont(QFont("Calibri"))
        self.v_box.addWidget(self.info_text)
        
        self.h_box.addLayout(self.v_box)
        
        self.Label_sign_up = QLabel("                     Log In")
        self.Label_sign_up.setStyleSheet("color: #00004d;"
                           "font-size: 40px;")
        self.Label_sign_up.setFont(QFont("Sitka Banner Semibold"))
        self.v_box2.addWidget(self.Label_sign_up)
        
        self.label_username = QLabel("Username*")
        self.v_box2.addWidget(self.label_username)
        self.label_username.setStyleSheet("color: #000066;"
                                           "font-size: 18px;")
        self.label_username.setFont(QFont("Sitka Banner Semibold"))
        
        self.edit_username = QLineEdit()
        self.edit_username.setPlaceholderText("Username")
        self.edit_username.setFont(QFont("Sitka Banner Semibold"))
        self.edit_username.setStyleSheet("border: 2px solid #00004d;"
                                          "border-radius: 10px;"
                                          "font-size: 20px;")
        self.v_box2.addWidget(self.edit_username)
        
        self.label_email = QLabel("Email*")
        self.label_email.setFont(QFont("Sitka Banner Semibold"))
        self.label_email.setStyleSheet("color: #000066;"
                                           "font-size: 18px;")
        self.v_box2.addWidget(self.label_email)
        
        self.edit_email = QLineEdit()
        self.edit_email.setPlaceholderText("Email")
        self.edit_email.setFont(QFont("Sitka Banner Semibold"))
        self.edit_email.setStyleSheet("border: 2px solid #00004d;"
                                          "border-radius: 10px;"
                                          "font-size: 20px;")
        self.v_box2.addWidget(self.edit_email)
        
        self.label_password = QLabel("Password*")
        self.label_password.setFont(QFont("Sitka Banner Semibold"))
        self.label_password.setStyleSheet("color: #000066;"
                                           "font-size: 18px;")
        self.v_box2.addWidget(self.label_password)
        
        self.edit_password = QLineEdit()
        self.edit_password.setPlaceholderText("Password")
        self.edit_password.setFont(QFont("Sitka Banner Semibold"))
        self.edit_password.setStyleSheet("border: 2px solid #00004d;"
                                          "border-radius: 10px;"
                                          "font-size: 20px;")
        self.v_box2.addWidget(self.edit_password)
        
        self.label_error = QLabel("Error")
        self.label_error.setFont(QFont("Sitka Banner Semibold"))
        self.label_error.setStyleSheet("font-size: 20px;")
        self.label_error.setStyleSheet("color: #e6e6ff;")
        self.v_box2.addWidget(self.label_error)
        
        self.v_box2.addSpacing(150)
        
        self.h_box2 = QHBoxLayout()
        
        self.register = QPushButton("Sign Up")
        self.register.setFont(QFont("Sitka Banner Semibold",20))
        self.register.setStyleSheet( "border: 2px solid #00FFFF;"
                                         "border-radius: 15px;"
                                          "font-size: 35px;"
                                          "background-color: #7B68EE;")
        self.register.clicked.connect(self.register_bos)
        
        self.h_box2.addWidget(self.register)
        
        self.login_btn = QPushButton("Log in")
        self.login_btn.setFont(QFont("Sitka Banner Semibold"))
        self.login_btn.setStyleSheet("border: 2px solid #00FFFF;"
                                        "border-radius: 15px;"
                                          "font-size: 35px;"
                                          "background-color: #00FF7F;")
        self.h_box2.addWidget(self.login_btn)
        self.login_btn.clicked.connect(self.login_bos)
        
        self.v_box2.addLayout(self.h_box2)
        self.v_box2.addSpacing(150)
    
                
        self.h_box.addSpacing(70)
        self.h_box.addLayout(self.v_box2)
        
    def register_bos(self):
        self.close()
        win_registration.show()
        
    def login_bos(self):
        self.close()
        win_main.show()
        
        
class PracticeWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label_typingg = QLabel("typingg.com",self)
        self.label_typingg.setStyleSheet("font-size: 40px;"
                                   "color: #1E90FF;")
        self.label_typingg.setFont(QFont("Arial Rounded MT Bold",40))
        self.label_typingg.move(40, 40)
        
        self.btn_speed_test = QPushButton("Practice",self)
        self.btn_speed_test.setStyleSheet("font-size: 30px;"
                                          "border: 2px solid #e6e6ff;")
        self.btn_speed_test.setFont(QFont("Sitka Banner Semibold"))
        self.btn_speed_test.move(500, 40)
        
        self.btn_speed_test = QPushButton("Speed Test",self)
        self.btn_speed_test.setStyleSheet("font-size: 30px;"
                                          "border: 2px solid #e6e6ff;")
        self.btn_speed_test.setFont(QFont("Sitka Banner Semibold"))
        self.btn_speed_test.move(650, 40)
        
        self.btn_speed_test = QPushButton("Change language\nto uzbek🌐",self)
        self.btn_speed_test.setStyleSheet("font-size: 23px;"
                                          "border: 2px solid #e6e6ff;")
        self.btn_speed_test.setFont(QFont("Sitka Banner Semibold"))
        self.btn_speed_test.move(830, 33)
        
        self.label_username = QLabel("userName",self)
        self.label_username.move(112, 115)
        self.label_username.setStyleSheet("font-size: 30px;")
        self.label_username.setFont(QFont("Sitka Banner Semibold"))
        
        self.btn_level = QPushButton("1",self)
        self.btn_level.setStyleSheet("font-size: 20px;"
                                     "background-color: #DDA0DD;"
                                     "border: 2px  solid #DAA520;"
                                     "border-radius: 25px;")
        self.btn_level.setFixedSize(60, 60)
        self.btn_level.move(40, 110)
        
        self.btn_tcoin = QPushButton("TC",self)
        self.btn_tcoin.setStyleSheet("background-color: #ffd633;"
                                     "color: #ffff99;"
                                     "border: 2px solid #b38f00;"
                                     "border-radius: 20px;"
                                     "font-size: 20px;")
        self.btn_tcoin.setFont(QFont("Sitka Banner Semibold"))
        self.btn_tcoin.setFixedSize(40, 40)
        self.btn_tcoin.move(1120, 115)
        
        self.label_balance = QLabel("000",self)
        self.label_balance.setStyleSheet("font-size: 20px;")
        self.label_balance.move(1080, 125)
        
        
        
        
app=QApplication(sys.argv)
win_registration = RegistrationWin()
win_main = PracticeWindow()
win_main.setStyleSheet('background-color: #e6e6ff;')
win_registration.setGeometry(500,100,1200,800)
win_main.setGeometry(500, 100, 1200, 800)