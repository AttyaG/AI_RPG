from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt6.QtCore import QSize, Qt
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
import pandas as pd

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()

        self.setWindowTitle('QD')

        self.gameWindow = GameWindow()
        
        self.additionalWindow = None

        self.label = QLabel(text='label')
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.continueButton = QPushButton('Continue')
        self.continueButton.clicked.connect(self.continueGame)
        
        self.newGameButton = QPushButton('New Game')
        self.newGameButton.setCheckable(True)
        self.newGameButton.clicked.connect(self.newGame)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.continueButton)
        self.layout.addWidget(self.newGameButton)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def newGame(self):
        print('New Game')
        self.hide()
        #self.additionalWindow = GeneralWindow('Create new Character', 'CreateNewCharacter.ui')
        #self.additionalWindow.createCharacterHandle()
        self.additionalWindow = CharacterCreator()
        self.additionalWindow.show()
        #self.gameWindow.showMaximized()

    def continueGame(self):
        print('Continue')

class GameWindow(QWidget):
    def __init__(self):
        super(GameWindow, self).__init__()

        # добавлю окно, которое будет общим
        # генерироватся при вызове метода
        # ui нет проблем загрузить
        # а что делать с методами
        self.generalWindow = None
        
        self.ui = uic.loadUi('gameScene.ui', self)

        self.ui.AIDialogButton.clicked.connect(self.startAIDialog)
        self.ui.saveGameButton.clicked.connect(self.saveGame)

        #pixmap = QPixmap('adventurers_guild_rs.png')
        #ui.label.setPixmap(pixmap)
        #ui.label.resize(pixmap.width(), pixmap.height())

    def startAIDialog(self):
        self.generalWindow = GeneralWindow('AI Dialog', 'AIDialog.ui')
        self.generalWindow.show()
        self.generalWindow.aiDialogHandle()

    def saveGame(self):
        pass

    
        
class GeneralWindow(QWidget):
    def __init__(self, title=None, ui_file='generalScene.ui'):
        super(GeneralWindow, self).__init__()
        self.setWindowTitle(title)
        self.ui = uic.loadUi(ui_file, self)

    def aiDialogHandle(self):
        self.ui.pushButton.clicked.connect(lambda : self.ui.textBrowser.setText("TextBrower\'s text set"))

class CharacterCreator(QWidget):
    def __init__(self):
        super(CharacterCreator, self).__init__()
        self.ui = uic.loadUi('CreateNewCharacter.ui', self)

        self.ui.createButton.clicked.connect(self.createCharacter)
        self.stats_data = pd.read_csv('game_data\stats.csv')
        self.roles = pd.read_csv(r'game_data\roles_by_race.csv')

        self.ui.raceCombo.addItems(self.stats_data['race'][self.stats_data['playable']])
        race = self.ui.raceCombo.currentText()

        self.ui.raceCombo.currentTextChanged.connect(self.raceChanged)
        self.ui.roleCombo.addItems(self.roles[race].dropna())
    def createCharacter(self):
        character_dict = {}
        character_dict['name'] = self.ui.lineEdit.text()
        character_dict['role'] = self.ui.roleCombo.currentText()
        print(character_dict)

    def raceChanged(self):
        # update roles
        self.ui.roleCombo.clear()
        race = self.ui.raceCombo.currentText()
        self.ui.roleCombo.addItems(self.roles[race].dropna())
        # update stats
        hp = self.stats_data["hp"][self.stats_data["race"]==race].iloc[0]
        power = self.stats_data["power"][self.stats_data["race"]==race].iloc[0]
        energy = self.stats_data["energy"][self.stats_data["race"]==race].iloc[0]
        mana = self.stats_data["mana"][self.stats_data["race"]==race].iloc[0]
        a = 'an' if race=='Elf' else 'a'
        hp_text = f'Health of {a} {race} is {hp}'
        p_text = f'Power of {a} {race} is {power}'
        e_text = f'Energy of {a} {race} is {energy}'
        m_text = f'Mana of {a} {race} is {mana}'
        self.ui.hp_label.setText(hp_text)
        self.ui.power_label.setText(p_text)
        self.ui.energy_label.setText(e_text)
        self.ui.mana_label.setText(m_text)

    def roleChanged(self):
        pass
        
'''
app = QApplication([])
qss="style.qss"
with open(qss,"r") as fh:
    app.setStyleSheet(fh.read())

window = MainMenu()
window.show()

app.exec()
'''
