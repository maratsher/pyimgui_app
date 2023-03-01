from typing import List

import imgui
import numpy as np

from window import Window


class DataMatrixWindow(Window):
    def __init__(self):
        super().__init__(300,300)
        self._id = "Data Matrix Window"
        self._shape = (5,3)
        self._original_coord_matrix = np.zeros(self._shape)
        self._real_coord_matrix = np.zeros(self._shape)
        self._result_matrix = np.zeros(self._shape)
        self._homography_matrix = np.zeros(self._shape)
        self._homo_changes = False


    def _draw_content(self):
        imgui.text("Original Coordinates")
        l1,self._original_coord_matrix[0] = imgui.input_float3("l1", *self._original_coord_matrix[0])
        l2,self._original_coord_matrix[1] = imgui.input_float3("l2", *self._original_coord_matrix[1])
        l3,self._original_coord_matrix[2] = imgui.input_float3("l3", *self._original_coord_matrix[2])
        l4,self._original_coord_matrix[3] = imgui.input_float3("l4", *self._original_coord_matrix[3])
        l5,self._original_coord_matrix[4] = imgui.input_float3("l5", *self._original_coord_matrix[4])
        imgui.text("")

        imgui.text("Real Coordinates")
        l6,self._real_coord_matrix[0] = imgui.input_float3("l6", *self._real_coord_matrix[0])
        l7,self._real_coord_matrix[1] = imgui.input_float3("l7", *self._real_coord_matrix[1])
        l8,self._real_coord_matrix[2] = imgui.input_float3("l8", *self._real_coord_matrix[2])
        l9,self._real_coord_matrix[3] = imgui.input_float3("l9", *self._real_coord_matrix[3])
        l10,self._real_coord_matrix[4] = imgui.input_float3("l10", *self._real_coord_matrix[4])


        imgui.text("")

        imgui.text("Result")
        imgui.input_float3("l11", *self._result_matrix[0])
        imgui.input_float3("l12", *self._result_matrix[1])
        imgui.input_float3("l13", *self._result_matrix[2])
        imgui.input_float3("l14", *self._result_matrix[3])
        imgui.input_float3("l15", *self._result_matrix[4])

        if l1 or l2 or l3 or l4 or l5 or self._homo_changes:
            kx = np.dot(self._original_coord_matrix, self._homography_matrix[0])
            ky = np.dot(self._original_coord_matrix, self._homography_matrix[1])
            K = np.dot(self._original_coord_matrix, self._homography_matrix[2])
            x = np.round(kx / K, 5)
            y = np.round(ky / K, 5)
            l=0
            for i, j in zip(x, y):
                self._result_matrix[l] = i,j,1
                l+=1

        imgui.text('You wrote: %' + str(list(self._homography_matrix)))

    def set_homography_matrix(self, matrix: np.ndarray):
        self._homography_matrix = matrix

    def set_homo_changes(self, status: bool):
        self._homo_changes = status
