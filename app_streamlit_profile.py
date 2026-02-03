
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Researcher Profile | FePt & DFT",
    layout="wide"
)

st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to",
    ["Profile", "Research", "Publications", "Contact"]
)

if menu == "Profile":
    st.title("Mashilo Matlala")
    st.subheader("University of Limpopo student")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "https://cdn.pixabay.com/photo/2017/08/30/01/05/atoms-2694069_1280.jpg",
            caption="Computational Materials Science",
            use_column_width=True
        )
    with col2:
        st.markdown(
            '''
            **Research Focus:**  
            Density Functional Theory (DFT) simulations of FePt-based alloys  
            
            **Specialisation:**  
            • Magnetic properties of L1₀ FePt alloys  
            • Elastic and thermodynamic properties  
            • Phonon and vibrational stability analysis  
            
            **Tools & Methods:**  
            VASP, GGA-PBE, PHONON, MedeA, Python, Streamlit
            '''
        )

elif menu == "Research":
    st.title("Current Research")
    st.markdown(
        '''
        My research focuses on **binary and ternary FePt-based alloys** investigated
        using **first-principles Density Functional Theory (DFT)** calculations.
        
        ### Key Research Areas
        - Magnetic moments and stability of Fe₅₀Pt₅₀₋ₓMₓ alloys  
        - Elastic moduli (Bulk, Shear, Young’s modulus)  
        - Phonon dispersion and vibrational stability  
        - Alloying effects of Ag, Cu, and B  
        '''
    )

    data = pd.DataFrame({
        "Alloy": ["Fe50Pt50", "Fe50Pt43.75Ag6.25", "Fe50Pt43.75Cu6.25"],
        "Bulk Modulus (GPa)": [204.7, 211.7, 198.3],
        "Shear Modulus (GPa)": [95.1, 107.2, 92.6]
    })

    st.subheader("Sample Computational Results")
    st.dataframe(data)

elif menu == "Publications":
    st.title("Publications")

    publications = pd.DataFrame({
        "Year": [2024, 2025],
        "Title": [
            "First-principles study of FePt-based ternary alloys",
            "Elastic and vibrational properties of L1₀ FePt alloys"
        ],
        "Type": ["Journal Article", "Conference Paper"]
    })

    st.dataframe(publications)

elif menu == "Contact":
    st.title("Contact")
    st.markdown(
        '''
        **Email:** matlalamashilo01@gmail.com  
        **Field:** Computational Materials Science  
        **Focus:** DFT, Magnetic Materials, Alloy Design  
        '''
    )

st.sidebar.markdown("---")
st.sidebar.caption("Streamlit Research Profile | CSS 2026")
