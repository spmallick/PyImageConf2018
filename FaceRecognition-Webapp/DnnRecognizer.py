#                          License Agreement
#                         3-clause BSD License
#
#       Copyright (C) 2018, Xperience.AI, all rights reserved.
#
# Third party copyrights are property of their respective owners.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#   * Neither the names of the copyright holders nor the names of the contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# This software is provided by the copyright holders and contributors "as is" and
# any express or implied warranties, including, but not limited to, the implied
# warranties of merchantability and fitness for a particular purpose are disclaimed.
# In no event shall copyright holders or contributors be liable for any direct,
# indirect, incidental, special, exemplary, or consequential damages
# (including, but not limited to, procurement of substitute goods or services;
# loss of use, data, or profits; or business interruption) however caused
# and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of
# the use of this software, even if advised of the possibility of such damage.

import cv2
import numpy

class DnnRecognizer():
    def __init__(self, model_path='data/openface.nn4.small2.v1.t7',
                 model_mean = [0, 0, 0], model_in_size = (96, 96), model_scale = 1.0 / 255, conf_threshold = 0.6):
        self.known_faces = dict()
        self.model = cv2.dnn.readNetFromTorch(model_path)
        self.mean = model_mean
        self.scale = model_scale
        self.in_size = model_in_size
        self.confidence = conf_threshold

    def enroll(self, imageBuffer, name):
        vec = self._face2vec(imageBuffer)
        self.known_faces[name] = vec

    def recognize(self, imageBuffer):
        vec = self._face2vec(imageBuffer)
        best_match_name = 'unknown'
        best_match_score = self.confidence
        # NOTE: Replace iteritems() method to items() if you use Python3
        for name, descriptor in self.known_faces.items():
            score = vec.dot(descriptor.T)
            if (score > best_match_score):
                best_match_score = score
                best_match_name = name
        return best_match_name

    def _face2vec(self, imageBuffer):
        dataFromBuffer = numpy.frombuffer(imageBuffer, dtype=numpy.uint8)
        image = cv2.imdecode(dataFromBuffer, cv2.IMREAD_COLOR)
        blob = cv2.dnn.blobFromImage(image, self.scale, self.in_size, self.mean, False, False)
        self.model.setInput(blob)
        vec = self.model.forward()
        return vec
