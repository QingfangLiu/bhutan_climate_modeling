from huggingface_hub import login, create_repo, upload_folder

# --- 1) Login (only needed once per environment/session) ---
# Paste your token when prompted; it will be stored securely.
login()

# --- 2) Set repo info ---
REPO_ID = "qlk0610/bhutan-climate"  # change to your repo
IS_PRIVATE = False                   # now this repo is private but may change later

# --- 3) Upload the local folder ---
upload_folder(
    folder_path="../../data/HydroSHEDS",  # local folder you want to upload
    path_in_repo="HydroSHEDS",      # where it appears inside the HF repo
    repo_id=REPO_ID,
    repo_type="dataset",
    commit_message="Add HydroSHEDS data" # update commit message
)
