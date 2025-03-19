import flet as ft
import controller as c

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = c.SpellChecker(self)
        # UI elements
        self._title = None
        self._theme_switch = None
        self._language_selector = None
        self._select_modality = None
        self._txtIn = None
        self._btnExecute = None
        # define the UI elements and populate the page



    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row1=ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        self._language_selector = ft.Dropdown(label="Select language", options=[ft.dropdown.Option("Italiano"), ft.dropdown.Option("Inglese")])
        self._select_modality = ft.Dropdown(label="Select modality", options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic")] )
        self._txtIn = ft.TextField(label="Add your sentence here")

        self.__btnExecute = ft.ElevatedButton(text="Spell Check", on_click=self.__controller.handleSpellChecker)

        self._txtOut = ft.ListView(expand=True)

        row3=ft.Row(spacing=30, controls=[self._select_modality, self._txtIn, self.__btnExecute])

        self.page.add(row1,self._language_selector,row3,self._txtOut)


        # Add your stuff here
        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()


