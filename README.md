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
   cd bandgap-calculation```
2. Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
