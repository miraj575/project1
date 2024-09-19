from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.image import MDImage
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from PIL import Image as PILImage
import io

# Helper function to convert an image file to a Kivy Texture
def load_image(image_path, size):
    pil_image = PILImage.open(image_path)
    pil_image = pil_image.resize(size, PILImage.Resampling.LANCZOS)
    byte_data = io.BytesIO()
    pil_image.save(byte_data, format='png')
    byte_data.seek(0)
    texture = Texture.create(size=(pil_image.width, pil_image.height), colorfmt='rgba')
    texture.blit_buffer(byte_data.read(), bufferfmt='ubyte', colorfmt='rgba')
    return texture

class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        Window.clearcolor = (1, 0.8, 0.8, 1)  # Light pink background

        # Title Label
        title = MDLabel(text="Heyy fairy, Heyy Rose [Fairuz], Welcome to magical fairy_rose_code.py 🌹",
                        font_style='H6', halign='center', size_hint_y=None, height=50)
        layout.add_widget(title)

        # Welcome Label
        welcome_label = MDLabel(text="Will you take the rose?", font_style='H6',
                                halign='center', size_hint_y=None, height=50)
        layout.add_widget(welcome_label)

        # Teddy Bear Image
        teddy_bear = MDImage(size_hint=(1, 0.6), allow_stretch=True, texture=couple_photo)
        layout.add_widget(teddy_bear)

        # Buttons
        button_layout = MDBoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        okay_button = MDRaisedButton(text="Okay", on_press=self.start_quiz, md_bg_color=(1, 0.4, 0.6, 1))
        no_button = MDRaisedButton(text="No", on_press=self.close_app, md_bg_color=(1, 0.4, 0.6, 1))
        button_layout.add_widget(okay_button)
        button_layout.add_widget(no_button)

        layout.add_widget(button_layout)
        self.add_widget(layout)

    def start_quiz(self, instance):
        self.manager.current = 'question'

    def close_app(self, instance):
        MDApp.get_running_app().stop()

class QuestionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.question = None
        self.correct_answer = None
        self.next_screen = None

    def setup(self, question, correct_answer, next_screen, bg_color, fg_color):
        self.question = question
        self.correct_answer = correct_answer
        self.next_screen = next_screen

        self.clear_widgets()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        Window.clearcolor = bg_color

        question_label = MDLabel(text=question, font_style='H6', halign='center', size_hint_y=None, height=50, theme_text_color="Custom", text_color=fg_color)
        layout.add_widget(question_label)

        self.answer_input = MDTextField(size_hint=(1, 0.2), multiline=False)
        layout.add_widget(self.answer_input)

        submit_button = MDRaisedButton(text="Submit", on_press=self.submit_answer, md_bg_color=fg_color)
        layout.add_widget(submit_button)

        # Teddy Bear Image
        teddy_bear = MDImage(size_hint=(1, 0.6), allow_stretch=True, texture=couple_photo)
        layout.add_widget(teddy_bear)

        self.add_widget(layout)

    def submit_answer(self, instance):
        answer = self.answer_input.text.strip().lower()
        if answer == self.correct_answer.lower():
            self.manager.current = self.next_screen
        else:
            self.show_feedback(False)

    def show_feedback(self, is_correct):
        self.clear_widgets()
        feedback_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        feedback_message = "Tumi na bolla math paro na!" if is_correct else "Ahare arekta try dao , please!"
        feedback_label = MDLabel(text=feedback_message, font_style='H6', halign='center', size_hint_y=None, height=50, theme_text_color="Custom", text_color=(1, 0.4, 0.6, 1))
        feedback_layout.add_widget(feedback_label)
        next_button = MDRaisedButton(text="Next" if is_correct else "Retry", on_press=self.go_to_next_screen, md_bg_color=(1, 0.4, 0.6, 1))
        feedback_layout.add_widget(next_button)
        self.add_widget(feedback_layout)

    def go_to_next_screen(self, instance):
        if self.next_screen:
            self.manager.current = self.next_screen

class PersonalQuestionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self, question, next_screen):
        self.question = question
        self.next_screen = next_screen

        self.clear_widgets()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        Window.clearcolor = (0.94, 1, 0.94, 1)  # Light green background

        question_label = MDLabel(text=question, font_style='H6', halign='center', size_hint_y=None, height=50, theme_text_color="Custom", text_color=(0, 0.8, 0, 1))
        layout.add_widget(question_label)

        self.answer_input = MDTextField(size_hint=(1, 0.4), multiline=True)
        layout.add_widget(self.answer_input)

        submit_button = MDRaisedButton(text="Submit", on_press=self.submit_answer, md_bg_color=(0, 0.8, 0, 1))
        layout.add_widget(submit_button)

        # Teddy Bear Image
        teddy_bear = MDImage(size_hint=(1, 0.5), allow_stretch=True, texture=couple_photo)
        layout.add_widget(teddy_bear)

        self.add_widget(layout)

    def submit_answer(self, instance):
        if self.next_screen:
            self.manager.current = self.next_screen

class SmilingQuestionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self):
        self.clear_widgets()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        Window.clearcolor = (1, 0.8, 0.8, 1)  # Light pink background

        question_label = MDLabel(text="You are smiling, right?", font_style='H6', halign='center', size_hint_y=None, height=50, theme_text_color="Custom", text_color=(1, 0.4, 0.6, 1))
        layout.add_widget(question_label)

        def handle_yes(instance):
            self.show_message()

        def handle_no(instance):
            self.show_message()

        def show_message():
            self.dialog = MDDialog(title='Message',
                                   text="Tumar cheharar expression miss korlam",
                                   size_hint=(0.7, 0.3))
            self.dialog.open()
            self.manager.current = 'romantic_message'

        yes_button = MDRaisedButton(text="Yes", on_press=handle_yes, md_bg_color=(1, 0.4, 0.6, 1))
        no_button = MDRaisedButton(text="No", on_press=handle_no, md_bg_color=(1, 0.4, 0.6, 1))
        button_layout = MDBoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        layout.add_widget(button_layout)

        # Teddy Bear Image
        teddy_bear = MDImage(size_hint=(1, 0.6), allow_stretch=True, texture=couple_photo)
        layout.add_widget(teddy_bear)

        self.add_widget(layout)

class RomanticMessageScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self):
        self.clear_widgets()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        Window.clearcolor = (1, 0.8, 0.8, 1)  # Light pink background

        romantic_message = ("আমার ইংরেজি থেকে বাংলা ভালো লাগে।সুন্দর ভাষা । আমি মিরাজ , আমি হিমু নই, আমার "
                            "মধ্যে হিমু ইফেক্ট নেই, হয়ত তুমি কিছুটা পাইসো। হিমুরা হলুদ , নিল পছন্দ করে কিন্তু আমি "
                            "সবুজ , নিল, বেগুনি পছন্দ করি। নিল বেশিরভাগ মানুষেরই পছন্দ ,হিমুর পছন্দের কারণ সব "
                            "মেয়েদের নিল শাড়িতে রুপবতী লাগে। আমার সবুজ পছন্দের একটা কারণ শুধুমাত্র অসম্ভব রুপবতী "
                            "মেয়েদেরকেই এই প্রকৃতির রঙে মানায়। তুমি আমার কাছে শুনতে চাও তুমি কেমন মেয়ে , তুমি ভীতু, "
                            "মিশুক ও রাগি প্রকৃতির। তুমি বলসিলা তোমার অহংকার আছে কিন্তু আমি তা দেখি নাই হয়তো। তুমি "
                            "মানুষের সাথে অনেক সহজেই শখা গড়তে পারো। এইসব লেখা পড়ে আমাকে অনেক লেইম মনে হইতে পারে।যেটা "
                            "আমার নিজেরই মনে হইতেসে। আমার মস্তিষ্কে আর কিছুই আসতেসে না, কি করব বলো। এই সিস্টেম "
                            "টা তোমার ভালো লাগসে কি না জানি না। আমার উপর থেকে বিরক্ত ভাব টা সরায় ফেলার জন্য এই প্রোগ্রাম। "
                            "ভালই কষ্ট হইসে, কিন্তু প্যাসানেট মনে হইসে। ধন্যবাদ নাফিসা। ইমুজি ব্যবহার করতে পারতেসি না "
                            "এইখানে।")

        romantic_label = MDLabel(text=romantic_message, font_style='H6', halign='center', valign='middle', size_hint_y=None, theme_text_color="Custom", text_color=(1, 0.4, 0.6, 1))
        layout.add_widget(romantic_label)

        finish_button = MDRaisedButton(text="ভালো না লাগলেও বলিও", on_press=self.close_app, md_bg_color=(1, 0.4, 0.6, 1))
        layout.add_widget(finish_button)

        self.add_widget(layout)

    def close_app(self, instance):
        MDApp.get_running_app().stop()

class QuizApp(MDApp):
    def build(self):
        self.title = "Quiz Application"
        sm = MDScreenManager()

        # Load the couple image
        global couple_photo
        image_path = "Avt_Couple.jpeg"
        couple_photo = load_image(image_path, (200, 200))

        # Add screens
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(QuestionScreen(name='question'))
        sm.add_widget(PersonalQuestionScreen(name='personal_question'))
        sm.add_widget(SmilingQuestionScreen(name='smiling_question'))
        sm.add_widget(RomanticMessageScreen(name='romantic_message'))

        # Setup question screens
        sm.get_screen('question').setup("Find the slope of the line 3x - 4y = 8.", "3/4", 'question_2', (0.94, 0.97, 1, 1), (0, 0, 0.5, 1))
        sm.get_screen('personal_question').setup("ekhon ki chinta korteso ?", 'personal_question_2')
        sm.get_screen('personal_question').setup("Ami tumar kache eto annoying keno ektu bolo to, Fairuz?", 'personal_question_3')
        sm.get_screen('personal_question').setup("hashteso ?", 'physics_question_1')
        sm.get_screen('physics_question_1').setup("A projectile is launched at an angle of 30 degrees with a speed of 20 m/s. What is its maximum height? (g = 9.8 m/s²)", "5.1", 'personal_question_4', (0.9, 0.9, 1, 1), (0, 0, 1, 1))
        sm.get_screen('personal_question').setup("amar kotha ekbaro mone porse , etodin ?", 'personal_question_5')
        sm.get_screen('personal_question').setup("kemon lagtese ei program e ashar por?", 'physics_question_2')
        sm.get_screen('physics_question_2').setup("A projectile is launched with a velocity of 20 m/s at an angle of 45 degrees. What is its range? (g = 9.8 m/s²)", "40.8", 'smiling_question', (0.9, 0.9, 1, 1), (0, 0, 1, 1))

        return sm

if __name__ == '__main__':
    QuizApp().run()
