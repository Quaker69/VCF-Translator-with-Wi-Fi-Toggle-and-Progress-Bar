# VCF Translator with Wi-Fi Toggle and Progress Bar

This repository provides a Python script to process and translate VCF (vCard) files. It supports translating names in the VCF file from English to Kannada and handles Wi-Fi toggling in case of network failures during translation. A progress bar is also included to track the processing status.

## Features
- **Translate Names:** Translates names from English to Kannada using the Google Translate API.
- **Wi-Fi Toggle Mechanism:** Automatically toggles Wi-Fi if translation fails due to network issues.
- **Progress Bar:** Displays a progress bar for monitoring the translation process.
- **Cross-Platform Wi-Fi Support:** Supports Wi-Fi toggling on Windows, Linux, and macOS.

## Requirements
- Python 3.7 or later
- Required Libraries:
  - `googletrans==4.0.0-rc1`
  - `tqdm`

Install the required libraries using:
```bash
pip install googletrans==4.0.0-rc1 tqdm
```

## Usage
### 1. Prepare Input VCF File
Place your input VCF file (vCard format) in the desired directory.

### 2. Update File Paths
Edit the following lines in the script to specify the input and output file paths:
```python
input_vcf_path = 'in_put_file_path.vcf'
output_vcf_path = 'out_put_file_path.vcf'
```
Replace `'in_put_file_path.vcf'` and `'out_put_file_path.vcf'` with actual file paths.

### 3. Run the Script
Execute the script using the command:
```bash
python script_name.py
```
Replace `script_name.py` with the filename of your script.

### 4. Output
The modified VCF file with translated names will be saved at the specified output path.

## Functions Overview
### 1. `translate_to_kannada_with_wifi_toggle`
- Translates text to Kannada with retries and toggles Wi-Fi in case of failures.

### 2. `toggle_wifi`
- Toggles Wi-Fi connection based on the operating system.

### 3. `modify_vcf_with_progress_and_wifi`
- Reads the input VCF file, processes each line, translates relevant fields, and writes to the output VCF file while showing a progress bar.

## Notes
- Ensure you have an active internet connection for translations.
- Wi-Fi toggling is platform-specific and may not work on unsupported operating systems.
- Backup your VCF file before processing it with this script.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## Contact
For any issues or suggestions, please create an issue in this repository.

