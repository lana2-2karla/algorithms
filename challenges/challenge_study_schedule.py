def study_schedule(permanence_period, target_time):
    qty_students = 0
    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                qty_students += 1
        except TypeError:
            return None

    return qty_students