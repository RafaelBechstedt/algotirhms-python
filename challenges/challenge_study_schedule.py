def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if target_time in range(start, end + 1):
            # Range funciona como start <= target_time < end. Por isso o +1
            count += 1
    return count
