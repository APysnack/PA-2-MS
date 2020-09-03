from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, NumericProperty
import ms_functionality


# The GUI's Home screen
class HomeScreen(Screen):
    pass


# Error Screen for incorrect user input
class ErrorScreen(Screen):
    pass


# screen that outputs the sorted and unsorted arrays
class OutputScreen(Screen):

    # the list of array objects that was generated on the success screen
    a_list = ListProperty()

    # kivy function for when the user enters the output string
    def on_enter(self, *args):

        # if the users integer is not one of the available arrays, routes to error page
        if self.manager.screens[2].user_input not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.manager.current = "error_screen"
            return

        # imports the list of array objects from the success screen
        self.a_list = self.manager.screens[1].array_list

        # gets the user's input from the input screen
        # (decrements by 1 since user types 1-9 and array is indexed from 0-8)
        input_num = (self.manager.screens[2].user_input - 1)

        # gets the array object's unsorted variant at the index specified by the user
        out_list = self.a_list[input_num].id

        # the beginning of a string that will be used to output to prompt
        out_str = "Unsorted Array: \n"

        # goes through the elements in the array and adds line breaks after every 7 numbers
        # kivy needs the line breaks to process the text
        for x, num in enumerate(out_list):
            out_str += (str(num) + ' ')
            if x % 7 == 0:
                out_str += '\n'

        # sets the text to be displayed in left column as concatenated out_string with unsorted array elements
        self.display_string.text = out_str

        # this is all repetition of the previous code but using the sorted variant of the array
        out_list = self.a_list[input_num].sorted_id

        # output string that will be concatenated with the array
        out_str = "Sorted Array: \n"

        # iterates through the array and enters line breaks while concatenating one long string
        for x, num in enumerate(out_list):
            out_str += (str(num) + ' ')
            if x % 7 == 0:
                out_str += '\n'

        # sets the text to be displayed in right column as concatenated out_string with sorted array elements
        self.display_string_2.text = out_str


# screen to let the user know that the arrays/csv file have been generated
class SuccessScreen(Screen):
    # stores the array list for future accessibility
    array_list = ListProperty()

    # when the success screen begins
    def on_enter(self):
        # uses the generate_all function on ms_functionality to generate randomized arrays
        array_list = ms_functionality.generate_all()

        # sorts all of the arrays using merge sort
        ms_functionality.sort_all(array_list)

        # creates a CSV file with statistics on how long the sorts took
        ms_functionality.create_csv(array_list)

        # sets the screen's array_list to array_list for future accessibility
        self.array_list = array_list


# The screen the user sees when selecting an array
class InputScreen(Screen):
    user_input = NumericProperty()

    # sets user_input to the users inputted integer
    def set_num(self):
        if not self.manager.screens[1].array_list:
            self.manager.current = "error_screen"
            return

        try:
            self.user_input = int(self.input.text)

        # routes user to error screen if they fail to enter an integer
        except ValueError:
            self.manager.current = "error_screen"


# loads the main.kv language file into the builder
GUI = Builder.load_file("main.kv")


# main app class for the kivy GUI
class MainApp(App):

    # builds the GUI and returns to the user's screen
    def build(self):
        return GUI

    # function to handle screen transitions
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


MainApp().run()