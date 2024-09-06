# Band Gap Calculation using Tauc Plot

This web application allows users to calculate the band gap of semiconductors using reflectance data via the Tauc plot method. The app is built with [Streamlit](https://streamlit.io/) and provides an interactive interface to upload data, visualize spectra, and perform band gap calculations.

## Features

- **Data Upload**: Upload reflectance data in CSV, XLSX, or TXT format.
- **Reflectance Spectrum**: Visualize the reflectance spectrum of the uploaded data.
- **Absorbance Spectrum**: Calculate and display the absorbance spectrum using the inverse Kubelka-Munk transformation.
- **Tauc Plot**: Generate the Tauc plot for both direct and indirect transitions.
- **Band Gap Calculation**: Perform a linear fit on a selected range of the Tauc plot to calculate the band gap energy.
- **Data Export**: Export the calculated data (Tauc plot values, linear fit results, and estimated band gap) to CSV and TXT files.

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

## Usage

1. Launch the Streamlit app.
2. Upload your reflectance data in CSV, XLSX, or TXT format.
3. Select the columns representing wavelength and reflectance.
4. Visualize the Reflectance and Absorbance spectra.
5. Generate the Tauc Plot and select the range for the linear fit.
6. The band gap energy is calculated and displayed on the screen.
7. Export the results as CSV or TXT files.

## File Formats

The app supports the following file formats for data upload:

- **CSV**: Comma-separated values.
- **XLSX**: Microsoft Excel files.
- **TXT**: Tab-delimited text files.

## Exported Data

The data exported in CSV and TXT formats include the following:

- Photon Energy (eV)
- Tauc Plot Values
- Fitted Photon Energy (eV) for the linear fit
- Fitted Tauc Plot Values for the linear fit
- Estimated Band Gap (eV)

## Example

- **Upload Data**: Upload a CSV file with columns for wavelength (in nm) and reflectance.
- **Visualization**: The app will display reflectance, absorbance spectra, and Tauc plot.
- **Calculation**: A linear fit will be performed in the selected region of the Tauc plot to estimate the band gap.

## Dependencies

The following Python packages are required:

- streamlit
- pandas
- numpy
- matplotlib
- scipy

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
