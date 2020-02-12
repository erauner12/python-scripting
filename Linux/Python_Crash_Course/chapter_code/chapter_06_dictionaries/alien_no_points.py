

alien_0 = {
    'color':'green',
    'speed':'slow',
    #'points':5
}
#if you uncomment the points above, point_value will return the key. default no point value instead

# Set a default value with get() method

point_value = alien_0.get('points', 'No Point value assigned.')

print(point_value)