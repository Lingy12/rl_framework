from cmath import phase
import xml.etree.ElementTree as ET

#assume parameters is a list of dictionary
#add some dummy value to test
param = [{'duration': '33', 'state': 'GGGrrrGGGrrrrrr'},
        {'duration': '6', 'state': 'yyyrrryyyrrrrrr'},
        {'duration': '33', 'state': 'rrrGGGrrrrrrrrr'},
        {'duration': '6', 'state': 'rrryyyrrrrrrrrr'},
        {'duration': '33', 'state': 'rrrrrrrrrGGGGGG'},
        {'duration': '6', 'state': 'rrrrrrrrryyyyyy'}]

def update(param_out):
    mytree = ET.parse('intersection.add.xml')
    myroot = mytree.getroot()

    i = 0
    for phase in myroot.iter('phase'):

        # phase.find('duration').text = str(float(phase.find('duration').text)+10)

        phase.set('duration', param_out[i]['duration'])
        phase.set('state', param_out[i]['state'])
        i += 1

    # mytree.write('output1.xml')
    mytree.write('intersection.add.xml')

# if __name__ == '__main__':
#     updater(param)