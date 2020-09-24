import airsim
import time
import sys
import cv2

# Create a client object to interact with OSim
c = airsim.VehicleClient()

camera_pose = airsim.Pose()

# Let's set position to (-3, 0, 0)
camera_pose.position.x_val = -3
# Move camera elsewhere just to test
c.simSetVehiclePose(camera_pose, False)
time.sleep(5.0)

# Let's create a random pose with position(1, 1, 0)
obj_pose = airsim.Pose()
obj_pose.position.x_val = 1
obj_pose.position.y_val = 1

# Create some scale for the object
scale = airsim.Vector3r(10, 10, 10)

# Name of actual mesh/asset
test_object_name = "Cone"

# Name of object we want to call it in the world
spawned_name = "test_mouse"

# Spawn the object with pre-specified pose and scale!
spawned_name = c.simSpawnObject(
    spawned_name, test_object_name, obj_pose, scale)
time.sleep(5.0)
print("Spawned")

# Set all objects to a particular segmentation ID through regex
c.simSetSegmentationObjectID('[\w]*', -1, True)

# OPtion 2 - Loop over all objects manually

obj_list = c.simListSceneObjects()

for obj in obj_list:
    c.simSetSegmentationObjectID(obj, -1, True)

# Set newly spawned object to a new ID
c.simSetSegmentationObjectID(spawned_name + '[\w]*', 240, True)

time.sleep(2.0)
# Let's decrease the size of the object by setting a new scale
new_scale = airsim.Vector3r(0.4, 0.4, 0.4)

# Set the new scale
c.simSetObjectScale(spawned_name, new_scale)
time.sleep(5.0)

# Change the position of the object to (2, 1, 0)
obj_pose.position.x_val = 2
c.simSetObjectPose(spawned_name, obj_pose, False)
time.sleep(5.0)


# Get the most updated pose of the object
obj_pose = c.simGetObjectPose(spawned_name)


# Check for all spawned objects with given name in a regex styled query
obj_list = c.simListSceneObjects(spawned_name + ".*")

# Destroy all those objects
for obj in obj_list:
    c.simDestroyObject(obj)
time.sleep(2.0)
