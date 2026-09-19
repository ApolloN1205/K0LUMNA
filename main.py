#K-0 shell, introduction menu

print('-----------------------------------------')
print('K0LUMNA - The Backbone of SOC Operations')
print('-----------------------------------------')
print('K-0 Core status : Online')
print('Selection Menu:')
print('[1] - Training')
print('[2] - SOC Investigation')
print('[3] - Progress Report(s)')
print('[4] - Exit')
print('-----------------------------------------')
#Looping menu for user selection
while True:
    Selection = int(input('Please select an option: '))
    if Selection == 1:
        print('You have selected Training.')
        break
    elif Selection == 2: #The spinal cord, containing test labs
        Vertebrae = ['Vertebra-001','Vertebra-002','Vertebra-003','Vertebra-004','Vertebra-005','Vertebra-006','Vertebra-007','Vertebra-008','Vertebra-009','Vertebra-010'] #Array containing the vertebrae (labs) for investigation
        #Spinal cord investigation menu
        print('You have selected SOC Investigation.')
        print('-----------------------------------------')
        print('The Spinal Cord')
        print('-----------------------------------------')
        #Looping menu for user selection of vertebrae (labs)
        for V in range (len(Vertebrae)):
            print(Vertebrae[V])
        while True:
            VertebraeSelection = int(input('Please select a Vertebrae (Lab) to investigate: '))
            if VertebraeSelection == ('001') or VertebraeSelection == (1):
                print('You have selected Vertebra-001.')
                break
            elif VertebraeSelection == ('002') or VertebraeSelection == (2):
                print('You have selected Vertebra-002.')
                break
            elif VertebraeSelection == ('003') or VertebraeSelection == (3):
                print('You have selected Vertebra-003.')
                break
            elif VertebraeSelection == ('004') or VertebraeSelection == (4):
                print('You have selected Vertebra-004.')
                break
            elif VertebraeSelection == ('005') or VertebraeSelection == (5):
                print('You have selected Vertebra-005.')
                break
            elif VertebraeSelection == ('006') or VertebraeSelection == (6):
                print('You have selected Vertebra-006.')
                break
            elif VertebraeSelection == ('007') or VertebraeSelection == (7):
                print('You have selected Vertebra-007.')
                break
            elif VertebraeSelection == ('008') or VertebraeSelection == (8):
                print('You have selected Vertebra-008.')
                break
            elif VertebraeSelection == ('009') or VertebraeSelection == (9):
                print('You have selected Vertebra-009.')
                break
            elif VertebraeSelection == ('010') or VertebraeSelection == (10):
                print('You have selected Vertebra-010.')                    
                break
            else:
                print('Invalid selection. Please try again.')
        break
    elif Selection == 3:
        print('You have selected Progress Report(s).')
        break
    elif Selection == 4:
        print('You have chosen to exit.')
        break
    else:
        print('Invalid selection. Please try again.')



