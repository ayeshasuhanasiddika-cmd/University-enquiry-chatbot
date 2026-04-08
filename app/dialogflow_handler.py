def detect_intent_from_text(text_input, session_id=None):

    if not text_input:
        return "Please enter a message."

    text = text_input.lower()

    # Greeting
    if "hi" in text or "hello" in text:
        return "Hello! Welcome to Davanagere University. How can I help you today?"

    # College Name
    elif "college name" in text or "university" in text:
        return "The college name is Davanagere University, Davanagere."

    # HOD Name
    elif "hod" in text or "head of department" in text:
        return "The Head of Department is DR. PROFESSOR BASSANNA SIR."

    # ---------------- SUBJECTS ----------------

    elif "subject" in text and "bca" in text:
        return (
            "The subjects in BCA include Programming in C, Data Structures, "
            "Database Management Systems, Web Development, Computer Networks, and Software Engineering."
        )

    elif "subject" in text and "mca" in text:
        return (
            "The subjects in MCA include Advanced Java, Python Programming, "
            "Data Science, Cloud Computing, Artificial Intelligence, and Software Testing."
        )

    elif "subject" in text and "btech" in text:
        return (
            "The subjects in B.Tech include Engineering Mathematics, Programming, "
            "Operating Systems, Computer Networks, Machine Learning, and Project Work."
        )

    # ---------------- SEMESTERS ----------------

    elif "semester" in text and "bca" in text:
        return "BCA has 6 semesters."

    elif "semester" in text and "mca" in text:
        return "MCA has 4 semesters."

    elif "semester" in text and "btech" in text:
        return "B.Tech has 8 semesters."

    # ---------------- INTERNSHIP ----------------

    elif "internship" in text:
        return (
            "Yes, internship opportunities are provided in the final year. "
            "Students can work with companies to gain practical experience."
        )

    # ---------------- PLACEMENT ----------------

    elif "placement" in text and "how many" in text:
        return (
            "Currently, around 120 students have been placed in reputed companies "
            "through campus placement drives."
        )

    elif "placement" in text:
        return (
            "Yes, placement drives are conducted every year. "
            "Top companies visit the campus for recruitment."
        )

    # ---------------- COURSES ----------------

    elif "course" in text:
        return "We offer courses like BCA, MCA, and B.Tech."

    # ---------------- FEES ----------------

    elif "bca" in text and "fee" in text:
        return "The BCA fee structure is approximately ₹25,000 per year."

    elif "mca" in text and "fee" in text:
        return "The MCA fee structure is approximately ₹35,000 per year."

    elif "btech" in text and "fee" in text:
        return "The B.Tech fee structure is approximately ₹60,000 per year."

    # Installment / EMI
    elif "installment" in text or "emi" in text:
        return "Yes, the fee can be paid in 2 installments."

    # Contact
    elif "contact" in text:
        return "You can contact the university office at 08192-123456."

    # Location
    elif "location" in text or "address" in text:
        return "Davanagere University is located in Davanagere, Karnataka."
    
    elif "thank you" in text or "thanks" in text:
        return (
        "You're welcome! If you have any more questions about the college, "
        "feel free to ask. I hope you have a great day!"
    )
     
    else:
        return "Sorry, I did not understand your question. Please try again."