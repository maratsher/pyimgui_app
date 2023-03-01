from imgui_app import ImGuiApp
from h_matrix_settings_window import HMatrixSettingsWindow
from data_matrix_window import DataMatrixWindow

class TestApp(ImGuiApp):
    def __init__(self, window_width, window_height, fullscreen):
        super().__init__(window_width, window_height, fullscreen)

        self.data_matrix_window = DataMatrixWindow()
        self.h_matrix_settings_window = HMatrixSettingsWindow(self.data_matrix_window)

    def draw_content(self):
        self.h_matrix_settings_window.draw()
        self.data_matrix_window.draw()

if __name__ == "__main__":
    app = TestApp(1280, 720, fullscreen=False)
    app.run()
