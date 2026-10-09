#K-0 shell, introduction menu
dash = '-----------------------------------------' #Divider for the menu, ensures all divisions are same length
print(dash)
print('K0LUMNA - The Backbone of SOC Operations')
print(dash)
print('K-0 Core status : Online')
print('Selection Menu:')
print('[1] - Training')
print('[2] - SOC Investigation')
print('[3] - Progress Report(s)')
print('[4] - Exit')
print(dash)
print('If at any moment you wish to return to the main menu, return to nil via "0" ')
print(dash)
#Looping menu for user selection
while True:
    def SubMenuPrint(menuname):
          print('You have selected ' + menuname + '.')
          print(dash)
          print(menuname)
          print(dash)
    def SubMenu(array): #uses array input
            for i in range (len(array)):
                print(array[i])
            while True:
                Selection = int(input('Please select an option: ')) #takes input for level
                match Selection:
                        case Selection if Selection >= 1 and Selection <= len(array):
                            print('You have selected ' + array[Selection - 1] + '.')
                            return Selection
                        case 0:
                            print('You have chosen to exit.') #exits
                            return 0
                        case _:
                            print('Invalid selection. Please try again.') #applies to everything invalid
                            continue
    Selection = int(input('Please select an option from the menu:'))
    match Selection:
          case 1:
                CoreTraining = ['Core-001','Core-002','Core-003'] #Array containing the core training modules
                SubMenuPrint('Core Training')
                SubMenu(CoreTraining)
                break
          case 2: #The spinal cord, containing test labsVertebrae
                Vertebrae = ['Vertebra-001','Vertebra-002','Vertebra-003'] #Array containing the vertebrae (labs) for investigation)
                SubMenuPrint('The SOC Investigation')
                SubMenu(Vertebrae)
                break #Calls the SubMenu function with the Vertebrae array as input
          case 3: #Progress Report(s)
                UserProfile = ['','',''] #Array containing the user profile information
                SubMenuPrint('Progress Report(s)')
                SubMenu(UserProfile)
                break #Calls the SubMenu function with the UserProfile array as input
          case 4: #Exit
                print('You have chosen to exit.')
                break
          case _:
                print('Invalid selection. Please try again.') #applies to everything invalid