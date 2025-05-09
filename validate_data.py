# validate_data.py

import os

REQUIRED_FILES = [
    "supply_chain_risks.txt",
    "nist_supply_chain_guidance.txt",
    "mitre_system_of_trust.txt",
    "intel_supply_chain_protections.txt",
    "microsoft_silk_typhoon_case.txt"
]

def validate_data_dir():
    for file in REQUIRED_FILES:
        path = os.path.join("data", file)
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ Missing file: {path}")
        if os.path.getsize(path) == 0:
            raise ValueError(f"⚠️ File is empty: {path}")
        print(f"✅ Found: {path}")

if __name__ == "__main__":
    validate_data_dir()
