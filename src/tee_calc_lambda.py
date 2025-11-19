import json # Not strictly required here, but good practice
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # 1. Extract inputs (Updated to match test payload keys)
    handicap_index = event.get('handicapIndex')
    slope = event.get('slope')      # <--- Changed from 'slopeRating'
    rating = event.get('rating')    # <--- Changed from 'courseRating'

    # Simple validation (using the new keys)
    if not all([handicap_index, slope, rating]):
        raise ValueError("Missing required inputs for calculation.")

    # 2. WHS Course Handicap Calculation (Par assumed 72)
    # CH = round((HI * (Slope / 113)) + (CR - Par))
    # We use the 'slope' and 'rating' variables here
    course_handicap = round((handicap_index * (slope / 113)) + (rating - 72))

    # 3. Return the original event data plus the new calculated value
    event['courseHandicap'] = course_handicap
    return event