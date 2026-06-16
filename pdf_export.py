from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_pdf(schedule):

    pdf = SimpleDocTemplate(
        "study_plan.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "StudyPilot Study Plan",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 12)
    )

    for session in schedule:

        text = (
            f"{session['subject']} : "
            f"{session['start']} -> "
            f"{session['end']}"
        )

        content.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 6)
        )

    pdf.build(content)

    return "study_plan.pdf"