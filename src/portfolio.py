import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Teresiah Njoki.
##### *Resume* 
''')

image = Image.open('Njoki.jpeg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Motivated and tech-savvy data expert with a knack for analysis. I'm enthusiastic about using data insights to tackle
intricate challenges. With a strong interest in Data Science, Machine Learning, Analytics, and Business Management.
Throughout my career, I've sharpened my communication skills and showcased my teamwork abilities for achieving
top-notch results
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" " target="_blank">Teresiah Njoki</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#conferences-and-seminars">Conferences and Seminars</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science**  (Data Science and Artificial Intelligence)  , *European Business University of Luxembourg*,Luxembourg',
'2022-Present')
st.markdown('''

''')

txt('**Bachelors of Economics**, *University of Nairobi*, Kenya',
'2013-2016')
st.markdown('''
- GPA: `Second class`
''')


#####################
st.markdown('''
## Work Experience
''')
txt('**AI Resident**, Apziva, Turkey-Remotely',
'06/2023-Present')
st.markdown('''
- Apziva empowers professionals by providing a unique platform for individuals to work on challenging real-world
projects and gain experience under the guidance of industry expert mentors.
- Working on designing and implementing machine learning models on various projects coming from organizations
from all around the world ranging from various fields of AI such as natural language processing, computer vision,
deep learning, and others.
''')

txt('**Trainee-intern**, IT, 4rivers GmbH, Germany',
'03/2023-06/2023')
st.markdown('''
- Provided technical support for software applications used by staff members.
- Gained experience in one-login app management, Identity Access Management, and One Identity Management.
''')

txt('**Admin and logistics Officer- Microfinance**, Microfinance Department, Mission of Hope International, Kenya',
'03/2019-12/2019')
st.markdown('''
- Developed response strategies to address clients' needs.
- Developed and implemented logistics systems to improve operational efficiency.
- Maintained a good data entry and filing system. Collaborated with internal and external teams to resolve issues
related to order fulfillment or shipment delays.
''')

txt('**Human Resource Assistant**,Missions of Hope International, Kenya',
'08/2017-02/2019')
st.markdown('''
- Maintained an effective, accurate and up to date Human Resource Information System (HRIS).
- Maintained an up-to-date database of employee profiles with their contact details, qualifications and
certifications.
- Provided administrative support to the HR team in processing payroll information and developed strategies to
improve the effectiveness of HR operations through process improvements and automation.
- Created detailed reports on company compliance with labor laws and regulations.
- Analyzed employee data to identify trends in staff retention and turnover.
''')

txt('**Administrative assistant-intern**, Microfinance Department, Missions of Hope International, Kenya',
'03/2017-07/2017')
st.markdown('''
- Prepared meeting agendas and took detailed minutes during meetings.
- Performed data entry duties accurately.
- Organized and maintained accurate filing systems for documents and records.
''')

txt('**Office clerk-Intern**, MUKI Sacco, Kenya',
'09/2015-12/2015')
st.markdown('''
- Verification of loan defaulters
- Petty cash vouching and posting transaction
- Verifying the authenticity of loans application form
- Preparing Excel spreadsheet reports and reconciliation
- Credit appraisals
- Filing and archiving
- Customer care desk
''')

#####################
st.markdown('''
''')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, ')
txt3('Data processing/wrangling', '`SQL`, `Hadoop`, `mongoDB`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn` ')
txt3('Deep Learning', '`TensorFlow` `pytoch`')
txt3('Web development', '`JavaScript`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Docker')


#####################
st.markdown('''
## Conferences and Seminars
''')
txt3('Model of Leadership ' ,'TYKE Society, 09/2021')

txt3('Servant Leadership', 'Missions of Hope International,  Nairobi, 09/2018')

txt3('Business Management', 'Missions of Hope, Nairobi, 07/2017')

txt3('Youth in sustainable development', 'University of Nairobi, Nairobi, 11/2016')

txt3('Christian student leadership summit', 'Nairobi, 07/2016 ')

txt3('Leadership training','Focus-Kenya, 03/2016' )



#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/teresiah-njoki')
txt2('GitHub', 'https://github.com/Wnjoki')
