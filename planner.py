from datetime import datetime


def calculate_priorities(subjects):

    today = datetime.today()

    for subject in subjects:

        # If no exam date exists,
        # give equal priority
        if "exam_date" not in subject:

            subject["priority"] = 1

        else:

            exam_date = datetime.strptime(
                subject["exam_date"],
                "%Y-%m-%d"
            )

            days_left = (
                exam_date - today
            ).days

            if days_left <= 0:
                days_left = 1

            subject["priority"] = (
                1 / days_left
            )

    return sorted(
        subjects,
        key=lambda x: x["priority"],
        reverse=True
    )


def create_schedule(
    subjects,
    total_hours
):

    subjects = calculate_priorities(
        subjects
    )

    total_priority = sum(
        subject["priority"]
        for subject in subjects
    )

    schedule = []

    for subject in subjects:

        allocated_hours = (
            subject["priority"]
            / total_priority
        ) * total_hours

        schedule.append(
            {
                "subject": subject["name"],
                "hours": round(
                    allocated_hours,
                    1
                )
            }
        )

    return schedule


def generate_daily_plan(
    schedule
):

    current_hour = 9

    daily_plan = []

    for item in schedule:

        start_time = round(
        current_hour,
        1
        )

        end_time = round(
        current_hour
        + item["hours"],
        1
        )

        daily_plan.append(
            {
                "subject": item["subject"],
                "start": start_time,
                "end": round(
                    end_time,
                    1
                )
            }
        )

        current_hour = end_time

    return daily_plan


def generate_topic_plan(
    subjects
):

    topic_plan = []

    for subject in subjects:

        for topic in subject.get(
            "topics",
            []
        ):

            topic_plan.append(
                {
                    "subject": subject["name"],
                    "topic": topic
                }
            )

    return topic_plan