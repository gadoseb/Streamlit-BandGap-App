# Band Gap Calculation using Tauc Plot an

This web application allows users to calculate the band gap of semiconductors using reflectance data via the Tauc plot method. Additionally, the app integrates a **CrossRef-based literature search** to compare your calculated band gap with published values. The app is built with [Streamlit](https://streamlit.io/) and provides an interactive interface to upload data, visualize spectra, perform band gap calculations, and search the scientific literature.

[Link to the App](https://app-bandgap-app-lk2dpmuh369fge7zbuvqkh.streamlit.app/)

## Features

- **Data Upload**: Upload reflectance data in CSV, XLSX, or TXT format.
- **Reflectance Spectrum**: Visualize the reflectance spectrum of the uploaded data.
- **Absorbance Spectrum**: Calculate and display the absorbance spectrum using the inverse Kubelka-Munk transformation.
- **Tauc Plot**: Generate the Tauc plot for both direct and indirect transitions.
- **Band Gap Calculation**: Perform a linear fit on a selected range of the Tauc plot to calculate the band gap energy.
- **Data Export**: Export the calculated data (Tauc plot values, linear fit results, and estimated band gap) to CSV and TXT files.
- **CrossRef Literature Search**: Search scientific literature through CrossRef for publications related to your material and compare the extracted band gap values with your calculated result.

## Literature Search with CrossRef

The application includes a **literature search** feature using the [CrossRef API](https://www.crossref.org/services/metadata-delivery/rest-api/). With this feature, users can search for published scientific articles related to their material based on keywords, and retrieve relevant metadata such as:

- **Title of the publication**
- **DOI (Digital Object Identifier)** for direct access to the paper
- **Estimated band gap value** (if available from the abstract or full text)

### How it works:

1. **Enter Search Term**: Input the common name of the material (e.g., "Band gap semiconductor").
2. **Search for Publications**: The app queries CrossRef's API to retrieve the most relevant publications matching the search term.
3. **Extract Band Gap Value**: The app attempts to extract band gap values from the abstract or full text of the publication (using regex pattern matching).
4. **Compare with User's Band Gap**: The app compares the band gap you calculated with those extracted from the literature, helping you validate your result.

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
8. Use the literature search feature to find related publications and compare the calculated band gap with values from the literature.

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
- **Download**: Download CSV or TXT file of the calculated values

## CrossRef Literature Search Example
- **Search Query**: Enter the common name of the material (e.g., "semiconductor band gap").
- **Results**:
   1. Retrieve and display the titles, DOIs, and abstracts (if available).
   2. Extract band gap values from the text or abstract.

## Dependencies

The following Python packages are required:

- streamlit
- pandas
- numpy
- matplotlib
- scipy
- requests (for CrossRef API integration)
- BeautifulSoup (for web scraping if full text analysis is needed)

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
