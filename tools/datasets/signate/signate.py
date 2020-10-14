from datasets.BaseDataset import BaseDataset


class Signate(BaseDataset):
    @classmethod
    def get_class_colors(*args):
        return [[69, 47, 142], [0, 255, 255], [0, 203, 151], [92, 136, 125],
                [255, 121, 166], [180, 131, 135], [255, 255, 0], [255, 134, 0], 
                [85, 255, 50], [136, 45, 66], [0, 152, 225], [255, 0, 0], 
                [65, 166, 1], [0, 0, 255], [180, 0, 129], [193, 214, 0], 
                [81, 99, 0], [215, 0, 255], [208, 149, 1]]

    @classmethod
    def get_class_names(*args):
        return ['Lane', 'Sidewalk', 'Building', 'Wall', 'SVehicle', 'Obstacle',
                'Signal', 'Signs',
                'Natural', 'Ground', 'Sky', 'Pedestrian', 'Motorbike', 'Car',
                'Truck', 'Bus', 'others', 'RoadShoulder', 'Bicycle']