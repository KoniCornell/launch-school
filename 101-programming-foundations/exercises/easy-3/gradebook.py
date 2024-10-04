def get_grade(grade1: int, grade2: int, grade3: int):
    average = (grade1 + grade2 + grade3) / 3
    score = average
    
    # using match case
    # it is easier to use if elif else

    match score:
        case score if 90 <= score <= 100:
            return 'A'
        case score if 80 <= score < 90:
            return 'B'
        case score if 70 <= score < 80:
            return 'C'
        case score if 60 <= score < 70:
            return 'D'
        case score if 0 <= score < 60:
            return 'F'
        case _:
            return 'Invalid score'  # For any score outside the 0-100 range
