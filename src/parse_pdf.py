import fitz


def extract_police_report_data(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc[0]
    blocks = page.get_text("blocks", sort=True)

    keys = {
        "Report Number:": "Report Number",
        "Date & Time:": "Date & Time",
        "Reporting Officer:": "Reporting Officer",
        "Incident Location:": "Incident Location",
        "Coordinates:": "Coordinates",
        "Detailed Description:": "Detailed Description",
        "Police District:": "Police District",
        "Resolution:": "Resolution",
        "Suspect Description:": "Suspect Description",
        "Victim Information:": "Victim Information",
    }

    data = {}
    current_key = None

    for block in blocks:
        text = block[4].strip()

        for key, mapped_key in keys.items():
            if key in text:
                current_key = mapped_key
                value = text.replace(key, "").strip()
                data[current_key] = value
                break  # move to next block if key is found

        # handle multi-line description
        if current_key == "Detailed Description" and current_key in data:
            cleaned_text = text.replace("Detailed Description:", "").strip()
            if cleaned_text:
                data[current_key] += " " + cleaned_text

        else:
            current_key = None

    return data
