from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


class Calculator(MDApp):

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.eq = None

    def build(self):
        Window.size = (320, 505)
        main_kv = Builder.load_file('calc.kv')
        return main_kv

    def button(self, button):
        if self.eq:
            self.eq = False
            self.root.ids.input_box.text = ''
        if button == 'x':
            button = '*'
        prior = self.root.ids.input_box.text
        if prior == '0' and button not in ('.', '+', '*', '/', '-'):
            prior = ''
        if prior == '':
            if button == '00' or button == '0':
                self.root.ids.input_box.text = '0'
                return
            if button in ('+', '/', '*', '%'):
                return
            self.root.ids.input_box.text = f'{button}'

        else:
            if prior == 'Cannot be divided by 0':
                prior = ''

            if button in ('+', '/', '*', '%', '-'):

                if self.root.ids.input_box.text[0] == '-':
                    return
                if self.root.ids.input_box.text[-1] in ('+', '/', '*', '%', '-'):
                    self.root.ids.input_box.text = f'{prior[:-1]}{button}'
                    return
            self.root.ids.input_box.text = ''
            self.root.ids.input_box.text = f'{prior}{button}'

    def clear_entry(self):
        i = -1
        l = len(self.root.ids.input_box.text)
        if l != 0 and self.root.ids.input_box.text[0] == '-':
            self.root.ids.input_box.text = ''
            return
        while i >= -l:
            if self.root.ids.input_box.text[i] in ('+', '-', 'x', '/', '%'):
                i += l
                self.root.ids.input_box.text = self.root.ids.input_box.text[:i + 1]
                return
            i -= 1

        self.root.ids.input_box.text = ''

    def clear(self):
        self.root.ids.input_box.text = ''

    def result(self):
        try:
            self.root.ids.input_box.text = str(eval(self.root.ids.input_box.text))
            self.eq = True
        except ZeroDivisionError:
            self.root.ids.input_box.text = 'Cannot be divided by 0'
        except Exception:
            pass


if __name__ == '__main__':
    Calculator().run()
