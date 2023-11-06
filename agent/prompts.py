from datetime import datetime
def generate_agent_role_prompt(agent):
    """ Generates the agent role prompt.
    Args: agent (str): The type of the agent.
    Returns: str: The agent role prompt.
    """
    prompts = {
        "Finance Agent": "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends.",
        "Travel Agent": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights.",
        "Academic Research Agent": "You are an AI academic research assistant. Your primary responsibility is to create thorough, academically rigorous, unbiased, and systematically organized reports on a given research topic, following the standards of scholarly work.",
        "Business Analyst": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis.",
        "Computer Security Analyst Agent": "You are an AI specializing in computer security analysis. Your principal duty is to generate comprehensive, meticulously detailed, impartial, and systematically structured reports on computer security topics. This includes Exploits, Techniques, Threat Actors, and Advanced Persistent Threat (APT) Groups. All produced reports should adhere to the highest standards of scholarly work and provide in-depth insights into the complexities of computer security.",
        "Default Agent": "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."
    }

    return prompts.get(agent, "No such agent")


# def generate_report_prompt(question, research_summary):
#     """ Generates the report prompt for the given question and research summary.
#     Args: question (str): The question to generate the report prompt for
#             research_summary (str): The research summary to generate the report prompt for
#     Returns: str: The report prompt for the given question and research summary
#     """

#     return f'"""{research_summary}""" Using the above information, provide details about the following'\
#            f' company: "{question}" in a detailed report --'\
#            " The report should contain the following:" \
#            "1. Industrial Analysis (Textual content that analyses the industry of the prospect company)" \
#             "2. Relevant News (List or highlight of recent news articles about the prospect company)" \
#             f'3. An draft/template Email to "{question}" as a salesperson from FCM Travel for reaching out. The length of the Email should be a maximum of 250 words. The Email should sound like the salesperson has investigated the company well and has knowledge about it. The email should contain how FCM services aligns with the need of the company.--'\
#             f'4. A draft/template LinkedIn Message to "{question}" as a salesperson from FCM Travel for reaching out. The length of the Message should be a maximum of 280 charcters. --'\
#             "FCM Travel (known also as FCM Travel Solutions) is a global business travel management company that provided a broad range of corporate travel solutions and services to clients. Here are some of the offerings that FCM Travel Business typically provides to their customers: Corporate Travel Management: FCM helps businesses manage and streamline their corporate travel, ensuring that travelers receive the best possible service for the most efficient cost. Travel Technology: They offer innovative and integrated travel technology solutions, such as their online booking tools, mobile apps, and travel analytics platforms. Expense Management: Solutions that allow companies to better track and manage their travel and entertainment expenses. Travel Policy Development: Assistance in developing and implementing effective corporate travel policies to save costs and ensure traveler safety and compliance. Global Network: With a presence in over 95 countries, FCM has a vast global network that ensures consistent and localized services for their clients, no matter where they travel. 24/7 Emergency Assistance: Around-the-clock customer service and emergency support for travelers, ensuring safety and assistance whenever and wherever required. Negotiated Rates: FCM has strong relationships with suppliers, allowing them to negotiate competitive rates on behalf of their clients for air travel, hotels, car rentals, and other services. Reporting and Analytics: Detailed reporting tools to help companies analyze their travel spend and identify potential savings. Leisure Travel Services: Some FCM offices also provide leisure travel services, helping employees or executives plan their personal or vacation trips. Duty of Care: Solutions and services designed to support and track the health, safety, and security of traveling employees. Sustainability and CSR Initiatives: Many businesses are concerned about their carbon footprint, and FCM offers solutions to track and reduce a company's environmental impact from their travel activities. Group and Meeting Planning: FCM provides planning services for larger groups or for businesses that require organized meetings, incentives, conferences, and events. Remember, the specific offerings might vary by region or country, and they could evolve over time. For the most up-to-date information on FCM Travel Business' services, it would be best to visit their official website or contact them directly." \
#             " The report should focus on the answer to the topics provided, should be well structured, informative," \
#            " in depth, with facts and numbers if available, a minimum of 1,200 words and with markdown syntax and apa format.\n "\
#             "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.\n" \
#            f"Write all used source urls at the end of the report in apa format.\n Make sure all the mentioned topics are covered in the report. \n" \
#            f"Assume that the current date is {datetime.now().strftime('%B %d, %Y')}"

def generate_report_prompt(question, research_summary):
    """ Generates the report prompt for the given question and research summary.
    Args: question (str): The question to generate the report prompt for
            research_summary (str): The research summary to generate the report prompt for
    Returns: str: The report prompt for the given question and research summary
    """

    return f'"""{research_summary}""" Using the above information, provide details about the following'\
           f' company: "{question}" in a detailed report --'\
            " The report should contain the following:" \
            "1. General Information => a. Company Name (Response Type = Text), b. Industry Sector (Response Type = Text), c. Number of Employees (Response Type = Numeric), d. Location of Operations (Response Type = Text)" \
            "2. Environmental: Emissions => a. Do you report GHG emissions according to the GHG Protocol? (Response Type = Yes/No), b. Total Scope 1 emissions (in tonnes CO2e) (Response Type = Numeric), c. Total Scope 2 emissions (in tonnes CO2e) (Response Type = Numeric), d. Total Scope 3 emissions (in tonnes CO2e) (Response Type = Numeric)" \
            "3. Environmental: Energy Use => a. Do you use renewable energy sources according to EU Taxonomy criteria? (Response Type = Yes/No), b. Percentage of total energy from renewable sources (Response Type = Numeric)" \
            "4. Environmental: Water Use => a. Do you manage water discharge, treatment, and recycling? (Response Type = Yes/No), b. Total annual water withdrawal (in cubic meters) (Response Type = Numeric)" \
            " The report should focus on the answer to the topics provided and should be well structured with markdown syntax and apa format \n" \
            "A sample report is:"\
            '''
            General Information:
            Company Name: Acme Corp
            Industry Sector: Manufacturing
            Number of Employees: 250
            Location of Operations: Germany

            Environmental: Emissions
            Do you report GHG emissions according to the GHG Protocol? Yes
            Total Scope 1 emissions (in tonnes CO2e): 1250
            Total Scope 2 emissions (in tonnes CO2e): 965
            Total Scope 3 emissions (in tonnes CO2e): 3075

            Environmental: Energy Use
            Do you use renewable energy sources according to EU Taxonomy criteria? Yes
            Percentage of total energy from renewable sources: 40%

            Environmental: Water Use
            Do you manage water discharge, treatment, and recycling? Yes
            Total annual water withdrawal (in cubic meters): 50
           '''\
            "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.\n" \
           f"Write all used source urls at the end of the report in apa format.\n Make sure all the mentioned topics are covered in the report and is structured as in the sample. \n" \
           f"Assume that the current date is {datetime.now().strftime('%B %d, %Y')}"

# def generate_report_prompt(question, research_summary):
#     """ Generates the report prompt for the given question and research summary.
#     Args: question (str): The question to generate the report prompt for
#             research_summary (str): The research summary to generate the report prompt for
#     Returns: str: The report prompt for the given question and research summary
#     """

#     return f'"""{research_summary}""" Using the above information, provide details about the following'\
#            f' company: "{question}" in a detailed report --'\
#             " The report should contain the following:" \
#             "1. General Information => a. Company Name (Response Type = Text), b. Industry Sector (Response Type = Text), c. Number of Employees (Response Type = Numeric), d. Location of Operations (Response Type = Text)" \
#             "2. Environmental: Emissions => a. Do you report GHG emissions according to the GHG Protocol? (Response Type = Yes/No), b. Total Scope 1 emissions (in tonnes CO2e) (Response Type = Numeric), c. Total Scope 2 emissions (in tonnes CO2e) (Response Type = Numeric), d. Total Scope 3 emissions (in tonnes CO2e) (Response Type = Numeric)" \
#             "3. Environmental: Energy Use => a. Do you use renewable energy sources according to EU Taxonomy criteria? (Response Type = Yes/No), b. Percentage of total energy from renewable sources (Response Type = Numeric)" \
#             "4. Environmental: Water Use => a. Do you manage water discharge, treatment, and recycling? (Response Type = Yes/No), b. Total annual water withdrawal (in cubic meters) (Response Type = Numeric)" \
#             "5. Social: Labor Practices => a. Do you have policies in place to avoid child and forced labor? (Response Type = Yes/No), b. Number of supplier audits conducted on labor practices (Response Type = Numeric)" \
#             "6. Social: Health and Safety => a. Do you offer health and safety training to your employees? (Response Type = Yes/No), b. Frequency of work-related injuries per year (Response Type = Numeric)" \
#             "7. Social: Human Rights => a. Do you have a formal policy addressing human rights issues? (Response Type = Yes/No)" \
#             "8. Governance: Ethics => a. Do you have policies or codes of conduct addressing corruption and bribery? (Response Type = Yes/No)" \
#             "9. Governance: ESG Governance => a. Does your company have an ESG governance structure? (Response Type = Yes/No), b. Frequency of ESG matters discussed at board level (Response Type = Numeric)" \
#             "10. Compliance: EU Taxonomy => a. Do you provide information on how your products contribute to environmental objectives? (Response Type = Yes/No), b. Proportion of turnover aligned with the EU Taxonomy (Response Type = Numeric)" \
#             "11. Performance: ESG Targets => a. Do you set and review ESG targets? (Response Type = Yes/No), b. Progress made toward ESG targets (describe briefly) (Response Type = Text)" \
#             "12. NFRD Specific => a. Description of the principal risks related to sustainability aspects (Response Type = Text), b. Description of the business model and strategy for sustainability (Response Type = Text)" \
#             "13. Lieferkettengesetz Specific => a. Do you assess human rights and environmental risks in your supply chain? (Response Type = Yes/No), b. Description of actions taken to mitigate identified risks (Response Type = Text)" \
#             "14. EU CSDDD Specific => a. Do you perform due diligence in line with EU CSDDD requirements? (Response Type = Yes/No)" \
#             " The report should focus on the answer to the topics provided and should be well structured with markdown syntax and apa format \n" \
#             "A sample report is:"\
#             '''
#             General Information:
#             Company Name: Acme Corp
#             Industry Sector: Manufacturing
#             Number of Employees: 250
#             Location of Operations: Germany

#             Environmental: Emissions
#             Do you report GHG emissions according to the GHG Protocol? Yes
#             Total Scope 1 emissions (in tonnes CO2e): 1250
#             Total Scope 2 emissions (in tonnes CO2e): 965
#             Total Scope 3 emissions (in tonnes CO2e): 3075

#             Environmental: Energy Use
#             Do you use renewable energy sources according to EU Taxonomy criteria? Yes
#             Percentage of total energy from renewable sources: 40%

#             Environmental: Water Use
#             Do you manage water discharge, treatment, and recycling? Yes
#             Total annual water withdrawal (in cubic meters): 50

#             Social: Labor Practices
#             Do you have policies in place to avoid child and forced labor? Yes
#             Number of supplier audits conducted on labor practices: 10

#             Social: Health and Safety
#             Do you offer health and safety training to your employees? Yes
#             Frequency of work-related injuries per year: 2

#             Social: Human Rights
#             Do you have a formal policy addressing human rights issues? Yes

#             Governance: Ethics
#             Do you have policies or codes of conduct addressing corruption and bribery? Yes

#             Governance: ESG Governance
#             Does your company have an ESG governance structure? Yes
#             Frequency of ESG matters discussed at board level: Quarterly

#             Compliance: EU Taxonomy
#             Do you provide information on how your products contribute to environmental objectives? Yes
#             Proportion of turnover aligned with the EU Taxonomy: 75%

#             Performance: ESG Targets
#             Do you set and review ESG targets? Yes
#             Progress made toward ESG targets (describe briefly): Reduced emissions by 10%

#             NFRD Specific
#             Description of the principal risks related to sustainability aspects: Climate change impacts
#             Description of the business model and strategy for sustainability: Circular economy approach

#             Lieferkettengesetz Specific
#             Do you assess human rights and environmental risks in your supply chain? Yes
#             Description of actions taken to mitigate identified risks: Implemented a stricter audit process

#             EU CSDDD Specific
#             Do you perform due diligence in line with EU CSDDD requirements? Yes
#             '''\
#             "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.\n" \
#            f"Write all used source urls at the end of the report in apa format.\n Make sure all the mentioned topics are covered in the report and is structured as in the sample. \n" \
#            f"Assume that the current date is {datetime.now().strftime('%B %d, %Y')}"


# def generate_report_prompt(question, research_summary):
#     """ Generates the report prompt for the given question and research summary.
#     Args: question (str): The question to generate the report prompt for
#             research_summary (str): The research summary to generate the report prompt for
#     Returns: str: The report prompt for the given question and research summary
#     """

#     return f'"""{research_summary}""" Using the above information, provide details about the following'\
#            f' company: "{question}" in a detailed report --'\
#            " The report should contain the following:" \
#            "1. Industrial Analysis (Textual content that analyses the industry of the prospect company)" \
#             "2. Relevant News (List or highlight of recent news articles about the prospect company)" \
#             f'3. An draft/template Email to "{question}" as a salesperson from FCM Travel for reaching out. The length of the Email should be a maximum of 250 words. The Email should sound like the salesperson has investigated the company well and has knowledge about it. The email should contain how FCM services aligns with the need of the company.--'\
#             f'4. A draft/template LinkedIn Message to "{question}" as a salesperson from FCM Travel for reaching out. The length of the Message should be a maximum of 280 charcters. --'\
#             "FCM Travel (known also as FCM Travel Solutions) is a global business travel management company that provided a broad range of corporate travel solutions and services to clients. Here are some of the offerings that FCM Travel Business typically provides to their customers: Corporate Travel Management: FCM helps businesses manage and streamline their corporate travel, ensuring that travelers receive the best possible service for the most efficient cost. Travel Technology: They offer innovative and integrated travel technology solutions, such as their online booking tools, mobile apps, and travel analytics platforms. Expense Management: Solutions that allow companies to better track and manage their travel and entertainment expenses. Travel Policy Development: Assistance in developing and implementing effective corporate travel policies to save costs and ensure traveler safety and compliance. Global Network: With a presence in over 95 countries, FCM has a vast global network that ensures consistent and localized services for their clients, no matter where they travel. 24/7 Emergency Assistance: Around-the-clock customer service and emergency support for travelers, ensuring safety and assistance whenever and wherever required. Negotiated Rates: FCM has strong relationships with suppliers, allowing them to negotiate competitive rates on behalf of their clients for air travel, hotels, car rentals, and other services. Reporting and Analytics: Detailed reporting tools to help companies analyze their travel spend and identify potential savings. Leisure Travel Services: Some FCM offices also provide leisure travel services, helping employees or executives plan their personal or vacation trips. Duty of Care: Solutions and services designed to support and track the health, safety, and security of traveling employees. Sustainability and CSR Initiatives: Many businesses are concerned about their carbon footprint, and FCM offers solutions to track and reduce a company's environmental impact from their travel activities. Group and Meeting Planning: FCM provides planning services for larger groups or for businesses that require organized meetings, incentives, conferences, and events. Remember, the specific offerings might vary by region or country, and they could evolve over time. For the most up-to-date information on FCM Travel Business' services, it would be best to visit their official website or contact them directly." \
#             " The report should focus on the answer to the topics provided, should be well structured, informative," \
#            " in depth, with facts and numbers if available, a minimum of 1,200 words and with markdown syntax and apa format.\n "\
#             "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.\n" \
#            f"Write all used source urls at the end of the report in apa format.\n Make sure all the mentioned topics are covered in the report. \n" \
#            f"Assume that the current date is {datetime.now().strftime('%B %d, %Y')}"


def generate_search_queries_prompt(question, link):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """

    return f'Write 6 google search queries to search online that scrapes in depth data about the following company: "{question}"'\
        f'Company locationo of operation is:"{link}"'\
        f'Questions should be such that they provide data for company General Information, Environmental: Emissions, Environmental: Energy Use, Environmental: Water Use'\
        f'Use the current date if needed: {datetime.now().strftime("%B %d, %Y")}.\n' \
        f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3"].'

# def generate_search_queries_prompt(question, link):
#     """ Generates the search queries prompt for the given question.
#     Args: question (str): The question to generate the search queries prompt for
#     Returns: str: The search queries prompt for the given question
#     """

#     return f'Write 10 google search queries to search online that scrapes in depth data about the following company: "{question}"'\
#         f'Company locationo of operation is:"{link}"'\
#             f'Questions should be such that they provide data for company General Information, Environmental: Emissions, Environmental: Energy Use, Environmental: Water Use, Social: Labor Practices, Social: Health and Safety, Social: Human Rights, Governance: ESG Governance, Governance: Ethics,Compliance: EU Taxonomy, Performance: ESG Targets, NFRD Specific, Lieferkettengesetz Specific, EU CSDDD Specific'\
#            f'Use the current date if needed: {datetime.now().strftime("%B %d, %Y")}.\n' \
#            f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3"].'


# def generate_resource_report_prompt(question, research_summary):
#     """Generates the resource report prompt for the given question and research summary.

#     Args:
#         question (str): The question to generate the resource report prompt for.
#         research_summary (str): The research summary to generate the resource report prompt for.

#     Returns:
#         str: The resource report prompt for the given question and research summary.
#     """
#     return f'"""{research_summary}""" Based on the above information, generate a bibliography recommendation report for the following' \
#            f' question or topic: "{question}". The report should provide a detailed analysis of each recommended resource,' \
#            ' explaining how each source can contribute to finding answers to the research question.' \
#            ' Focus on the relevance, reliability, and significance of each source.' \
#            ' Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax.' \
#            ' Include relevant facts, figures, and numbers whenever available.' \
#            ' The report should have a minimum length of 1,200 words.'


# def generate_outline_report_prompt(question, research_summary):
#     """ Generates the outline report prompt for the given question and research summary.
#     Args: question (str): The question to generate the outline report prompt for
#             research_summary (str): The research summary to generate the outline report prompt for
#     Returns: str: The outline report prompt for the given question and research summary
#     """

#     return f'"""{research_summary}""" Using the above information, generate an outline for a research report in Markdown syntax'\
#            f' for the following question or topic: "{question}". The outline should provide a well-structured framework'\
#            ' for the research report, including the main sections, subsections, and key points to be covered.' \
#            ' The research report should be detailed, informative, in-depth, and a minimum of 1,200 words.' \
#            ' Use appropriate Markdown syntax to format the outline and ensure readability.'

def generate_concepts_prompt(question, research_summary):
    """ Generates the concepts prompt for the given question.
    Args: question (str): The question to generate the concepts prompt for
            research_summary (str): The research summary to generate the concepts prompt for
    Returns: str: The concepts prompt for the given question
    """

    return f'"""{research_summary}""" Using the above information, generate a list of 5 main concepts to learn for a research report'\
           f' on the following question or topic: "{question}". The outline should provide a well-structured framework'\
           'You must respond with a list of strings in the following format: ["concepts 1", "concepts 2", "concepts 3", "concepts 4, concepts 5"]'


def generate_lesson_prompt(concept):
    """
    Generates the lesson prompt for the given question.
    Args:
        concept (str): The concept to generate the lesson prompt for.
    Returns:
        str: The lesson prompt for the given concept.
    """

    prompt = f'generate a comprehensive lesson about {concept} in Markdown syntax. This should include the definition'\
    f'of {concept}, its historical background and development, its applications or uses in different'\
    f'fields, and notable events or facts related to {concept}.'

    return prompt

def get_report_by_type(report_type):
    report_type_mapping = {
        'research_report': generate_report_prompt,
        # 'resource_report': generate_resource_report_prompt,
        # 'outline_report': generate_outline_report_prompt
    }
    return report_type_mapping[report_type]

# def auto_agent_instructions():
#     return """
#         This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer. The research is conducted by a specific agent, defined by its type and role, with each agent requiring distinct instructions.
#         Agent
#         The agent is determined by the field of the topic and the specific name of the agent that could be utilized to research the topic provided. Agents are categorized by their area of expertise, and each agent type is associated with a corresponding emoji.

#         examples:
#         task: "should I invest in apple stocks?"
#         response: 
#         {
#             "agent": "💰 Finance Agent",
#             "agent_role_prompt: "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends."
#         }
#         task: "could reselling sneakers become profitable?"
#         response: 
#         { 
#             "agent":  "📈 Business Analyst Agent",
#             "agent_role_prompt": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis."
#         }
#         task: "what are the most interesting sites in Tel Aviv?"
#         response:
#         {
#             "agent:  "🌍 Travel Agent",
#             "agent_role_prompt": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights."
#         }
#     """

def auto_agent_instructions():
    return """
        This task involves researching a given company name, regardless of its complexity or the availability of a definitive answer. The research is conducted by a lead generation agent, defined by its type and role, with the agent requiring specific instructions.
        Agent
        The agent will always be a web-scrapping and lead generation agent that will be given a company name and the company's location of operation. The agent will search in depth about the company on internet and get the company details.

        examples:
        Company: "Apple"
        Location: "United States"
        response: 
        { 
            "agent":  "📈 Lead Generation Agent",
            "agent_role_prompt": "You are an experienced AI business analyst and lead generation assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis."
        }
    """
