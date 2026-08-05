def better_than_average(class_points, your_points):
    if your_points > (sum(class_points) + your_points) / (len(class_points) + 1):
        return True
    else:
        return False