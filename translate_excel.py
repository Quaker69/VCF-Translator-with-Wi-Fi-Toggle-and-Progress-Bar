import os
import platform
from googletrans import Translator
from time import sleep
from tqdm import tqdm

# Function to translate text from English to Kannada with retry and Wi-Fi toggle mechanism
def translate_to_kannada_with_wifi_toggle(text, retries=3):
    translator = Translator()
    attempt = 0
    while attempt < retries:
        try:
            return translator.translate(text, src='en', dest='kn').text
        except Exception as e:
            print(f"Translation failed: {e}. Retrying...")
            toggle_wifi()  # Toggle Wi-Fi on failure
            sleep(2)  # Wait 2 seconds before retrying
            attempt += 1
    print(f"Failed to translate: {text}. Returning original text.")
    return text  # Return original text if translation fails

# Function to toggle Wi-Fi (platform-specific)
def toggle_wifi():
    system = platform.system()
    if system == "Windows":
        os.system("netsh interface set interface name=\"Wi-Fi\" admin=disable")
        sleep(1)
        os.system("netsh interface set interface name=\"Wi-Fi\" admin=enable")
    elif system == "Linux":
        os.system("nmcli radio wifi off")
        sleep(1)
        os.system("nmcli radio wifi on")
    elif system == "Darwin":  # macOS
        os.system("networksetup -setairportpower airport off")
        sleep(1)
        os.system("networksetup -setairportpower airport on")
    else:
        print("Wi-Fi toggle not supported on this operating system.")

# Function to modify VCF fields for version 2.1 with progress bar
def modify_vcf_with_progress_and_wifi(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    output_lines = []
    with tqdm(total=len(lines), desc="Processing VCF", unit="lines") as pbar:
        for line in lines:
            if line.startswith("N:"):
                parts = line[2:].strip().split(";")
                parts = [translate_to_kannada_with_wifi_toggle(part) for part in parts if part]
                line = f"N:{';'.join(parts)}\n"
            elif line.startswith("FN:"):
                name = line[3:].strip()
                name = translate_to_kannada_with_wifi_toggle(name)
                line = f"FN:{name}\n"
            output_lines.append(line)
            pbar.update(1)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(output_lines)

# Input and output file paths
input_vcf_path = 'in_put_file_path.vcf' # enter your input file path
output_vcf_path = 'out_put_file_path.vcf' # enter your output file path

# Run the process
try:
    modify_vcf_with_progress_and_wifi(input_vcf_path, output_vcf_path)
    print(f"Modified VCF (version 2.1) saved to {output_vcf_path}")
except Exception as e:
    print(f"An error occurred: {e}")
