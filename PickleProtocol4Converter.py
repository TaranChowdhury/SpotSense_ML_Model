import pickle

# Load the original pickle file with protocol 5
with open(r'C:\Users\taran\Desktop\CMPE195\TEST_ML\parking_detection\CMPE195A\Mask_RCNN\data\regions3.p', 'rb') as file:
    data = pickle.load(file)
# Save the data with a lower protocol
with open(r'C:\Users\taran\Desktop\CMPE195\TEST_ML\parking_detection\CMPE195A\Mask_RCNN\data\regions3.p', 'wb') as file:
    pickle.dump(data, file, protocol=4)
# Now you can load this file in Python 3.7.9
with open(r'C:\Users\taran\Desktop\CMPE195\TEST_ML\parking_detection\CMPE195A\Mask_RCNN\data\regions3.p', 'rb') as file:
    parked_car_boxes = pickle.load(file)
