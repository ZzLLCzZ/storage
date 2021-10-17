import BigNumber
import SeededRand
import GameController

class Data:
    def __init__(self, id):
        self.id = id
        self.level = 0
        self.current = 0
        self.max_storage = 1000
        self.stored_value = 0
        self.upgrade_points = 0

        s_list = GameController.GetAllOf("slider")

        self.stored_mod = s_list[len(s_list) - 1].id - 1

        self.prestige_currency = str(BigNumber(self.p_currency))
        self.up_points = "UP:" + str(BigNumber(self.upgrade_points))


def onLoad():
    return  "Success Loading"

def onUnload():
    return "Success Unloading"

def createModule(id):
    data = Data(id)
    data.result = "Created Template"

    return data

def tick(data):

    return data

def bulkTick(data, amount):

    return data

def destroyModule(data):
    return data

def onPrestige(data):
    data.upgrade_points += 1

    return data

def loadSave(save, id):
    data = createModule(id)
    data.level = int(save.split(",")[0])
    data.goal = float(save.split(",")[1])
    data.p_currency = int(save.split(",")[2])

    return data

def saveData(data):
    result = ""
    result += str(data.level) + ","
    result += str(data.goal) + ","
    result += str(data.p_currency)

    return result

"""
END special functions
"""

def upgrade_storage(data):
    data.max_storage += 1000

    GameController.GetSlider(data.stored_mod).value -= data.level * 5000

    data.level += 1

    return data

def upgrade_storage_avail(data):
    return data.level * 5000 < GameController.GetSlider(data.stored_mod).value
