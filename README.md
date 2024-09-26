# Band Gap Calculation using Tauc Plot

This web application allows users to calculate the band gap of semiconductors using reflectance data via the Tauc plot method. The app is built with [Streamlit](https://streamlit.io/) and provides an interactive interface to upload data, visualise spectra, and perform band gap calculations.

[Link to the App](https://app-bandgap-app-sebastiano-gadolini.streamlit.app/)

## Features

- **Data Upload**: Upload reflectance data in CSV, XLSX, or TXT format.
- **Experiement Selection**: Transmittance or Reflectance data. Direct or Indirect Band Gap calculation
- **Wavelength Range Slider**: Select the wavelength range for calculations and plots.
- **Transmittance Spectrum**: Visualize or calculate the transmittance spectrum of the uploaded data.
- **Reflectance Spectrum**: Visualize or calculate the reflectance spectrum of the uploaded data.
- **Absorbance Spectrum**: Calculate and display the absorbance spectrum using the inverse Kubelka-Munk transformation.
- **Tauc Plot**: Generate the Tauc plot for direct and indirect transitions.
- **Band Gap Calculation**: Perform a linear fit on a selected range of the Tauc plot to calculate the band gap energy.
- **Data Export**: Export the calculated data (Tauc plot values, linear fit results, and estimated band gap) to CSV file.
- **Automatic Linear Region Detector [Beta]**: Estimate band gap automatically and display fit quality metrics.
- **Quick and Dirty Literature Review [Beta]**: Perform a literature review about the material under investigation. The band gap is shown only for open-source journals with a webpage view.

## Demo

https://github.com/user-attachments/assets/78809a60-4fe8-4ff5-beb9-fbbc0c6cd6ae

## Usage

1. Launch the Streamlit app.
2. Upload your data in CSV, XLSX, or TXT format.
4. Select the columns representing wavelength and signal.
5. Select the data range to be used.
6. Visualize the spectra.
7. Generate the Tauc Plot and select the range for the linear fit.
8. The band gap energy is calculated and displayed on the screen.
9. Export the results as CSV.

## File Formats

The app supports the following file formats for data upload:

- **CSV**: Comma-separated values.
- **XLSX**: Microsoft Excel files.
- **TXT**: Tab-delimited text files.

## Exported Data

The data exported in CSV formats include the following:

- Wavelength (nm)
- Reflectance
- Absorbance
- Transmittance
- Photon Energy (eV)
- Tauc Plot Values
- Fitted Photon Energy (eV) for the linear fit
- Fitted Tauc Plot Values for the linear fit
- Estimated Band Gap (eV)

## Example

- **Upload Data**: Upload a CSV file with columns for wavelength (in nm) and reflectance.
- **Visualization**: The app will display reflectance, absorbance spectra, and Tauc plot.
- **Calculation**: A linear fit will be performed in the selected region of the Tauc plot to estimate the band gap.
- **Download**: Download CSV file of the calculated values.
- **Quick and Dirty Literature Review**: Perform a quick literature review on your material without changing the webpage!

## Dependencies

The following Python packages are required:

- streamlit==1.38.0
- pandas>=1.3.0
- numpy>=1.21.0
- matplotlib>=3.4.0
- scipy>=1.7.0
- requests>=2.26.0
- beautifulsoup4>=4.10.0
- openpyxl

## How Tauc Plot works

The Tauc plot is used to estimate the optical band gap energy of semiconductors. It is based on the following equation for direct transitions:

$$
(\alpha h \nu)^2 = A(h \nu - E_g)
$$

Where:
- \( \alpha \) is the absorption coefficient (approximated using Kubelka-Munk function).
- \( h \nu \) is the photon energy (in electron volts, eV).
- \( E_g \) is the band gap energy.
- \( A \) is a constant.

For indirect transitions, the equation becomes:

$$
(\alpha h \nu)^{1/2} = A(h \nu - E_g)
$$

The linear region of the Tauc plot is used to extrapolate the band gap.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/bandgap-calculation.git
   cd bandgap-calculation
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run bandgap.py
