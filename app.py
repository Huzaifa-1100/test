import streamlit as st
from cryptography.fernet import Fernet
import hashlib
import json
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Secure Data System",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }
    .css-1d391kg {
        padding: 1rem;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stTextArea>div>div>textarea {
        border-radius: 5px;
    }
    .stSelectbox>div>div>select {
        border-radius: 5px;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #cce5ff;
        color: #004085;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Constants
MAX_LOGIN_ATTEMPTS = 3
STORAGE_FILE = "secure_data.json"

# Initialize storage
def load_stored_data():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_stored_data(data):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(data, f)

# Load stored data
stored_data = load_stored_data()

# Function to hash a passkey using SHA-256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to generate a Fernet key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt text using Fernet
def encrypt_text(text, key):
    try:
        fernet = Fernet(key)
        return fernet.encrypt(text.encode()).decode()
    except Exception as e:
        st.error(f"Error encrypting data: {str(e)}")
        return None

# Function to decrypt text using Fernet
def decrypt_text(ciphertext, key):
    try:
        fernet = Fernet(key)
        return fernet.decrypt(ciphertext.encode()).decode()
    except Exception as e:
        st.error(f"Error decrypting data: {str(e)}")
        return None

# Function to clear session state
def clear_session_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# Function to handle logout
def handle_logout():
    clear_session_state()
    st.session_state.logged_in = False
    st.session_state.page = "login"
    st.session_state.login_attempts = 0
    st.session_state.username = None
    st.session_state.logout_confirmed = False

# Initialize session state variables
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"
if "username" not in st.session_state:
    st.session_state.username = None
if "logout_confirmed" not in st.session_state:
    st.session_state.logout_confirmed = False

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("🔒 Secure Data System")
    st.sidebar.markdown("---")
    
    if st.session_state.logged_in:
        st.sidebar.markdown(f"### 👤 {st.session_state.username}")
        st.sidebar.markdown("---")
        
        # Navigation menu with icons
        menu_items = {
            "🏠 Home": "home",
            "📝 Store New Data": "insert",
            "🔍 Retrieve Data": "retrieve"
        }
        
        for label, page in menu_items.items():
            if st.sidebar.button(label, use_container_width=True):
                st.session_state.page = page
                st.rerun()
        
        st.sidebar.markdown("---")
        
        # Logout button with confirmation
        if st.sidebar.button("🚪 Logout", use_container_width=True):
            st.session_state.logout_confirmed = True
            
        # Show confirmation dialog if logout was initiated
        if st.session_state.logout_confirmed:
            st.sidebar.markdown("### ⚠️ Confirm Logout")
            st.sidebar.markdown("Are you sure you want to logout?")
            col1, col2 = st.sidebar.columns(2)
            if col1.button("✅ Yes", use_container_width=True):
                handle_logout()
                st.rerun()
            if col2.button("❌ No", use_container_width=True):
                st.session_state.logout_confirmed = False
                st.rerun()
    else:
        st.sidebar.markdown("### 🔐 Login Required")
        st.sidebar.markdown("Please log in to access the system.")

# Login Page
def login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h1 style='text-align: center;'>🔒 Login</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Please log in to continue</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("👤 Username")
            password = st.text_input("🔑 Password", type="password")
            submit = st.form_submit_button("Login", use_container_width=True)
            
            if submit:
                if username == "admin" and password == "password":
                    st.session_state.logged_in = True
                    st.session_state.login_attempts = 0
                    st.session_state.page = "home"
                    st.session_state.username = username
                    st.session_state.logout_confirmed = False
                    st.success("✅ Logged in successfully!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password.")

# Home Page
def home_page():
    st.markdown("<h1 style='text-align: center;'>🛡️ Secure Data System</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>Welcome, {st.session_state.username}! 👋</h3>", unsafe_allow_html=True)
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class='metric-card'>
                <h2>📊 Total Entries</h2>
                <h1>{len(stored_data)}</h1>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        active_entries = sum(1 for data in stored_data.values() if not data.get("expired", False))
        st.markdown(f"""
            <div class='metric-card'>
                <h2>✅ Active Entries</h2>
                <h1>{active_entries}</h1>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        expired_entries = sum(1 for data in stored_data.values() if data.get("expired", False))
        st.markdown(f"""
            <div class='metric-card'>
                <h2>⏰ Expired Entries</h2>
                <h1>{expired_entries}</h1>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recent entries
    if stored_data:
        st.markdown("### 📝 Recent Entries")
        recent_entries = sorted(
            stored_data.items(),
            key=lambda x: x[1]["created_at"],
            reverse=True
        )[:5]
        
        for data_id, data in recent_entries:
            with st.expander(f"Entry: {data_id}"):
                st.markdown(f"**Created:** {datetime.fromisoformat(data['created_at']).strftime('%Y-%m-%d %H:%M:%S')}")
                st.markdown(f"**Created by:** {data['created_by']}")
    else:
        st.info("No data stored yet. Use the sidebar to store new data.")

# Insert Data Page
def insert_data_page():
    st.markdown("<h1 style='text-align: center;'>📝 Store New Data</h1>", unsafe_allow_html=True)
    
    with st.form("insert_data_form"):
        st.markdown("### Enter your data")
        user_text = st.text_area("📄 Text to encrypt", height=200)
        passkey = st.text_input("🔑 Encryption passkey", type="password")
        
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button("🔒 Encrypt & Store", use_container_width=True)
        
        if submit:
            if user_text and passkey:
                data_id = f"data_{int(datetime.now().timestamp())}"
                hashed_passkey = hash_passkey(passkey)
                encryption_key = generate_key()
                encrypted_text = encrypt_text(user_text, encryption_key)
                
                if encrypted_text is not None:
                    stored_data[data_id] = {
                        "encrypted_text": encrypted_text,
                        "passkey": hashed_passkey,
                        "encryption_key": encryption_key.decode(),
                        "created_at": datetime.now().isoformat(),
                        "created_by": st.session_state.username
                    }
                    
                    save_stored_data(stored_data)
                    st.success("✅ Data stored securely!")
                    st.session_state.page = "home"
                    st.rerun()
            else:
                st.error("❌ Please enter both text and a passkey.")

# Retrieve Data Page
def retrieve_data_page():
    st.markdown("<h1 style='text-align: center;'>🔍 Retrieve Data</h1>", unsafe_allow_html=True)
    
    if not stored_data:
        st.warning("No data available to retrieve.")
        return

    # Create a list of data entries with timestamps
    data_entries = []
    for data_id, data in stored_data.items():
        created_at = datetime.fromisoformat(data["created_at"]).strftime("%Y-%m-%d %H:%M:%S")
        data_entries.append((data_id, f"{data_id} (Created: {created_at})"))
    
    # Sort entries by creation time (newest first)
    data_entries.sort(key=lambda x: x[0], reverse=True)
    
    # Create a dictionary for the selectbox
    data_options = {display: data_id for data_id, display in data_entries}
    
    with st.form("retrieve_data_form"):
        st.markdown("### Select and decrypt your data")
        selected_display = st.selectbox("📦 Select stored data:", list(data_options.keys()))
        data_id = data_options[selected_display]
        
        passkey = st.text_input("🔑 Enter passkey:", type="password")
        
        submit = st.form_submit_button("🔓 Decrypt Data", use_container_width=True)
        
        if submit:
            if not passkey:
                st.error("❌ Please enter a passkey.")
                return
                
            hashed_passkey = hash_passkey(passkey)
            if stored_data[data_id]["passkey"] == hashed_passkey:
                try:
                    encryption_key = stored_data[data_id]["encryption_key"].encode()
                    encrypted_text = stored_data[data_id]["encrypted_text"]
                    
                    decrypted_text = decrypt_text(encrypted_text, encryption_key)
                    
                    if decrypted_text is not None:
                        st.success("✅ Data decrypted successfully!")
                        st.markdown("### Decrypted Data")
                        st.markdown(f"```\n{decrypted_text}\n```")
                        
                        st.markdown("### Metadata")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**Created:** {datetime.fromisoformat(stored_data[data_id]['created_at']).strftime('%Y-%m-%d %H:%M:%S')}")
                        with col2:
                            st.markdown(f"**Created by:** {stored_data[data_id]['created_by']}")
                except Exception as e:
                    st.error(f"❌ Error during decryption: {str(e)}")
            else:
                st.session_state.login_attempts += 1
                st.error(f"❌ Incorrect passkey! Attempts left: {MAX_LOGIN_ATTEMPTS - st.session_state.login_attempts}")
                if st.session_state.login_attempts >= MAX_LOGIN_ATTEMPTS:
                    handle_logout()
                    st.rerun()

# Main App Logic
def main():
    # Add sidebar navigation
    sidebar_navigation()

    # Check if the user is logged in
    if not st.session_state.logged_in:
        login_page()
    else:
        # Navigation between pages
        if st.session_state.page == "home":
            home_page()
        elif st.session_state.page == "insert":
            insert_data_page()
        elif st.session_state.page == "retrieve":
            retrieve_data_page()

# Run the app
if __name__ == "__main__":
    main()