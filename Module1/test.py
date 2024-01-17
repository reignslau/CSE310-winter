from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class WeightLossApp(App):
    def build(self):
        self.weight = 0
        self.calories = 0

        layout = GridLayout(cols=2, spacing=10, padding=10)

        weight_label = Label(text='Weight:')
        self.weight_input = TextInput(multiline=False)
        calories_label = Label(text='Calories:')
        self.calories_input = TextInput(multiline=False)

        submit_button = Button(text='Submit', on_press=self.submit_data)
        result_label = Label(text='')

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

            result = f'Weight: {self.weight} kg\nCalories: {self.calories} kcal'
            self.root.children[-1].text = result
        except ValueError:
            self.root.children[-1].text = 'Invalid input. Please enter numbers.'

if __name__ == '__main__':
    WeightLossApp().run()
