class MenuBarManager:
    def __init__(self, main_window):
        self.main_window = main_window

    def create_menubar(self):
        # Menubar
        menu_bar = self.main_window.menuBar()

        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        view_menu = menu_bar.addMenu('View')

        # File Menu Actions
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Exit")

        # Edit Menu Actions
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")

        # View Menu Actions
        view_menu.addAction("Zoom In")
        view_menu.addAction("Zoom Out")