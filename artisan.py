import streamlit as st
import pandas as pd

# Function to filter artisans based on user's criteria
def filter_artisans(user_location, desired_skill, availability, scheduling_preference, artisan_location, df):
    # Filter the dataset based on the user's criteria
    filtered_data = df[(df['User_Location'] == user_location) &
                       (df['Skill_Type'] == desired_skill) &
                       (df['Availability'] == availability) &
                       (df['Artisan_Location'] == artisan_location)]

    # If scheduling preference is 'On-demand', additionally filter based on 'On-Demand' preference
    if scheduling_preference == 'On-demand':
        filtered_data = filtered_data[filtered_data['Scheduling_Preference'] == 'On-Demand']

    # Check if filtered_data is empty
    if filtered_data.empty:
        return pd.DataFrame(columns=['Artisan_Name'])  # Return empty DataFrame with only Artisan_Name column

    # Extract artisan details from the filtered dataset
    artisan_details = filtered_data[['Artisan_Name']].reset_index(drop=True)

    return artisan_details

# Main function to run the Streamlit app
def main():
    # Title and introduction
    st.title("Artisan Recommendation App")
    st.markdown(
        """
        This app recommends artisans based on user's criteria.
        """
    )

    # Create sidebar layout
    with st.sidebar:
        st.subheader("User Criteria")
        user_location = st.selectbox("User Location", [''] + ['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
                                                          'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina',
                                                          'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau',
                                                          'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'])
        desired_skill = st.selectbox("Desired Skill", [''] + ['Electrician', 'Plumber', 'Carpenter', 'Painter', 'Tiler', 'Welder', 'Mechanic', 'Tailor',
                                                           'Hairdresser', 'Caterer', 'Graphic Designer', 'Photographer', 'Event Planner', 'Gardener',
                                                           'Interior Decorator', 'Furniture Maker', 'Shoe Cobbler', 'Barber', 'Makeup Artist', 'Dressmaker'])
        availability = st.selectbox("Availability", [''] + ["Available", "Not Available"])
        scheduling_preference = st.selectbox("Scheduling Preference", [''] + ["Advance", "On-demand"])
        artisan_location = st.selectbox("Artisan Location", [''] + ['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River',
                                                                 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina',
                                                                 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau',
                                                                 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'])

    # Check if all criteria are selected
    if user_location != '' and desired_skill != '' and availability != '' and scheduling_preference != '' and artisan_location != '':
        # Load the dataset
        df = pd.read_csv("Main_Artisan_data.csv")  # Replace "Main_Artisan_data.csv" with your dataset filename

        # Filter artisans based on user input
        artisan_details = filter_artisans(user_location, desired_skill, availability, scheduling_preference, artisan_location, df)

        # Display recommended artisans
        st.subheader("Recommended Artisans")
        if artisan_details.empty:
            st.write("No artisans found matching the criteria.")
        else:
            for index, row in artisan_details.iterrows():
                st.write(row['Artisan_Name'])

    else:
        st.write("Please select all criteria to get recommendations.") 

# Run the Streamlit app
if __name__ == "__main__":
    main()
