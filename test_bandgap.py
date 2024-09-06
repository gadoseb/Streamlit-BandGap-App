import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from io import StringIO

# Define the Tauc plot fitting function (for linear region)
def linear_fit(x, m, c):
    return m * x + c

# Kubelka-Munk function for reflectance data
def kubelka_munk(reflectance):
    return (1 - reflectance)**2 / (2 * reflectance)

# Inverse Kubelka-Munk function for calculating absorbance
def inverse_kubelka_munk(alpha):
    return 1 - np.sqrt(1 + 4 * alpha) / 2

# File loading function
def load_data(uploaded_file, file_type):
    if file_type == "csv":
        return pd.read_csv(uploaded_file)
    elif file_type == "xlsx":
        return pd.read_excel(uploaded_file)
    elif file_type == "txt":
        return pd.read_csv(uploaded_file, delimiter='\t')  # Assuming tab-delimited txt file

# Export data to CSV
def export_to_csv(wavelength, reflectance, absorbance, photon_energy, y, x_fit, y_fit, band_gap):
    df = pd.DataFrame({
        'Wavelength (nm)': wavelength,
        'Reflectance': reflectance,
        'Absorbance': absorbance,
        'Photon Energy (eV)': photon_energy,
        'Tauc Plot Value': y,
        'Fitted Photon Energy (eV)': np.concatenate([x_fit, np.full(len(photon_energy) - len(x_fit), np.nan)]),
        'Fitted Tauc Plot Value': np.concatenate([y_fit, np.full(len(photon_energy) - len(y_fit), np.nan)]),
        'Band Gap (eV)': [band_gap] * len(photon_energy)
    })
    csv = df.to_csv(index=False)
    return csv

# Export data to TXT
def export_to_txt(wavelength, reflectance, absorbance, photon_energy, y, x_fit, y_fit, band_gap):
    output = StringIO()
    output.write("Wavelength (nm),Reflectance,Absorbance,Photon Energy (eV),Tauc Plot Value,Fitted Photon Energy (eV),Fitted Tauc Plot Value,Band Gap (eV)\n")
    for i in range(len(photon_energy)):
        output.write(f"{wavelength[i]},{reflectance[i]},{absorbance[i]},{photon_energy[i]},{y[i]},{x_fit[i] if i < len(x_fit) else ''},{y_fit[i] if i < len(y_fit) else ''},{band_gap}\n")
    txt = output.getvalue()
    return txt

# Streamlit app starts here
def main():
    st.title("Band Gap Calculation using Tauc Plot")

    st.write("""
    This app allows you to upload reflectance data and calculate the band gap of a semiconductor using the Kubelk-Munk function and Tauc plot method.
    """)

    # File upload
    uploaded_file = st.file_uploader("Upload your data (CSV, XLSX, or TXT format)", type=["csv", "xlsx", "txt"])

    if uploaded_file is not None:
        # Detect the file type based on the extension
        file_type = uploaded_file.name.split('.')[-1].lower()

        # Load the data using the appropriate pandas function
        if file_type in ['csv', 'xlsx', 'txt']:
            data = load_data(uploaded_file, file_type)
        else:
            st.error("Unsupported file format. Please upload a CSV, XLSX, or TXT file.")
            return

        st.write("Data Preview:")
        st.write(data.head())

        # Let the user choose which columns to use for wavelength and reflectance
        column1 = st.selectbox("Select Column 1 (Wavelength in nm):", data.columns)
        column2 = st.selectbox("Select Column 2 (Reflectance):", data.columns)

        # Extract the selected columns
        wavelength = data[column1]
        reflectance = data[column2]

        # Apply Kubelka-Munk transformation to reflectance data
        alpha = kubelka_munk(reflectance)

        # Calculate absorbance using the inverse Kubelka-Munk function
        absorbance = inverse_kubelka_munk(alpha)

        # Convert Wavelength to photon energy (hν in eV)
        h = 4.135667696e-15  # Planck's constant in eV·s
        c = 3e8              # Speed of light in m/s
        photon_energy = (h * c) / (wavelength * 1e-9)  # Convert wavelength from nm to m

        # Tauc plot (direct or indirect transition)
        transition_type = st.selectbox("Select the type of electronic transition", ("Direct", "Indirect"))

        if transition_type == "Direct":
            y = (alpha * photon_energy)**2
        else:
            y = np.sqrt(alpha * photon_energy)

        # Plot Reflectance Spectrum
        st.write("Reflectance Spectrum:")
        fig, ax = plt.subplots()
        ax.plot(wavelength, reflectance, label='Reflectance')
        ax.set_xlabel('Wavelength')
        ax.set_ylabel('Reflectance')
        plt.legend()
        st.pyplot(fig)

        # Plot Absorbance Spectrum
        st.write("Absorbance Spectrum:")
        fig, ax = plt.subplots()
        ax.plot(wavelength, absorbance, label='Absorbance', color='orange')
        ax.set_xlabel('Wavelength')
        ax.set_ylabel('Absorbance')
        plt.legend()
        st.pyplot(fig)

        # Tauc Plot
        st.write("Tauc Plot:")
        fig, ax = plt.subplots()
        ax.plot(photon_energy, y, label=f'Tauc Plot ({transition_type})')
        ax.set_xlabel('Photon Energy (eV)')
        ax.set_ylabel(r'$(\alpha h\nu)^n$')
        plt.legend()
        st.pyplot(fig)

        # Linear region selection
        st.write("Select the energy range for the linear region fitting:")
        x_min = st.number_input("Minimum energy (eV):", min_value=float(photon_energy.min()), max_value=float(photon_energy.max()), value=float(photon_energy.min()))
        x_max = st.number_input("Maximum energy (eV):", min_value=float(photon_energy.min()), max_value=float(photon_energy.max()), value=float(photon_energy.max()))

        # Select the linear region data
        mask = (photon_energy >= x_min) & (photon_energy <= x_max)
        x_fit = photon_energy[mask]
        y_fit = y[mask]

        # Perform linear fit
        popt, _ = curve_fit(linear_fit, x_fit, y_fit)

        # Plot the linear fit
        st.write("Linear Fit on the Selected Region:")
        fig, ax = plt.subplots()
        ax.plot(photon_energy, y, label=f'Tauc Plot ({transition_type})')
        ax.plot(x_fit, linear_fit(x_fit, *popt), 'r--', label='Linear Fit')
        ax.set_xlabel('Photon Energy (eV)')
        ax.set_ylabel(r'$(\alpha h\nu)^n$')
        plt.legend()
        st.pyplot(fig)

        # Extrapolate to find band gap
        band_gap = -popt[1] / popt[0]
        st.write(f"Estimated Band Gap: {band_gap:.2f} eV")
        
        # Prepare data for export
        csv_data = export_to_csv(wavelength, reflectance, absorbance, photon_energy, y, x_fit, y_fit, band_gap)
        txt_data = export_to_txt(wavelength, reflectance, absorbance, photon_energy, y, x_fit, y_fit, band_gap)

        # Provide download links
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="band_gap_results.csv",
            mime="text/csv"
        )

        st.download_button(
            label="Download TXT",
            data=txt_data,
            file_name="band_gap_results.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()






