from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class WeightLossApp(App):
    def build(self):
        self.weight = 0
        self.calories = 0

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        header_image = Image(source='cals.jpg', size_hint_y=None, height=100)
        
        weight_label = Label(text='Enter Weight (kg):', font_size='20sp')
        self.weight_input = TextInput(multiline=False, font_size='20sp', size_hint_y=None, height=40)
        calories_label = Label(text='Enter Calories (kcal):', font_size='20sp')
        self.calories_input = TextInput(multiline=False, font_size='20sp', size_hint_y=None, height=40)

        submit_button = Button(text='Submit', on_press=self.submit_data, font_size='20sp', size_hint_y=None, height=50)
        result_label = Label(text='', font_size='20sp', halign='center')

        layout.add_widget(header_image)
        layout.add_widget(weight_label)
        layout.add_widget(self.weight_input)
        layout.add_widget(calories_label)
        layout.add_widget(self.calories_input)
        layout.add_widget(submit_button)
        layout.add_widget(result_label)

        return layout

    def submit_data(self, instance):
        try:
            weight = float(self.weight_input.text)
            calories = float(self.calories_input.text)
            self.weight += weight
            self.calories += calories

            result = f'Total Weight: {self.weight} kg\nTotal Calories: {self.calories} kcal'
            self.root.children[-1].text = result
        except ValueError:
            self.root.children[-1].text = 'Invalid input. Please enter numbers.'

if __name__ == '__main__':
    WeightLossApp().run()
