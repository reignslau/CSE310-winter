from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image

class MealCalorieCalculatorApp(App):
    def build(self):
        self.meal_totals = {'breakfast': 0, 'lunch': 0, 'dinner': 0, 'snack': 0}
        self.selected_meal = 'breakfast'
        self.exercise_total = 0

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        header_image = Image(source='cals.jpg', size_hint_y=None, height=100)

        title_label = Label(text='Meal & Exercise Calorie Calculator', font_size='24sp')

        food_label = Label(text='Enter Food Item:')
        self.food_input = TextInput(multiline=False, font_size='20sp')

        calorie_label = Label(text='Enter Calories (kcal):')
        self.calorie_input = TextInput(multiline=False, font_size='20sp')

        meal_label = Label(text='Select Meal:')
        self.meal_dropdown = DropDown()

        for meal in self.meal_totals.keys():
            btn = Button(text=meal.capitalize(), size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.meal_dropdown.select(btn.text))
            self.meal_dropdown.add_widget(btn)

        meal_button = Button(text='Select Meal', on_release=self.meal_dropdown.open, font_size='20sp')
        self.meal_dropdown.bind(on_select=lambda instance, x: setattr(meal_button, 'text', x))

        submit_button = Button(text='Add Food', on_press=self.add_food, font_size='20sp')
        delete_button = Button(text='Delete Food', on_press=self.delete_food, font_size='20sp')

        exercise_label = Label(text='Enter Exercise (kcal):')
        self.exercise_input = TextInput(multiline=False, font_size='20sp')

        exercise_button = Button(text='Add Exercise', on_press=self.add_exercise, font_size='20sp')

        self.breakfast_label = Label(text='Breakfast Total: 0 kcal', font_size='18sp')
        self.lunch_label = Label(text='Lunch Total: 0 kcal', font_size='18sp')
        self.dinner_label = Label(text='Dinner Total: 0 kcal', font_size='18sp')
        self.snack_label = Label(text='Snack Total: 0 kcal', font_size='18sp')

        total_label = Label(text='Total Calories:', font_size='24sp')
        self.total_display = Label(text=str(self.calculate_total()), font_size='24sp')

        layout.add_widget(header_image)
        layout.add_widget(title_label)
        layout.add_widget(food_label)
        layout.add_widget(self.food_input)
        layout.add_widget(calorie_label)
        layout.add_widget(self.calorie_input)
        layout.add_widget(meal_label)
        layout.add_widget(meal_button)
        layout.add_widget(submit_button)
        layout.add_widget(delete_button)
        layout.add_widget(exercise_label)
        layout.add_widget(self.exercise_input)
        layout.add_widget(exercise_button)
        layout.add_widget(self.breakfast_label)
        layout.add_widget(self.lunch_label)
        layout.add_widget(self.dinner_label)
        layout.add_widget(self.snack_label)
        layout.add_widget(total_label)
        layout.add_widget(self.total_display)

        return layout

    def add_food(self, instance):
        try:
            calories = float(self.calorie_input.text)
            selected_meal = self.meal_dropdown.children[0]

            self.meal_totals[selected_meal] += calories

            self.update_meal_labels()
            self.update_total_display()
            self.clear_input_fields()
        except ValueError:
            self.total_display.text = 'Invalid input. Please enter numbers.'

    def delete_food(self, instance):
        try:
            if hasattr(self, 'selected_meal') and self.selected_meal in self.meal_totals:

                if self.meal_totals[self.selected_meal] > 0:
                    self.meal_totals[self.selected_meal] -= 1
                    self.update_meal_labels()
                    self.update_total_display()
        except ValueError:
            self.total_display.text = 'Error deleting food.'

    def add_exercise(self, instance):
        try:
            exercise_calories = float(self.exercise_input.text)

            self.exercise_total += exercise_calories

            self.update_total_display()
            self.clear_input_fields()
        except ValueError:
            self.total_display.text = 'Invalid input. Please enter numbers.'

    def calculate_total(self):
        return sum(self.meal_totals.values()) - self.exercise_total

    def update_meal_labels(self):
        self.breakfast_label.text = f'Breakfast Total: {self.meal_totals["breakfast"]} kcal'
        self.lunch_label.text = f'Lunch Total: {self.meal_totals["lunch"]} kcal'
        self.dinner_label.text = f'Dinner Total: {self.meal_totals["dinner"]} kcal'
        self.snack_label.text = f'Snack Total: {self.meal_totals["snack"]} kcal'

    def update_total_display(self):
        self.total_display.text = str(self.calculate_total())

    def clear_input_fields(self):
        self.food_input.text = ''
        self.calorie_input.text = ''
        self.exercise_input.text = ''

if __name__ == '__main__':
    MealCalorieCalculatorApp().run()
