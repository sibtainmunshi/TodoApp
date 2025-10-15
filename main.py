
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class TodoApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title
        title = Label(text='📝 My Todo App', font_size=24, size_hint_y=None, height=50)
        main_layout.add_widget(title)

        # Input section
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        self.task_input = TextInput(hint_text='Enter your task here...', multiline=False)
        add_button = Button(text='Add Task', size_hint_x=None, width=100)
        add_button.bind(on_press=self.add_task)

        input_layout.add_widget(self.task_input)
        input_layout.add_widget(add_button)
        main_layout.add_widget(input_layout)

        # Tasks display area
        scroll = ScrollView()
        self.tasks_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))

        scroll.add_widget(self.tasks_layout)
        main_layout.add_widget(scroll)

        # Clear all button
        clear_button = Button(text='Clear All Tasks', size_hint_y=None, height=50)
        clear_button.bind(on_press=self.clear_all_tasks)
        main_layout.add_widget(clear_button)

        return main_layout

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            # Create task layout
            task_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)

            # Task label
            task_label = Label(text=f'• {task_text}', text_size=(None, None), halign='left')

            # Delete button
            delete_button = Button(text='❌', size_hint_x=None, width=50)
            delete_button.bind(on_press=lambda x: self.remove_task(task_layout))

            task_layout.add_widget(task_label)
            task_layout.add_widget(delete_button)

            self.tasks_layout.add_widget(task_layout)
            self.task_input.text = ''  # Clear input field

    def remove_task(self, task_layout):
        self.tasks_layout.remove_widget(task_layout)

    def clear_all_tasks(self, instance):
        self.tasks_layout.clear_widgets()

# Run the app
if __name__ == '__main__':
    TodoApp().run()
