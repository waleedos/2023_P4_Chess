"""class Homepage controller"""


from src.views.homepage import HomepageView


class HomepageController:
    def __init__(self, view=HomepageView()):
        self.view = view

    def run(self):
        """homepage menu"""

        return self.view.menu()
