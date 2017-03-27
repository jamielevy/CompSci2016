from tkinter import *

WelcomeScreen = Tk()    #This defines the starting root window for the GUI
WelcomeScreen.configure(bg="black")

def PupilInterface():
    WelcomeScreen.destroy()     #The '.destroy()' method closes the last window so that only one window is open at one time, making things less confusting
    global PupilInterfaceWindow     #Variable is set to global so that it can be accessed from outside of this subroutine
    PupilInterfaceWindow = Tk()     #This defines the pupil interface root for the GUI

    SelectClassTest = Label(PupilInterfaceWindow, text = "Select your class")   #The 'label' attribute allows text to be displayed
    SelectClassTest.grid(columnspan=10)

    ClassPlaceholder = Button(PupilInterfaceWindow, text = "ClassPlaceholder", command = SelectPupil, height = 5, width = 15)
    #The 'button' attribute allows a button to be created
    ClassPlaceholder.grid(column=1,row=1) #the'.grid' method allows the button/label to be aligned to the grid to make things look neater


    
def TeacherInterface():
    WelcomeScreen.destroy()
    global TeacherInterfaceWindow
    TeacherInterfaceWindow = Tk()

    ViewOverallStatsButton = Button(TeacherInterfaceWindow, text = "View overall statistics", command = ViewOverallStats, height = 5, width = 45,
                                    font=("Comic Sans MS", 25), fg = "orange", bg = "black")
    ViewOverallStatsButton.grid(column=1,row=1)

    
    SelectTheClassYouTeachButton = Button(TeacherInterfaceWindow, text = "Select the class you teach", command = SelectYourClass,
                                          height = 5, width = 45, font=("Comic Sans MS", 25), fg = "orange", bg = "black")
    # The command method links a button press to the specified subroutine, in this case it's the 'SelectYourClass' subroutine. Therefore when a button is
    # pressed, the program will branch to this subroutine.
    SelectTheClassYouTeachButton.grid(column=1, row=2)

    ViewReportButton = Button(TeacherInterfaceWindow, text = "View a report from a specified period", command = ViewReport, height = 5, width = 45,
                              font=("Comic Sans MS", 25), fg = "orange", bg = "black")
    ViewReportButton.grid(column=1, row=3)
    
def ViewOverallStats():
    TeacherInterfaceWindow.destroy()
    global ViewOverallStatsWindow
    ViewOverallStatsWindow = Tk()

    ViewOverallStatsPlaceholder = Label(ViewOverallStatsWindow, text = "access to the database will be added in the second iteration")
    ViewOverallStatsPlaceholder.grid(columnspan=10)

def ViewReport():
    TeacherInterfaceWindow.destroy()
    global ViewReportWindow
    ViewReportWindow = Tk()

    ViewReportPlaceholder = Label(ViewReportWindow, text = "access to the database will be added in the second iteration")
    ViewReportPlaceholder.grid(columnspan=10)

def SelectYourClass():
    TeacherInterfaceWindow.destroy()
    global SelectYourClassWindow
    SelectYourClassWindow = Tk()

    ViewPupilStats = Button(SelectYourClassWindow, text = "View statistics about a certain pupil", command = ViewPupilStatistics, height = 5, width = 45
                            ,font=("Comic Sans MS", 25), fg = "orange", bg = "black")
    ViewPupilStats.grid(column=1, row=1)

    ViewClassStats = Button(SelectYourClassWindow, text = "View statistics about a certain class", command = ViewClassStatistics, height = 5, width = 45
                            ,font=("Comic Sans MS", 25), fg = "orange", bg = "black")
    ViewClassStats.grid(column=1, row=2)

    AddEditMember = Button(SelectYourClassWindow, text = "Add or edit an existing member", command = AddEditClassMember, height = 5, width = 45
                           , font=("Comic Sans MS", 25), fg = "orange", bg = "black")
    AddEditMember.grid(column=1, row=3)

def ViewPupilStatistics():
    ViewPupilStatsWindow = Tk()

    PupilStatsPlaceholder = Label(ViewPupilStatsWindow, text="access to the database will be added in the second iteration")
    PupilStatsPlaceholder.grid(columnspan=10)

def ViewClassStatistics():
    ViewClassStatsWindow = Tk()

    ClassStatsPlaceholder = Label(ViewClassStatsWindow, text="access to the database will be added in the second iteration")
    ClassStatsPlaceholder.grid(columnspan=10)

def AddEditClassMember():
    AddEditClassMemberWindow = Tk()

    AddEditClassMemberPlaceholder = Label(AddEditClassMemberWindow, text="access to the database will be added in the second iteration")
    AddEditClassMemberPlaceholder.grid(columnspan=10)

 
##########################################################################################################################################################
############################################ pupil section ###############################################################################################

def SelectPupil():
    PupilInterfaceWindow.destroy()
    global SelectPupilWindow
    SelectPupilWindow = Tk()

    SelectYourName = Label(SelectPupilWindow, text = "Select your name", font=("Comic Sans MS", 50), fg = "light blue", bg = "black")
    SelectYourName.grid(columnspan = 10)
    
    PupilPlaceHolder = Button(SelectPupilWindow, text = "Pupil Placeholder", command = FoodSelection, height = 5, width = 15)
    PupilPlaceHolder.grid(row=1, column=1)

def FoodSelection():
    SelectPupilWindow.destroy()
    global FoodSelectionWindow
    FoodSelectionWindow = Tk()

    FoodSelectionPlaceHolder = Label(FoodSelectionWindow, text = "Food selection will be added in the third iteration")
    FoodSelectionPlaceHolder.grid(columnspan=10)
    
##########################################################################################################################################################
############################################ end of pupil section ########################################################################################

GoodMorningText = Label(WelcomeScreen, text = "Good morning!", font=("Comic Sans MS", 50), fg="light blue", bg="black" )
GoodMorningText.grid(columnspan=10)

PupilPhoto = PhotoImage(file="pupil.gif")
PupilInterfaceButton = Button(WelcomeScreen, text = "I am a pupil", command = PupilInterface , font=("Comic Sans MS", 25), fg = "light green", bg = "black",
                              height = 150, width = 200, image = PupilPhoto, compound = BOTTOM)
PupilInterfaceButton.grid(column=1,row=1)
#The 'compound' element tells the program where to place the image
#When a user clicks the PupilInterface Button, they will be taken to the pupil-faciing interface (i.e. the program branches to the PupilInterface function)

TeacherPhoto = PhotoImage(file="teacher.gif")
TeacherInterfaceButton = Button(WelcomeScreen, text = "I am a teacher", command = TeacherInterface, font=("Comic Sans MS", 25), fg = "red",
                                bg = "black", height = 150, width = 220, image = TeacherPhoto, compound = BOTTOM)
TeacherInterfaceButton.grid(column=2, row=1)
#The same is true for the TeacherInterface button

