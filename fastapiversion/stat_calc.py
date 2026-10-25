from data.db import students


def check_score(score, count5, count4, count3):

    if score >= 86:
        count5 += 1

    elif 86 > score >= 72:
        count4 += 1

    elif 72 > score >= 56:
        count3 += 1

    return (count5, count4, count3)

def score_stats(students):

    score_res_list = []

    for student in students:
        
        count5, count4, count3 = 0, 0, 0

        count5, count4, count3 = check_score(student.inf_score, count5, count4, count3)
        count5, count4, count3 = check_score(student.math_score, count5, count4, count3)
        count5, count4, count3 = check_score(student.history_score, count5, count4, count3)

        score_res_list.append((count5, count4, count3))
    
    return score_res_list
