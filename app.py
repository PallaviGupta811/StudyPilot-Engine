import streamlit as st

from pdf_export import create_pdf

from planner import (
    create_schedule,
    generate_daily_plan,
    generate_topic_plan
)

from syllabus_parser import load_syllabus_json


st.title("📚 StudyPilot Engine")

uploaded_file = st.file_uploader(
    "Upload Syllabus PDF",
    type=["pdf"]
)

study_hours = st.slider(
    "Available Study Hours",
    min_value=1,
    max_value=12,
    value=8
)


if st.button("Generate Study Plan"):

    try:

        data = load_syllabus_json()

        subjects = data["subjects"]

        st.success(
            "Syllabus Loaded Successfully"
        )

        total_subjects = len(
            subjects
        )

        total_topics = sum(
            len(
                subject.get(
                    "topics",
                    []
                )
            )
            for subject in subjects
        )

        st.subheader(
            "📊 Summary"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Subjects",
                total_subjects
            )

        with col2:

            st.metric(
                "Topics",
                total_topics
            )

        st.subheader(
            "📘 Topics To Study"
        )

        for subject in subjects:

            with st.expander(
                subject["name"]
            ):

                for topic in subject.get(
                    "topics",
                    []
                ):

                    st.write(
                        f"• {topic}"
                    )

        schedule = create_schedule(
            subjects,
            study_hours
        )

        daily_plan = generate_daily_plan(
            schedule
        )

        st.subheader(
            "📅 Today's Study Plan"
        )

        for session in daily_plan:

            st.write(
                f"📖 {session['subject']} "
                f"({session['start']} → "
                f"{session['end']})"
            )

        if st.button(
            "Export PDF"
        ):

            pdf_file = create_pdf(
                daily_plan
            )

            st.success(
                "PDF Created Successfully!"
            )

            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="Download PDF",
                    data=file,
                    file_name="study_plan.pdf",
                    mime="application/pdf"
                )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )