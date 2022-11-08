from keras.models import model_from_json
import numpy as np


class FaceKeypointsCaptureModel(object):

    COLUMNS = ['left_eye_center_x', 'left_eye_center_y',
               'right_eye_center_x', 'right_eye_center_y',
               'left_eye_inner_corner_x', 'left_eye_inner_corner_y', 
               'left_eye_outer_corner_x', 'left_eye_outer_corner_y',
               'right_eye_inner_corner_x', 'right_eye_inner_corner_y', 
               'right_eye_outer_corner_x', 'right_eye_outer_corner_y',
               'left_eyebrow_inner_end_x', 'left_eyebrow_inner_end_y',
               'left_eyebrow_outer_end_x', 'left_eyebrow_outer_end_y',
               'right_eyebrow_inner_end_x', 'right_eyebrow_inner_end_y',
               'right_eyebrow_outer_end_x', 'right_eyebrow_outer_end_y',
               'nose_tip_x', 'nose_tip_y',
               'mouth_left_corner_x', 'mouth_left_corner_y',
               'mouth_right_corner_x', 'mouth_right_corner_y',
               'mouth_center_top_lip_x', 'mouth_center_top_lip_y',
               'mouth_center_bottom_lip_x', 'mouth_center_bottom_lip_y']

    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)
        #print("Model loaded from disk")
        self.loaded_model.summary()

    def predict_points(self, img):
        self.preds = self.loaded_model.predict(img) % 96

        self.pred_dict = dict([(point, val) for point, val in zip(FaceKeypointsCaptureModel.COLUMNS, self.preds[0])])

        return self.preds, self.pred_dict

    def scale_prediction(self, out_range_x=(-1, 1), out_range_y=(-1, 1)):
        range_ = [0, 96]
        self.preds = ((self.preds - range_[0]) / (range_[1] - range_[0]))
        self.preds[:, range(0, 30, 2)] = ((self.preds[:, range(0, 30, 2)] *
                                         (out_range_x[1] - out_range_x[0])) + out_range_x[0])
        self.preds[:, range(1, 30, 2)] = ((self.preds[:, range(1, 30, 2)] *
                                         (out_range_y[1] - out_range_y[0])) + out_range_y[0])

        self.pred_dict = dict([(point, val) for point, val in zip(FaceKeypointsCaptureModel.COLUMNS, self.preds[0])])
        return self.preds, self.pred_dict


if __name__ == '__main__':
    model = FaceKeypointsCaptureModel("face_model.json", "face_model.h5")
    
   