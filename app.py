import streamlit as st
from PIL import Image

st.set_page_config(page_title="My resume", page_icon=":tada:", layout="wide")

with st.container():
    left_col, right_col = st.columns(2)
    st.write("---")
    with left_col:
        st.write("Pooja Pootula")
    with right_col:
        st.write("Contact details: +91-9705518077")
        st.write("Email: poojapootula@gmail.com")
    st.subheader("Summary")
    st.write("- I am working as Senior Project Engineer for 'Wipro Technologies' from July 2015 to date.")
    st.write("- Worked as Module lead handling two applications and as a Unix shell scripts developer automating "
              "the LOA and upgrade activities of technical teams. Designing Websites using Python")
    st.write("- Good exposure to designing and understanding requirements, coding, testing, and implementation "
              "support.")
    st.write("- Good collaborator and ability to learn new skills quickly and flexible to work on various "
              "technologies.")
    st.write("- To work in a competitive environment that effectively utilizes my analytical, interpersonal, "
              "leadership, and organizational skills to conceive and achieve solutions. The solutions that help "
             "the organization in not only meeting its targets, but also allowing it to grow, thereby, enhancing my "
             "own skills as an individual and as a key player in the organization's development.")

with st.container():
    st.subheader("Professional Snapshot")
    st.write("Since Aug 2016, have around 5 years as a module lead handling two application with six members team, "
             "1 year of extensive direct experience of designing, developing and deploying shell scripts in Solaris"
             " platform. An experienced collaborator with excellent communication and people skills who can work "
             "independently under pressure, can lead, motivate, and influence others and can train and mentor subordinates.")
    st.write("- Knowledge in Unix Shell Scripting, SQL Queries.")
    st.write("- Knowledge in creating websites in Python (flask, streamlit).")
    st.write("- Knowledge in Remedy and ServiceNow tools.")
    st.write("- Good Exposure and working knowledge with Incident management Change management and release management.")
    st.write("- Possess strong problem analysis skills with the ability to follow project standards.")
    st.write("- Have Good Knowledge of writing test cases.")
    st.write("- Front end to the clients in giving updates and providing innovative ideas.")
    st.write("- Ability to work in-group as well as independently with minimal supervision.")
    st.write("- Good analytical thinker that consistently resolves ongoing issues or defects")

with st.container():
    st.subheader("Education details")
    st.write("- Master’s degree from Birla Institute of Technology & Science (BITS), Pilani in 2019")

with st.container():
    st.subheader("Engagement overview")
    st.markdown("**Project: British Petroleum ISP Operations – Sales Accounting Monitoring**")
    st.write("Company: BP")
    st.write("Technologies Used: Unix Shell Scripting, SQL")
    st.write("Role: Developer/ Team Lead")
    st.caption("Description:")
    st.write("Sales accounting processes the transactions and creates invoice lines. It calculates exchange rate, prices, taxes for each invoice product."
             "Sales accounting job esin001V and IOP batches are the main programs running in the month end streams.We have automated the monitoring and "
             "sending the status report of these streams for every 2hrs during the initial five days of the month.This is overly critical period for "
             "the business as all the transactions are closed.")
    st.caption("Responsibilities:")
    st.write("- Analyzing the application from end to end.")
    st.write("- Providing diverse options to businesses and suggesting the best option that saves the cost and gives high availability for the "
             "application.")
    st.write("- Removing the dependencies and providing alternative solutions.")
    st.write("- Creating new programs in the application by adding extra features.")
    st.write("- Knowledge transfer to the support team providing the design documents and developing the test cases.")
    st.caption("Achievements:")
    st.write("After successfully implementing this automation the manual time of monitoring the streams has reduced helping the team in "
             "focusing on other important aspects for the day. As the process is automated there were no errors in the report be it the calculation, "
             "timing of the report, mismatch of country/database.")

    st.divider()

    st.markdown("**Project: British Petroleum ISP Operations – Month End Streams Monitoring**")
    st.write("Company: BP")
    st.write("Technologies Used: Unix Shell Scripting, SQL")
    st.write("Role: Developer/ Team Lead")
    st.caption("Description:")
    st.write("Month End streams are nothing but the special sales accounting streams that processes the transactions and creates invoice lines for "
             "the entire month, which helps in account closure. Every country has their own sales accounting job based on the region differentiated using "
             "the database numbers. These jobs produce the invoices by checking the planned invoice date of those transactions. I have automated the "
             "monitoring and sending the status report of these streams for every 2hrs during the initial five days of the month. This process starts "
             "a day before the stream run date and ends after the stream run date, making sure the business is up to date with the stream status "
             "(Waiting, running, error, completed) This is overly critical period for the business as all the transactions are closed.")
    st.caption("Responsibilities:")
    st.write("- Analyzing the application from end to end.")
    st.write("- Providing diverse options to businesses and suggesting the best option that saves the cost and gives high availability for the "
        "application.")
    st.write("- Removing the dependencies and providing alternative solutions.")
    st.write("- Creating new programs in the application by adding extra features.")
    st.write("Knowledge transfer to the support team providing the design documents and developing the test cases.")
    st.caption("Achievements:")
    st.write("After successfully implementing this automation the manual time of monitoring the streams has reduced helping the team in "
        "focusing on other important aspects for the day. As the process is automated there were no errors in the report be it the calculation, "
        "timing of the report, mismatch of country/database.")

    st.divider()

    st.markdown("**Project: British Petroleum ISP UOA Automation**")
    st.write("Company: BP")
    st.write("Technologies Used: Unix Shell Scripting, SQL")
    st.write("Role: Developer/ Team Lead")
    st.caption("Description:")
    st.write("Used oil analysis (UOA) is a process where the team receive files with transactional data. Flat file and data file belonging to operations"
             " and marketing team respectively, is loaded into the system. Once the data is loaded and an updated file is created, it must be sent "
             "to a specific mail ID provided. I have automated this process of loading the files into the system by copying them into the "
             "required directories. I have also made sure that the entire process monitored by triggering the e-mail for every step.")
    st.caption("Responsibilities:")
    st.write("- Analyzing the application from end to end.")
    st.write("- Providing diverse options to businesses and suggesting the best option that saves the cost and gives high availability for the "
        "application.")
    st.write("- Removing the dependencies and providing alternative solutions.")
    st.write("- Analyzing the scripts and rewriting them to fit in SQL without any compatibility issues.")
    st.write("- Creating the Test cases and performing the Unit testing of all the jobs end to end")
    st.write("- Updating business from time to time on the execution plan.")
    st.write("- Adhere to standards and procedures")
    st.caption("Achievements:")
    st.write("With this automation, we have removed the manual intervention in loading the files, saving approximately 10hrs of manual effort, "
             "for business. Removed the dependency on support team for loading and sending the report. Able to transform the process smoothly even"
             " after removing the dependencies of manual work.")

    st.divider()

    st.markdown("**Project: British Petroleum ISP OPSCOE**")
    st.write("Company: BP")
    st.write("Technologies Used: Unix Shell Scripting, SQL")
    st.write("Role: Module Lead/Support Analyst/Developer")
    st.caption("Responsibilities:")
    st.write("- Single handedly managing DBA team application and technical data flow by performing the LOA activities.")
    st.write("- Monitoring Interfaces that interact with applications daily.")
    st.write("- Resolving Interface failure issues.")
    st.write("- Review all deliverables and ensure defect-free delivery to the business.")
    st.write("- Collaborated with clients and delivered quarterly and monthly releases without failure.")
    st.write("- Know remedy and ServiceNow ticketing tools.")
    st.write("- Actively participated in P1 and P2 to resolve the issues and providing the RCA to the Clients.")
    st.write("- Adhere to standards and procedures.")
    st.write("- Gathering the requirements from Clients, analyzing them to make the workflow more efficient.")
    st.write("- Actively participated in Disaster Recovery plans.")
    st.write("- Worked as a single point of contact for the team DBAs, interacting with users and the vendor in solving the issues and updating the"
              " clients in catchup calls.")
    st.write("- Created change management and problem management requests to keep track of the application changes and fixes.")

    st.divider()
    st.markdown("**Certifications:**")
    st.write("- Azure Fundamentals (AZ-900)")
    st.write("- Azure Administrator (AZ-104)")

    st.markdown("**Rewards:**")
    st.write("- Inspiring Performance Badge")
    st.write("- Victory Badge")
    st.write("- Applause Badge")
    st.write("- Creativity & Innovation Badge")
    st.write("- Pleasure to work with you Badge")

    st.markdown("**Personal Details:**")
    st.markdown("**Name** : Pooja Pootula")
    st.markdown("**Marital Status** : Married")
    st.markdown("**Date of Birth** : 06th July 1994")
    st.markdown("**Languages Known** : English, Telugu and Hindi")
    st.markdown("**State** : Telangana")

    st.markdown("**Declaration:**")
    st.write("I hereby declare that the above information is true to the best of my knowledge and belief.")

    with st.container():
        right_column, left_column = st.columns(2)
    with left_column:
        st.write("Pooja Pootula")
    with right_column:
        st.write("Date:")

