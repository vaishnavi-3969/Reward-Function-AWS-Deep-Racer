def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    # marker_1 = 0.1 * track_width
    # marker_2 = 0.25 * track_width
    # marker_3 = 0.5 * track_width
    # marker_4 = 0.75 * track_width 
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width
    marker_5 = 0.5 * track_width
    marker_6 = 0.6 * track_width
    marker_7 = 0.7 * track_width
    marker_8 = 0.8 * track_width
    marker_9 = 0.9 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.4
    elif distance_from_center <= marker_4:
        reward = 0.3
    elif distance_from_center <= marker_5:
        reward = 0.2
    elif distance_from_center <= marker_6:
        reward = 0.1
    elif distance_from_center <= marker_7:
        reward = 0.01
    elif distance_from_center <= marker_8:
        reward = 0.001
    elif distance_from_center <= marker_9:
        reward = 0.0001
    else:
        reward = -1 # likely crashed/ close to off track

    return float(reward)
