import streamlit as st
import pandas as pd

# -------------------------
# Sample Data (10 leads)
# -------------------------
data = [
    {"Name": "Dr. Alice Smith", "Title": "Director of Toxicology", "Company": "BioTechX",
     "Location": "Cambridge, MA", "HQ": "Cambridge, MA", "Email": "alice.smith@biotechx.com",
     "RoleFit": 30, "CompanyIntent": 20, "Technographic": 25, "LocationScore": 10, "ScientificIntent": 40},

    {"Name": "Dr. Bob Johnson", "Title": "Junior Scientist", "Company": "StartUpLabs",
     "Location": "Remote, TX", "HQ": "Boston, MA", "Email": "bob.johnson@startuplabs.com",
     "RoleFit": 10, "CompanyIntent": 0, "Technographic": 5, "LocationScore": 5, "ScientificIntent": 0},

    {"Name": "Dr. Carol Lee", "Title": "Head of Preclinical Safety", "Company": "HepaTech",
     "Location": "Boston, MA", "HQ": "Boston, MA", "Email": "carol.lee@hepatech.com",
     "RoleFit": 30, "CompanyIntent": 20, "Technographic": 25, "LocationScore": 10, "ScientificIntent": 40},

    {"Name": "Dr. David Kim", "Title": "VP Preclinical", "Company": "LiverTech",
     "Location": "San Francisco, CA", "HQ": "San Francisco, CA", "Email": "david.kim@livertech.com",
     "RoleFit": 30, "CompanyIntent": 20, "Technographic": 15, "LocationScore": 10, "ScientificIntent": 30},

    {"Name": "Dr. Emily Zhang", "Title": "Research Scientist", "Company": "ToxBio",
     "Location": "Remote, MA", "HQ": "Boston, MA", "Email": "emily.zhang@toxbio.com",
     "RoleFit": 15, "CompanyIntent": 10, "Technographic": 10, "LocationScore": 5, "ScientificIntent": 20},

    {"Name": "Dr. Frank Rivera", "Title": "Director of Safety Assessment", "Company": "HepaCore",
     "Location": "Basel, Switzerland", "HQ": "Basel, Switzerland", "Email": "frank.rivera@hepacore.com",
     "RoleFit": 30, "CompanyIntent": 25, "Technographic": 20, "LocationScore": 10, "ScientificIntent": 35},

    {"Name": "Dr. Grace Patel", "Title": "Senior Scientist", "Company": "LiverWorks",
     "Location": "Boston, MA", "HQ": "Boston, MA", "Email": "grace.patel@liverworks.com",
     "RoleFit": 25, "CompanyIntent": 20, "Technographic": 15, "LocationScore": 10, "ScientificIntent": 30},

    {"Name": "Dr. Henry White", "Title": "Toxicology Manager", "Company": "BioLiver",
     "Location": "Remote, CA", "HQ": "San Francisco, CA", "Email": "henry.white@bioliver.com",
     "RoleFit": 20, "CompanyIntent": 15, "Technographic": 10, "LocationScore": 5, "ScientificIntent": 25},

    {"Name": "Dr. Irene Gomez", "Title": "Head of Drug Safety", "Company": "HepaLabs",
     "Location": "Boston, MA", "HQ": "Boston, MA", "Email": "irene.gomez@hepalabs.com",
     "RoleFit": 30, "CompanyIntent": 20, "Technographic": 20, "LocationScore": 10, "ScientificIntent": 40},

    {"Name": "Dr. Jack Liu", "Title": "Preclinical Scientist", "Company": "ToxSolutions",
     "Location": "Remote, NY", "HQ": "Boston, MA", "Email": "jack.liu@toxs.com",
     "RoleFit": 15, "CompanyIntent": 10, "Technographic": 10, "LocationScore": 5, "ScientificIntent": 20},
]

df = pd.DataFrame(data)

# -------------------------
# Compute Score and Work Mode
# -------------------------
df['ProbabilityScore'] = df['RoleFit'] + df['CompanyIntent'] + df['Technographic'] + df['LocationScore'] + df['ScientificIntent']
df = df.sort_values(by='ProbabilityScore', ascending=False)
df['Rank'] = range(1, len(df) + 1)
df['WorkMode'] = df.apply(lambda x: 'Remote' if x['Location'] != x['HQ'] else 'Onsite', axis=1)

# -------------------------
# Columns to Display
# -------------------------
display_df = df[['Rank', 'ProbabilityScore', 'Name', 'Company', 'Location', 'HQ', 'WorkMode', 'Email']]

# -------------------------
# Streamlit Layout
# -------------------------
st.set_page_config(page_title="3D In-Vitro Lead Dashboard", layout="wide")

# Colorful Title
st.markdown("<h1 style='text-align: center; color: #FF5733;'>3D In-Vitro Lead Dashboard 🧬</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #2E86C1;'>Find, rank, and prioritize top potential collaborators!</p>", unsafe_allow_html=True)

# Use GitHub raw images (fully reliable)
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image("https://raw.githubusercontent.com/addycuber/sample-images/main/3d_cell_culture.jpg", caption="3D Cell Culture")
with col2:
    st.image("https://raw.githubusercontent.com/addycuber/sample-images/main/lab_research.jpg", caption="Lab Research")
with col3:
    st.image("https://raw.githubusercontent.com/addycuber/sample-images/main/liver_cells.jpg", caption="Toxicology")

# Colorful divider
st.markdown("<hr style='border:3px solid #FF5733'>", unsafe_allow_html=True)

# Table
st.markdown("### 📝 Leads Overview")
st.dataframe(display_df, height=400)

# CSV Download
csv = display_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Leads CSV",
    data=csv,
    file_name='leads_dashboard.csv',
    mime='text/csv'
)
