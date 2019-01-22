from kivy.app import App
from kivy.properties import StringProperty, NumericProperty


class HelloApp(App):

    formula_text = StringProperty()
    factor1 = NumericProperty(0)
    factor2 = NumericProperty(0)

    def on_start(self):
        self._update_formula_text()

    def on_factor1(self, instance, value):
        self._update_formula_text()

    def on_factor2(self, instance, value):
        self._update_formula_text()

    def _update_formula_text(self):
        product = self.factor1 * self.factor2
        self.formula_text = "{} x {} = {}".format(self.factor1, self.factor2, product)
