from typing import List

import imgui
import numpy as np

from window import Window
from data_matrix_window import DataMatrixWindow


class HMatrixSettingsWindow(Window):
    def __init__(self, dmw: DataMatrixWindow):
        super().__init__(300,300)
        self._id = "Homography Matrix"
        self._N = 1
        self._matrix = np.zeros((3,3))
        self._temp_matrix = np.zeros((3,3))
        self._shifts = np.zeros((3,3))
        self._dmw = dmw

    def _draw_content(self):
        imgui.text("Homography Matrix")
        _,self._temp_matrix[0] = imgui.input_float3("i1", *self._temp_matrix[0],format='%.7f', flags=2)
        _,self._temp_matrix[1] = imgui.input_float3("i2", *self._temp_matrix[1],format='%.7f')
        _,self._temp_matrix[2] = imgui.input_float3("i3", *self._temp_matrix[2],format='%.7f')

        s1, self._shifts[0] = imgui.slider_float3(
            "s1", *self._shifts[0],
            min_value=-self._N, max_value=self._N,
            format="%.2f")

        s2, self._shifts[1] = imgui.slider_float3(
            "s2", *self._shifts[1],
            min_value=-self._N, max_value=self._N,
            format="%.2f")

        s3, self._shifts[2] = imgui.slider_float3(
            "s3", *self._shifts[2],
            min_value=-self._N, max_value=self._N,
            format="%.2f")

        imgui.begin_group()
        if imgui.button("Применить"):
            self._matrix = self._temp_matrix
            self._shifts = np.zeros((3,3))
        imgui.end_group()

        imgui.same_line(spacing=5)

        imgui.begin_group()
        if imgui.button("Сбросить"):
            self._temp_matrix = self._matrix
            self._shifts = np.zeros((3,3))
        imgui.end_group()

        self._dmw.set_homography_matrix(self._temp_matrix)
        self._dmw.set_homo_changes(s1 or s2 or s3)

        if s1 or s2 or s3:
            self._temp_matrix = self._matrix + self._shifts
            s1 = s2 = s3 = False

        imgui.text('You wrote: %' + str(list(self._matrix)))

    def get_matrix(self):
        return self._matrix

    def set_matrix(self, matrix: np.ndarray):
        self._matrix = matrix

    def set_N(self, N: float):
        self._N = N

