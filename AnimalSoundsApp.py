# Teste final de push
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

kivy.require('2.1.0') # Versão do Kivy que estamos usando

class AnimalButton(Button):
    def __init__(self, animal_name, **kwargs):
        super(AnimalButton, self).__init__(**kwargs)
        self.animal_name = animal_name
        self.background_normal = f'assets/images/{self.animal_name}.png'
        self.background_down = f'assets/images/{self.animal_name}.png' # Mantém a mesma imagem ao pressionar
        self.sound = SoundLoader.load(f'assets/sounds/{self.animal_name}.wav')
        self.bind(on_press=self.play_sound)

    def play_sound(self, instance):
        if self.sound:
            self.sound.play()

class AnimalSoundsApp(App):
    def build(self):
        # Layout em grade com 3 colunas
        layout = GridLayout(cols=3, spacing=10, padding=10)

        # Lista de animais (o nome do arquivo de imagem e som deve ser o mesmo)
        animais = ['cao', 'gato', 'leao', 'elefante', 'macaco', 'pato']

        for animal in animais:
            btn = AnimalButton(animal_name=animal)
            layout.add_widget(btn)

        return layout

if __name__ == '__main__':
    AnimalSoundsApp().run()



