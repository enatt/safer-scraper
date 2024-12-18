## NOTE: ##
# This dictionary is constructed to handle reading of the 2023 SAFER Report
# Each key in the dictionary represents the name of the governing act.
# Keys are truncated to match how the act name appears in the FIRST LINE
# of the page in the SAFER report (ex., page 18 of the 2023 report is represented
# here as "Barber, Cosmetology, Esthetics, Hair Braiding, and Nail")

# Values are a list of the licenses governed by that act. In the case that
# an act covers several pages in the SAFER report, it is a list of lists,
# one list for each page.

# Each year, the list of governed licenses changes slightly
# Sometimes the act name changes, sometimes the regulated licenses change
# If running on years OTHER than 2023, make sure to make the necessary changes
# to which licenses are associated with which acts.
# If the act name changes, alter the key
# If the regulated licenses change, alter the value

license_dict = {
    "Acupuncture Practice Act": ["Acupuncture CE Sponsor", "Licensed Acupuncturist"],
    "Cemetery Oversight Act": [
        "Licensed Cemetery Authority",
        "Licensed Cemetery Customer Service Employee",
        "Licensed Cemetery Exempt",
        "Licensed Cemetery Manager",
        "Licensed Cemetery Partially Exempt",
        "Licensed Cemetery CE Sponsor",
    ],
    "Barber, Cosmetology, Esthetics, Hair Braiding, and Nail": [
        [
            "BCENT*** Continuing Education Sponsor",
            "Licensed Hair Braiding School",
            "BCENT*** Salon/Shop Registration",
            "Licensed Barber",
            "Licensed Barber School",
            "Licensed Barber Teacher",
        ],
        [
            "Licensed Cosmetologist",
            "Licensed Cosmetologist Teacher",
            "Licensed Cosmetology School",
            "Licensed Esthetician",
            "Licensed Esthetician Teacher",
        ],
        [
            "Licensed Esthetician School",
            "Licensed Hair Braider",
            "Licensed Hair Braider Teacher",
            "Licensed Nail Technician",
            "Licensed Nail Technology Teacher",
        ],
        [
            "BCENT Domestic Violence CE Sponsor",
            "Licensed Cosmetology School PUBLIC",
            "Licensed Nail Technician School",
            "Licensed Hair Braiding School",
        ],
    ],
    "Private Detective, Private Alarm, Private Security,": [
        [
            "Armed Proprietary Security Force",
            "Canine Handler Authorization Card",
            "Canine Trainer Authorization Card",
            "Firearm Control Card",
            "Licensed Alarm Contractor Agency Branch Office",
        ],
        [
            "Licensed Fingerprint Vendor",
            "Licensed Fingerprint Vendor Agency",
            "Licensed Locksmith",
            "Licensed Locksmith Agency",
            "Licensed Private Alarm Contractor",
        ],
        [
            "Licensed Private Alarm Contractor Agency",
            "Licensed Private Detective",
            "Licensed Private Detective Agency",
            "Licensed Private Detective Agency Branch Office",
            "Licensed Private Security Contractor",
        ],
        [
            "Licensed Private Security Contractor Agency",
            "Licensed Private Security Contractor Agency Branch Office",
            "Permanent Employee Registration",
            "Registered Firearm Instructor",
        ],
        [
            "Canine Instructor Training Course",
            "Firearm Training Course",
            "Licensed Locksmith Agency Branch Office",
            "Original Firearms Training",
        ],
        ["Firearm Control Card-IROCC Waiver"],
    ],
    "Home Medical Equipment and Services": [
        "Home Medical Equipment and Services Provider"
    ],
    "Electrologist Licensing Act": ["Licensed Electrologist"],
    "Marriage and Family Therapy Licensing Act": [
        "Associate Licensed Marriage and Family Therapist",
        "Licensed Marriage and Family Therapist",
        "Marriage and Therapy Continuing Education Sponsor",
    ],
    "Massage Licensing Act": [
        "Licensed Massage Therapist",
        "Massage Continuing Education Sponsor",
    ],
    "Nursing Home Administrators Licensing and": [
        "Approved Nursing Home Administrator Continuing Education Sponsor",
        "Licensed Nursing Home Administrator",
        "Licensed Nursing Home Administrator Temporary",
    ],
    "Pharmacy Practice Act": [
        "Pharmacy Controlled Substance License",
        "Licensed Pharmacy",
        "Pharmacy Technician",
        "Registered Pharmacist",
    ],
    "Professional Counselor and Clinical Professional Counselor": [
        "Licensed Clinical Professional Counselor",
        "Licensed Professional Counselor",
        "Professional Counselor Continuing Education Sponsor",
    ],
    # Ones above -- 16 occupations we care about
    # Ones below -- others
    "Cannabis Regulation and Tax Act": [
        "Registered Adult Use Cannabis Dispensing Organization",
        "Registered Adult Use Agent",
        "Registered Adult Use Agent-In-Charge",
        "Registered Adult Use Principal Officer",
    ],
    "Architecture Practice Act of 1989": ["Architect"],
    "Illinois Athletic Trainers Practice Act": ["Athletic Trainer"],
    "Boxing and Full-contact Martial Arts Act": [
        "Licensed Amateur FCMA*** Promoter",
        "Licensed Boxer",
        "Licensed Boxing Judge",
        "Licensed Boxing Manager",
        "Licensed Boxing Promoter",
    ],
    "Boxing and Full-contact Martial Arts Act (cont’d)": [
        [
            "Licensed Boxing Referee",
            "Licensed Boxing Second",
            "Licensed FCMA*** Contestant",
            "Licensed FCMA*** Promoter",
            "Licensed FCMA*** Referee",
        ],
        [
            "Licensed FCMA*** Judge",
            "Licensed FCMA*** Manager",
            "Licensed FCMA*** Matchmaker",
            "Licensed FCMA*** Second",
            "Licensed FCMA*** Referee",
        ],
        [
            "Licensed MMA Contestant",
            "Licensed Timekeeper",
            "Licensed Boxing Matchmaker",
        ],
    ],
    "Clinical Psychologist Licensing Act": [
        "Clinical Psychologist",
        "Licensed Psychological Partnership",
        "Prescribing Psychologist",
        "Prescribing Psychologist Controlled Substances",
        "Psychologist Continuing Education Sponsor",
    ],
    "Clinical Psychologist Licensing Act (cont’d)": [
        "Prescribing Pschologist Clinical Rotation Program",
        "Licensed Psychological Corporation",
    ],
    "Collection Agency Act": [
        "Licensed Collection Agency",
        "Licensed Collection Agency Branch Office",
    ],
    "Controlled Substances Act": ["Controlled Substances License***"],
    "Illinois Dental Practice Act": [
        "Approved Dental/Dental Hygienist Continuing Education Sponsor",
        "Dental Sedatoin Permit",
        "Licensed Dentist",
        "Licensed Dentist Controlled Substance",
        "Licensed Specialist in Dentistry",
    ],
    "Illinois Dental Practice Act (cont’d)": [
        "Registered Dental Hygienist",
        "Registered Faculty License",
        "Temporary Dental Training License",
    ],
    "Design Firm Registration": [
        "Land Surveyor, Architect, Professional Engineering, Structural Engineering",
        "Architect",
        "Architect, Professional Engineering",
        "Land Surveyor",
    ],
    "Design Firm Registration (cont’d)": [
        [
            "Land Surveyor, Professional Engineering",
            "Professional Engineering, Structural Engineering",
            "Professional Engineering",
            "Structural Engineering",
        ],
        [
            "Land Surveyor, Professional Engineering, Structural Engineering",
            "Architect Professional Engineering, Structural Engineering",
            "Architects/Structural Engineer",
        ],
    ],
    "Design Firm Registration (cont'd)": [
        [
            "Land Surveyor, Professional Engineering",
            "Professional Engineering, Structural Engineering",
            "Professional Engineering",
            "Structural Engineering",
        ],
        [
            "Land Surveyor, Professional Engineering, Structural Engineering",
            "Architect Professional Engineering, Structural Engineering",
            "Architects/Structural Engineer",
        ],
    ],
    "Detection of Deception Examiners Act": [
        "Detection of Deception Examiner",
        "Detection of Deception Trainee",
    ],
    "Dietitian Nutritionist Practice Act": [
        "Dietitian/Nutrition Counselor Continuing Education Sponsor",
        "Licensed Dietitian Nutritionist",
    ],
    "Environmental Health Practitioner Licensing Act": [
        "Environmental Health Practitioner Continuing Education Sponsor",
        "Environmental Health Practitioner in Training",
        "Licensed Environmental Health Practitioner",
    ],
    "Funeral Directors and Embalmers Licensing Code": [
        "FUneral Director and Embalmer Continuing Education Sponsor",
        "Licensed Funeral Director and Embalmer",
        "Licensed Funeral Director and Embalmer Intern",
    ],
    "Professional Geologist Licensing Code": ["Licensed Professional Geologist"],
    "Humane Euthanasia in Animal Shelters Act": [
        "Certified Euthanasia Agency",
        "Certified Euthanasia Agency Controlled Substance",
        "Certified Euthanasia Technician",
    ],
    "Genetic Counselor Licensing Act": [
        "Genetic Counselor",
        "Temporary Genetic Counselor",
    ],
    "Registered Interior Designers Act": ["Registered Interior Designer"],
    "Illinois Professional Land Surveyor Act of 1989": [
        "Licensed Professional Land Surveyor",
        "Surveyor Intern",
    ],
    "Limited Liability Company Act": ["Professional Limited Liability Company"],
    "Medical Practice Act of 1987": [
        "Continuing Medical Education Sponsor",
        "Licensed Chiropractic Physician",
        "Licensed Physician and Surgeon",
        "Licensed Physician Controlled Substance",
        "Limited Medical Temporary Permit",
    ],
    "Medical Practice Act of 1987 (cont’d)": [
        "Temporary Medical Permit",
        "Visiting Physician Permit",
        "Visiting Physician Professor",
        "Visiting Resident",
    ],
    "Compassionate Use of Medical Cannabis Pilot Program Act": [
        "Registered Agent",
        "Registered Agent in Charge",
        "Registered Principal Officer",
        "Registered Medical Cannabis Dispensing Organizaiton",
    ],
    "Compassionate Use of Medical Cannabis Program Act": [
        "Registered Agent",
        "Registered Agent in Charge",
        "Registered Principal Officer",
        "Registered Medical Cannabis Dispensing Organization",
    ],
    "Medical Corporation Act": ["Registered Medical Corporation"],
    "Naprapathic Practice Act": ["Licensed Naprapath", "Naprapath CE Sponsor"],
    "Nurse Practice Act": [
        "Advanced Practice Registered Nurse",
        "Advanced Practice Nurse Controlled Substance",
        "Nurse Continuing Education Sponsor",
    ],
    "Nurse Practice Act (cont’d)": [
        "Licensed Practical Nurse",
        "Registered Professional Nurse",
        "Full Practice Authority APRN",
        "Full Practice Authority APRN Controlled Substance License",
    ],
    "Illinois Occupational Therapy Practice Act": [
        "Certified Occupational Therapy Assistant",
        "Occupational Therapist",
        "Occupational Therapy Continuing Education Sponsor",
    ],
    "Illinois Optometric Practice Act of 1987": [
        "Licensed Optometrist",
        "Licensed Optometrist Ancillary Office",
        "Licensed Optometry CE Sponsor",
        "Mail Order Ophthalmic Provider",
        "Optometrist Controlled Substance",
    ],
    "Orthotics, Prosthetics, and Pedorthics Practice Act": [
        "Licensed Orthotist",
        "Licensed Pedorthist",
        "Licensed Prosthetist",
    ],
    "Perfusionist Practice Act": ["Licensed Perfusionist"],
    "Illinois Physical Therapy Act": [
        "Licensed Physical Therapist",
        "Licensed Physical Therapist Assistant",
        "Physical Therapy Continuing Education Sponsor",
    ],
    "Physician Assistant Practice Act of 1987": [
        "Licensed Physician Assistant",
        "Physician Assistant Controlled Substance",
    ],
    "Podiatric Medical Practice Act of 1987": [
        "Licensed Podiatric Physician",
        "Licensed Podiatry Controlled Substance",
        "Temporary Podiatric Physician",
    ],
    "Professional Service Corporation Act": [
        "Registered Professional Service Corporation"
    ],
    "Professional Engineering Practice Act of 1989": [
        "Enrolled Professional Engineer Intern",
        "Licensed Professional Engineer",
    ],
    "Illinois Public Accounting Act": [
        "Licensed Certified Public Accountant",
        "Public Accountant Continuing Education Sponsor",
        "Public Accountant Firm License",
        "Registered Certified Public Accountant",
    ],
    "Respiratory Care Practice Act": [
        "Respiratory Care Practicioner",
        "Respiratory Care Practitioner CE Sponsor",
    ],
    "Illinois Roofing Industry Licensing Act": [
        "Licensed Roofing Contractor",
        "Qualifying Party Roofing Contractor",
    ],
    "Sex Offender Evaluation and Treatment Provider Act": [
        "Associate Sex Offender Provider",
        "Sex Offender Evaluator",
        "Sex Offender Treatment Provider",
    ],
    "Illinois Certified Shorthand Reporters Act of 1984": [
        "Certified Shorthand Reporter",
        "Restricted Shorthand Reporter",
    ],
    "Clinical Social Work and Social Work Practice Act": [
        "Licensed Clinical Social Worker",
        "Licensed Social Worker",
        "Registered Social Worker Continuing Education Sponsor",
    ],
    "Illinois Speech-Language Pathology and": [
        "Licensed Audiologist",
        "Licensed Speech Language Pathology Temporary",
        "Speech Language Pathologist",
        "Speech Language Pathology and Audiology Continuing Education Sponsor",
        "Speech-Langauge Pathology and Audiology Assitant",
    ],
    "Structural Engineering Practice Act of 1989": [
        "Enrolled Structural Engineering Intern",
        "Licensed Structural Engineer",
    ],
    "Registered Surgical Assistant and Registered Surgical": [
        "Registered Surgical Assistant",
        "Registered Surgical Technologist",
    ],
    "Wholesale Drug Distribution Licensing Act": [
        "Wholesale Drug Distributor",
        "Wholesale Drug Distributor Controlled Substance",
    ],
    "Wholesale Drug Distribution Licensing Act (cont’d)": [
        "Wholesale Drug Third Party Logistics Provider",
        "Wholesale Drug Third Party Logistics Provider Controlled Substance",
    ],
    "Veterinary Medicine and Surgery Practice Act of 2004": [
        "Certified Veterinary Technician",
        "Licensed Veterinarian",
        "Licensed Veterinarian Controlled Substance",
    ],
    "Real Estate Appraiser Licensing Act of 2002": [
        "Certified General Real Estate Appraiser",
        "Certified Residential Real Estate Appraiser",
        "Associate Real Estate Trainee Appraiser",
        "Temporary Practice Real Estate Appraiser",
        "Appraiser Education Provider",
    ],
    "Appraisal Management Company Registration Act": ["Appraisal Management Company"],
    "Auction License Act": [
        "Auctioneer",
        "Auction Firm",
        "Auction Continuing Education School",
    ],
    "Community Association Manager Licensing and": [
        "Community Association Manager",
        "Community Association Firm",
    ],
    "Home Inspector License Act": [
        "Home Inspector",
        "Home Inspector Entity",
        "Home Inspector Education Provider",
    ],
    "Real Estate License Act of 2000": [
        "Real Estate Managing Broker",
        "Real Estate Broker",
        "Residential Leasing Agent",
        "Residential Leasing Agent Permit",
    ],
    "Real Estate License Act of 2000 (cont’d)": [
        "Real Estate Entity or Firm",
        "Real Estate Branch Office",
        "Real Estate Education Provider",
        "Real Estate Education Provider Instructor",
    ],
}
