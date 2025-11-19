def lambda_handler(event, context):
    # 1. Extract inputs
    # Use .get to safely retrieve values from the Step Function event
    # Assume the Step Function provides all necessary data here for this path
    handicap_index = event.get('handicapIndex')
    slope_rating = event.get('slopeRating')
    course_rating = event.get('courseRating')

    # Simple validation (for production, this would be more robust)
    if not all([handicap_index, slope_rating, course_rating]):
        # If data is missing, the preceding Choice state should have sent it to Fail,
        # but we raise an error here as a safeguard.
        raise ValueError("Missing required inputs for calculation.")

    # 2. WHS Course Handicap Calculation (Par assumed 72)
    # CH = round((HI * (SR / 113)) + (CR - Par))
    course_handicap = round((handicap_index * (slope_rating / 113)) + (course_rating - 72))

    # 3. Return the original event data plus the new calculated value
    event['courseHandicap'] = course_handicap
    return event