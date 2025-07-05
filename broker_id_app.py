import streamlit as st

def calculate_broker_id(total_production, liberty_percentage, attitude):
    # Convert total production to a format like 8.8 (in hundred thousands)
    production_code = total_production / 100000
    # Format the Broker I.D. as per example: P production/percentage/attitude
    return f"P {production_code:.1f}/{liberty_percentage}/{attitude}"

def main():
    st.title("Broker I.D. Generator")
    
    # Input for total production
    total_production = st.number_input(
        "Enter total production across all companies (in Rands)",
        min_value=0.0,
        step=1000.0,
        format="%.2f"
    )
    
    # Input for Liberty percentage
    liberty_percentage = st.number_input(
        "Enter percentage of business Liberty receives",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
        format="%.1f"
    )
    
    # Input for attitude
    attitude = st.selectbox(
        "Select broker's attitude towards Liberty",
        options=["+", "0", "-"],
        help="Positive (+), Neutral (0), or Negative (-)"
    )
    
    # Button to generate Broker I.D.
    if st.button("Generate Broker I.D."):
        if total_production > 0 and liberty_percentage >= 0:
            broker_id = calculate_broker_id(total_production, liberty_percentage, attitude)
            st.success(f"Broker I.D.: **{broker_id}**")
        else:
            st.error("Please ensure total production is positive and percentage is valid.")

if __name__ == "__main__":
    main()