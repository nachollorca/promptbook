# TODO: include inputs to modify number of paragraphs/sentences etc.
def write_cover_letter(
        job: str,
        resume: str,
        language: str = "English",
        style: str = None,
        vocabulary: str = None,
) -> str:
    prompt = f"""
Your task is to write a cover letter in {language} language for the job posting delimited by quotation marks below:

"{job}" 

Use the information from my resume delimited by quotation marks below, only when you feel it advantageous.

"{resume}"

Perform the following actions:
 1. Write a paragraph of maximum 6 sentences explaining why I would like to work with them and praising their business.
 2. Write a paragraph of maximum 7 sentences explaining why I am a wonderful fit for the role and how my experience aligns perfectly with the position.
 3. Write a short closing paragraph re-stating my interest and hoping to hear from them soon.

"""
    if style is not None:
        prompt = prompt + f"Use a {style} voice tone."

    if vocabulary is not None:
        prompt = prompt + f"Use {vocabulary} vocabulary."

    return prompt

job_example = """Job Description: Community Bank is looking for an outgoing individual to serve as the face of our institution.

About Community Bank: Community Bank is a local leader in financial services. Founded in 1821, our bank serves the needs of area customers with personal and business banking and wealth management services. Regardless of what our customers’ needs are, we meet them with the personalized attention only a community bank can provide.

What it’s Like to Work Here: Ask our employees and the one word they’d use to describe working at Community Bank is “great.” Our team members all share a positive attitude, problem solving abilities and patience, enabling them to provide excellent customer service even during fast-paced shifts. Our culture, plus continuous opportunities for growth, have resulted in an industry-low turnover rate. Don’t miss out on this rare opening with us!

A Day in the Life as a Teller: As the first person customers engage with when entering the bank, you will help complete transactions, uncover financial needs, recommend products/services to help them meet their goals, and refer them to other specialists at the bank if appropriate. With each transaction, you will need to ensure compliance with our policies, procedures and security requirements as well as government regulations.

Qualifications to be a Teller: No special skills are required but some requirements mean you have the potential to be a great teller:

    Cash handling skills
    Caring attitude
    Detail oriented
    Good communications skills
    Strong math skills
    Knowledge of core computer programs and aptitude for working with new systems and software

Ready to apply? If this job sounds like a fit for you, then click on the ‘apply’ button below. Good luck!
"""

resume_example = """[Your Name]
[Your Address]
[City, State, ZIP Code]
[Your Email Address]
[Your Phone Number]
[LinkedIn Profile (Optional)]

Objective:
Dedicated and results-driven professional seeking a challenging banking position to utilize my expertise in financial analysis, risk management, and exceptional customer service skills. With a strong commitment to ethical and responsible banking practices, I aim to contribute to the growth and success of a reputable financial institution.

Education:
Bachelor of Business Administration in Finance
[University Name]
[City, State]
[Graduation Date: Month, Year]

Relevant Courses:

    Financial Management
    Investment Analysis
    Banking and Financial Services
    Risk Management
    Accounting Principles

Professional Experience:

Banking Associate
[Bank Name]
[City, State]
[Dates of Employment: Month, Year - Present]

    Assist customers with their banking needs, including deposits, withdrawals, and account inquiries, ensuring a high level of customer satisfaction.
    Promote and cross-sell various financial products and services, resulting in a 15% increase in the bank's product adoption rate.
    Conduct financial analyses to assess customers' financial needs and provide tailored solutions, leading to improved client financial health.
    Collaborate with team members to maintain a clean and organized banking environment, which earned recognition from management for a neat and efficient workspace.
    Adhere to strict compliance with banking regulations, including the Bank Secrecy Act (BSA) and Anti-Money Laundering (AML) guidelines, ensuring a secure banking environment.

Intern - Risk Management Department
[Financial Institution Name]
[City, State]
[Dates of Internship: Month, Year - Month, Year]

    Assisted in identifying, analyzing, and mitigating potential risks associated with the bank's lending and investment activities.
    Conducted research and created reports on industry trends, credit risk, and market risk, providing valuable insights to senior risk analysts.
    Contributed to the development of stress testing scenarios and risk models, enhancing the bank's risk assessment capabilities.
    Collaborated with cross-functional teams to ensure compliance with regulatory requirements and internal risk management policies.
    Participated in meetings with regulatory authorities, gaining insight into regulatory compliance and risk assessment practices.

Skills:

    Financial Analysis
    Risk Management
    Customer Service
    Financial Products Sales
    Banking Regulations
    Data Analysis
    Microsoft Office Suite
    Communication Skills
    Problem Solving
    Attention to Detail

Certifications:

    Certified Banking Professional (CBP)
    Anti-Money Laundering (AML) Certification
    Financial Industry Regulatory Authority (FINRA) Series 6 and Series 63 (or relevant licenses)

Languages:

    Fluent in English and [Any Additional Languages]

Professional Memberships:

    American Bankers Association
    Financial Management Association
"""

_title = "Cover Letter Builder"
_description = "Produce quick Cover Letters by just introducing the job offer and information about yourself."
_ui = {
    "job": {
        "help": "The job posting text.",
        "suggestions": job_example,
    },
    "resume": {
        "help": "Your CV. If your resume supports ATS (it really should, check online), you can just copy paste its text in here.",
        "suggestions": resume_example,
    },
    "style": {
        "suggestions": "simple, formal, creative and excited..."
    },
    "vocabulary": {
        "suggestions": "technical, academic..."
    },
}

