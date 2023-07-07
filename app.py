import streamlit as st
import sys
import time
import subprocess

st.set_page_config(
    page_title='FinClear Streamlit App', # TODO Change name
    layout='centered',  # Can be wide
    initial_sidebar_state='auto',  # Best to have auto for mobile
    menu_items={
        'Report a bug': 'mailto:emlyn.evans@finclear.com.au', # TODO Change email/info
        'Get help': 'mailto:emlyn.evans@finclear.com.au',  # TODO Change email/info
        'About': 'https://finclear.com.au/' # TODO Change info
    }
)

# Import all private packages here at the start of the app boot.
# You must "Reboot App" if you add more dependencies

# Based on https://discuss.streamlit.io/t/pip-installing-from-github/21484/5
try:
    # TODO Change the name to the private package you want to install from GitHub
    import streamlit_template_private

# This block executes only on the first run when your package isn't installed
except ModuleNotFoundError as e:
    sleep_time = 10
    package_name = 'streamlit_template_private' # TODO Change package name
    github_username = 'FinClear-Data' # TODO Change GitHub name
    dependency_warning = st.warning(
        f"Installing dependencies, this takes {sleep_time} seconds."
    )

    subprocess.Popen([
        f"{sys.executable} -m pip install git+https://${{github_token}}@github.com/{github_username}/{package_name}.git"],
        shell=True)

    # Wait for subprocess to install package before running your actual code below
    time.sleep(sleep_time)

    # Remove the installing dependency warning
    dependency_warning.empty()

    # Relaod the app
    st.experimental_rerun()

# Run the app!
# TODO change the name to your private package
streamlit_template_private.run()
