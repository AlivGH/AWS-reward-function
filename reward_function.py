import math

def reward_function(params):

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    X = params['x']
    Y = params['y']
    speed = params['speed']
    track_width = params["track_width"]
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    # Initialize the reward with a typical value
    reward = 1.0


    next_point = waypoints[closest_waypoints[1]]
    prev_point = (X, Y)


    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    
# Convert to degrees
    track_direction = math.degrees(track_direction)


    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff


    DIRECTION_THRESHOLD = 10.0
    SPEED_THRESHOLD = 1.0
    DISTANCE_PARAMETER = 1 - distance_from_center/track_width/2
    
      
    if direction_diff > DIRECTION_THRESHOLD :#or speed < SPEED_THRESHOLD:
        reward -= 0.4
    if DISTANCE_PARAMETER <=0.4:
        reward -= 0.1
    if speed < SPEED_THRESHOLD:
        reward -= 0.2
    if not all_wheels_on_track:
        reward = -3

    return float(reward)
