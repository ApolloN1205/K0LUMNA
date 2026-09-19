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
print('If at any moment you wish to return to the main menu, return to nil via "0" ')
print('-----------------------------------------')
#Looping menu for user selection
while True:
    Selection = int(input('Please select an option: '))
    if Selection == 1:
        CoreTraining = ['Core-001','Core-002','Core-003'] #Array containing the core training modules
        Cindex = len(CoreTraining) - 1 #Index for the core training array
        #Core training menu
        print('You have selected Training.')
        print('-----------------------------------------')
        print('Core Training Modules')
        print('-----------------------------------------')
        #Looping menu for user selection of core training modules
        for i in range (len(CoreTraining)):
            print(CoreTraining[i])
        while True:
            CoreSelection = int(input('Please select a Core Training Module to investigate: '))
            if CoreSelection >= 1 and CoreSelection <= len(CoreTraining):
                print('You have selected ' + CoreTraining[CoreSelection - 1] + '.')
                break
            elif CoreSelection < 0 or CoreSelection > len(CoreTraining):
                print('Invalid selection. Please try again.')
            elif CoreSelection == 0:
                print('You have chosen to exit.')
                break
    elif Selection == 2: #The spinal cord, containing test labs
        Vertebrae = ['Vertebra-001','Vertebra-002','Vertebra-003'] #Array containing the vertebrae (labs) for investigation
        Vindex = len(Vertebrae) - 1 #Index for the vertebrae array
        #Spinal cord investigation menu
        print('You have selected SOC Investigation.')
        print('-----------------------------------------')
        print('The Spinal Cord')
        print('-----------------------------------------')
        #Looping menu for user selection of vertebrae (labs)
        for i in range (len(Vertebrae)):
            print(Vertebrae[i])
        while True:
            VertebraeSelection = int(input('Please select a Vertebrae (Lab) to investigate: '))
            if VertebraeSelection >= 1 and VertebraeSelection <= len(Vertebrae):
                print('You have selected ' + Vertebrae[VertebraeSelection - 1] + '.')
                break
            elif VertebraeSelection < 0 or VertebraeSelection > len(Vertebrae):
                print('Invalid selection. Please try again.')
            elif VertebraeSelection == 0:
                print('You have chosen to exit.')
                break
    elif Selection == 3: #Progress Report(s)
        print('You have selected Progress Report(s).')
        UserProfile = ['','',''] #Array containing the user profile information
        print('-----------------------------------------')
        print('User Profile')
        print('-----------------------------------------')
        break
    elif Selection == 4: #Exit
        print('You have chosen to exit.')
        break
    else:
        print('Invalid selection. Please try again.')
