__author__ = 'user'

class Pet(object):
    def __init__(self):

        self.id=None
        self.kinds=None
        self.kinds_kinds = None
        self.is_free=None
        self.gender=None
        self.is_Neutralization = None
        self.weight = None
        self.height = None
        self.helth = None
        self.uid = None

    @classmethod
    def create_from_request(cls, request_data):
        pet = None
        if 'is_free' in request_data:
            if request_data['is_free']=='O':
                pet=FreePet()
                pet.is_free=1
            else:
                pet=NFreePet()
                pet.is_free=0

        pet.kinds=request_data['kinds']
        if 'kinds_kinds' in request_data:
            pet.kinds_kinds=request_data['kinds_kinds']

        if 'gender' in request_data:
            if request_data['gender']=='male':
                pet.gender=1
            else:
                pet.gender=0
        if 'is_Neutralization' in request_data:
            if request_data['is_Neutralization']=='O':
                pet.is_Neutralization=1
            else:
                pet.is_Neutralization=0
        if 'weight' in request_data:
            pet.weight=int(request_data['weight'])
        if 'height' in request_data:
            pet.height=int(request_data['height'])
        if 'helth' in request_data:
            pet.helth=request_data['helth']

        return pet

    @classmethod
    def create_from_dbdata(cls, dbdata):
        pet = None

        if dbdata[3] == 1:
            pet = FreePet()
            pet.is_free = dbdata[3]
        else:
            pet = NFreePet()
            pet.is_free = dbdata[3]
        pet.id=dbdata[0]
        pet.kinds = dbdata[1]
        pet.kinds_kinds = dbdata[2]
        pet.price = 0
        pet.gender = dbdata[5]
        pet.is_Neutralization = dbdata[6]
        pet.weight = dbdata[7]
        pet.height = dbdata[8]
        pet.helth = dbdata[9]
        pet.uid = dbdata[10]

        return pet

    @classmethod
    def makeDicByPet(cls, pet):
        dic = {'id': pet.id, 'kinds': pet.kinds, 'kinds_kinds': pet.kinds_kinds, 'is_free': pet.is_free,
               'price': pet.price, 'gender': pet.gender, 'is_Neutralization':pet.is_Neutralization, 'weight':pet.weight,
               'height':pet.height,'helth':pet.helth,'uid':pet.uid}
        return dic


class NFreePet(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.price = None

    @classmethod
    def create_from_request(cls, request_data):
        npet = NFreePet()
        npet.kinds = request_data['kinds']
        if 'kinds_kinds' in request_data:
            npet.kinds_kinds = request_data['kinds_kinds']
        if 'is_free' in request_data:
            if request_data['is_free'] == 'O':
                npet.is_free = 1
            else:
                npet.is_free = 0
        if 'price' in request_data:
            npet.price = int(request_data['price'])
        if 'gender' in request_data:
            if request_data['gender'] == 'male':
                npet.gender = 1
            else:
                npet.gender = 0
        if 'is_Neutralization' in request_data:
            if request_data['is_Neutralization'] == 'O':
                npet.is_Neutralization = 1
            else:
                npet.is_Neutralization = 0
        if 'weight' in request_data:
            npet.weight = int(request_data['weight'])
        if 'height' in request_data:
            npet.height = int(request_data['height'])
        if 'helth' in request_data:
            npet.helth = request_data['helth']

        return npet

    @classmethod
    def create_from_dbdata(cls, dbdata):
        npet = NFreePet()
        npet.id = dbdata[0]
        npet.kinds = dbdata[1]
        npet.kinds_kinds = dbdata[2]
        npet.is_free = dbdata[3]
        npet.price = dbdata[4]
        npet.gender = dbdata[5]
        npet.is_Neutralization = dbdata[6]
        npet.weight = dbdata[7]
        npet.height = dbdata[8]
        npet.helth = dbdata[9]
        npet.uid = dbdata[10]

        return npet

    @classmethod
    def makeDicByPet(cls, npet):
        dic = {'id': npet.id, 'kinds': npet.kinds, 'kinds_kinds': npet.kinds_kinds, 'is_free': npet.is_free,
               'price': npet.price, 'gender': npet.gender, 'is_Neutralization': npet.is_Neutralization,
               'weight': npet.weight,
               'height': npet.height, 'helth': npet.helth, 'uid': npet.uid}
        return dic



class FreePet(Pet):
    def __init__(self):
        Pet.__init__(self)

