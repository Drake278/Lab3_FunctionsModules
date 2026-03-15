
print("heres ur grades") #This is a terminal test

import grades

LAST_NAME = "MARQUEZ"          
STUDENT_ID = "TUPM-25-0080"     

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)


scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark(grade)

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("=" * 40)


from access_control import compute_access_level, validate_access, audit_log


SEED_NUM = int(0)
FAVORITE_ARTIST = "PIERCE THE VEIL"


CONTROL_NUM = max(1, SEED_NUM)

@audit_log
def run_authorization():
   
    level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
    
   
    decision = validate_access(level, CONTROL_NUM)
    
    
    print(f"Control Number: {CONTROL_NUM}")
    print(f"Computed Access Level: {level}")
    print(f"Final Decision: {decision}")

if __name__ == "__main__":
    run_authorization()



from access_control import signal_shutdown

initial_power = CONTROL_NUM + len(FAVORITE_ARTIST)

print("\n--- Mission: Recursive Signal Shutdown ---")
total_calls = signal_shutdown(initial_power)

print(f"Total Recursive Calls: {total_calls}")



from media_engine import play_count_stream, monitor


stream_limit = CONTROL_NUM + len(FAVORITE_ARTIST)

@monitor
def run_analytics(limit):
    total_plays = 0
    records_processed = 0
    generated_counts = []

    
    for count in play_count_stream(limit):
        generated_counts.append(count)
        total_plays += count
        records_processed += 1
    
    
    print(f"Computed Stream Limit: {limit}")
    print(f"Generated Play Counts: {generated_counts}")
    print(f"Total Plays: {total_plays}")
    print(f"Number of Records Processed: {records_processed}")

if __name__ == "__main__":
    print("\n--- Mission: Streaming Media Analytics ---")
    run_analytics(stream_limit)