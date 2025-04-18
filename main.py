import streamlit as st

st.set_page_config(page_title="Service Pricing Calculator", layout="centered")
st.title("📊 Monthly Cost Calculator")
st.markdown("Adjust the sliders below to estimate your monthly cost across services.")

st.divider()

# ------------------------------
# 📨 TWILIO (WhatsApp)
# ------------------------------
st.subheader("WhatsApp Configuration")
whatsapp_msgs = st.slider("Number of WhatsApp Messages (per month)", 0, 500_000, 10_000, step=1_000)
whatsapp_cost = whatsapp_msgs * 0.005  # $0.005 per message (Twilio fee)
st.write(f"**WhatsApp Cost (Twilio):** ${whatsapp_cost:,.2f}")

st.divider()

# ------------------------------
# 🗄️ SUPABASE (Storage & Compute)
# ------------------------------
st.subheader("Database Configuration")
supabase_storage = st.slider("Supabase Storage (in GB)", 0, 500, 5, step=5)
supabase_compute_hours = st.slider("Supabase Postgres Compute (hours/month)", 0, 744, 100)
supabase_storage_cost = supabase_storage * 0.25  # $0.25/GB
supabase_compute_cost = supabase_compute_hours * 0.10  # $0.10/hour
supabase_total = supabase_storage_cost + supabase_compute_cost
st.write(f"**Supabase Cost:** ${supabase_total:,.2f}")

st.divider()

# ------------------------------
# 🧠 GEMINI (LLM)
# ------------------------------
st.subheader("Gemini LLM Configuration")
model_choice = st.selectbox("Select Gemini Model", ["Flash", "Flash-Lite"])
tokens_million = st.slider("Tokens (in millions)", 0, 100, 1)

if model_choice == "Flash":
    gemini_input_cost = tokens_million * 0.10
    gemini_output_cost = tokens_million * 0.40
elif model_choice == "Flash-Lite":
    gemini_input_cost = tokens_million * 0.075
    gemini_output_cost = tokens_million * 0.30

gemini_cost = gemini_input_cost + gemini_output_cost
st.write(f"**Gemini Cost ({model_choice}):** ${gemini_cost:,.2f}")

st.divider()

# ------------------------------
# 📧 SENDGRID (Email API)
# ------------------------------
st.subheader("Email API Configuration")
emails_sent = st.slider("Emails Sent per Month", 0, 500_000, 10_000, step=1_000)
free_emails = 3_000
extra_emails = max(0, emails_sent - free_emails)
sendgrid_cost = extra_emails * 0.001  # $0.001/email after 3,000 free
tier_cost = 0
if emails_sent > 50_000:
    tier_cost = 89.95
elif emails_sent > 3_000:
    tier_cost = 19.95
st.write(f"**SendGrid Cost (incl. Tier):** ${(sendgrid_cost + tier_cost):,.2f}")

st.divider()

# ------------------------------
# 🖥️ RENDER (Backend Server)
# ------------------------------
st.subheader("Render Server Configuration")
render_ram = st.selectbox("RAM (GB)", [0.5, 1, 2, 4, 8, 16, 32], index=2)
render_cpu = st.selectbox("vCPU", [0.25, 0.5, 1, 2, 4], index=2)
render_hours = st.slider("Usage Hours per Month", 0, 744, 100)

# Pricing: $0.007 per vCPU-hour, $0.01 per GB RAM-hour
render_cost = (render_cpu * 0.007 + render_ram * 0.01) * render_hours
st.write(f"**Render Server Cost:** ${render_cost:,.2f}")

st.divider()

# ------------------------------
# 💰 TOTAL MONTHLY COST
# ------------------------------
total_cost = whatsapp_cost + supabase_total + gemini_cost + sendgrid_cost + tier_cost + render_cost
st.subheader(f"💰 Total Estimated Monthly Cost: ${total_cost:,.2f}")
